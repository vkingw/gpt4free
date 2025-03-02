from __future__ import annotations

import json

from ..typing import AsyncResult, Messages, ImagesType
from ..providers.asyncio import to_async_iterator
from ..client.service import get_model_and_provider
from ..client.helper import filter_json
from .base_provider import AsyncGeneratorProvider
from .response import ToolCalls, FinishReason

class ToolSupportProvider(AsyncGeneratorProvider):
    working = True

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool = True,
        images: ImagesType = None,
        tools: list[str] = None,
        response_format: dict = None,
        **kwargs
    ) -> AsyncResult:
        provider = None
        if ":" in model:
            provider, model = model.split(":", 1)
        model, provider = get_model_and_provider(
            model, provider,
            stream, logging=False,
            has_images=images is not None
        )
        if tools is not None:
            if len(tools) > 1:
                raise ValueError("Only one tool is supported.")
            if response_format is None:
                response_format = {"type": "json"}
            tools = tools.pop()
            lines = ["Respone in JSON format."]
            properties = tools["function"]["parameters"]["properties"]
            properties = {key: value["type"] for key, value in properties.items()}
            lines.append(f"Response format: {json.dumps(properties, indent=2)}")
            messages = [{"role": "user", "content": "\n".join(lines)}] + messages

        finish = None
        chunks = []
        async for chunk in provider.get_async_create_function()(
            model,
            messages,
            stream=stream,
            images=images,
            response_format=response_format,
            **kwargs
        ):
            if isinstance(chunk, FinishReason):
                finish = chunk
                break
            elif isinstance(chunk, str):
                chunks.append(chunk)
            else:
                yield chunk

        chunks = "".join(chunks)
        if tools is not None:
            yield ToolCalls([{
                "id": "",
                "type": "function",
                "function": {
                    "name": tools["function"]["name"],
                    "arguments": filter_json(chunks)
                }
            }])
        yield chunks
        if finish is not None:
            yield finish