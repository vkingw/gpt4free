from __future__ import annotations

import os
import json

from ...typing import Messages, AsyncResult
from ...errors import MissingAuthError, ModelNotFoundError
from ..template import OpenaiTemplate

class Azure(OpenaiTemplate):
    url = "https://ai.azure.com"
    api_base = "https://host.g4f.dev/api/Azure"
    working = True
    needs_auth = True
    active_by_default = True
    login_url = "https://discord.gg/qXA4Wf4Fsm"
    routes: dict[str, str] = {}
    audio_models = ["gpt-4o-mini-audio-preview"]
    vision_models = ["gpt-4.1", "o4-mini", "model-router"]
    model_extra_body = {
        "gpt-4o-mini-audio-preview": {
            "audio": {
                "voice": "alloy",
                "format": "mp3"
            },
            "modalities": ["text", "audio"],
            "stream": False
        }
    }

    @classmethod
    def get_models(cls, api_key: str = None, **kwargs) -> list[str]:
        routes = os.environ.get("AZURE_ROUTES")
        if routes:
            try:
                routes = json.loads(routes)
            except json.JSONDecodeError:
                raise ValueError(f"Invalid AZURE_ROUTES environment variable format: {routes}")
            cls.routes = routes
        if cls.routes:
            return list(cls.routes.keys())
        return super().get_models(api_key=api_key, **kwargs)

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        api_key: str = None,
        api_endpoint: str = None,
        **kwargs
    ) -> AsyncResult:
        if not model:
            model = os.environ.get("AZURE_DEFAULT_MODEL", cls.default_model)
        if model in cls.model_extra_body:
            for key, value in cls.model_extra_body[model].items():
                kwargs.setdefault(key, value)
        if not api_key:
            raise ValueError(f"API key is required for Azure provider. Ask for API key in the {cls.login_url} Discord server.")
        if not api_endpoint:
            if not cls.routes:
                cls.get_models()
            api_endpoint = cls.routes.get(model)
            if cls.routes and not api_endpoint:
                raise ModelNotFoundError(f"No API endpoint found for model: {model}")
        if not api_endpoint:
            api_endpoint = os.environ.get("AZURE_API_ENDPOINT")
        try:
            async for chunk in super().create_async_generator(
                model=model,
                messages=messages,
                api_key=api_key,
                api_endpoint=api_endpoint,
                **kwargs
            ):
                yield chunk
        except MissingAuthError as e:
            raise MissingAuthError(f"{e}. Ask for help in the {cls.login_url} Discord server.") from e