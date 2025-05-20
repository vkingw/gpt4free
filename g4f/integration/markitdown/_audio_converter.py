from typing import Any, BinaryIO

from markitdown.converters._exiftool import exiftool_metadata
from markitdown._base_converter import DocumentConverter, DocumentConverterResult
from markitdown._stream_info import StreamInfo
from markitdown._exceptions import MissingDependencyException

from ._transcribe_audio import transcribe_audio

ACCEPTED_MIME_TYPE_PREFIXES = [
    "audio/x-wav",
    "audio/mpeg",
    "video/mp4",
    "video/webm",
    "audio/webm",
]

ACCEPTED_FILE_EXTENSIONS = [
    ".wav",
    ".mp3",
    ".m4a",
    ".mp4",
    ".webm",
]

class AudioConverter(DocumentConverter):
    """
    Converts audio files to markdown via extraction of metadata (if `exiftool` is installed), and speech transcription (if `speech_recognition` is installed).
    """

    def accepts(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        **kwargs: Any,  # Options to pass to the converter
    ) -> bool:
        mimetype = (stream_info.mimetype or "").lower()
        extension = (stream_info.extension or "").lower()

        if extension in ACCEPTED_FILE_EXTENSIONS:
            return True

        for prefix in ACCEPTED_MIME_TYPE_PREFIXES:
            if mimetype.startswith(prefix):
                return True

        return False

    def convert(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        recognition_language: str = None,
        **kwargs: Any,  # Options to pass to the converter
    ) -> DocumentConverterResult:
        md_content = ""

        # Add metadata
        metadata = exiftool_metadata(
            file_stream, exiftool_path=kwargs.get("exiftool_path")
        )
        if metadata:
            for f in [
                "Title",
                "Artist",
                "Author",
                "Band",
                "Album",
                "Genre",
                "Track",
                "DateTimeOriginal",
                "CreateDate",
                # "Duration", -- Wrong values when read from memory
                "NumChannels",
                "SampleRate",
                "AvgBytesPerSec",
                "BitsPerSample",
            ]:
                if f in metadata:
                    md_content += f"{f}: {metadata[f]}\n"

        # Figure out the audio format for transcription
        if stream_info.extension == ".wav" or stream_info.mimetype == "audio/x-wav":
            audio_format = "wav"
        elif stream_info.extension == ".mp3" or stream_info.mimetype == "audio/mpeg":
            audio_format = "mp3"
        elif (
            stream_info.extension in [".mp4", ".m4a"]
            or stream_info.mimetype == "video/mp4"
        ):
            audio_format = "mp4"
        elif stream_info.extension == ".webm" or stream_info.mimetype in ("audio/webm", "video/webm"):
            audio_format = "webm"
        else:
            audio_format = None

        # Transcribe
        if audio_format:
            try:
                md_content = transcribe_audio(file_stream, audio_format=audio_format, language=recognition_language)
            except MissingDependencyException:
                pass

        # Return the result
        return DocumentConverterResult(markdown=md_content.strip())
