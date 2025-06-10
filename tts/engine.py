class TTSEngine:
    """Placeholder TTS engine using an ONNX model."""

    def __init__(self, model_path: str):
        self.model_path = model_path
        # Actual model loading would go here

    def synthesize(self, text: str) -> bytes:
        """Return PCM16 audio bytes for the given text (stub)."""
        raise NotImplementedError("TTS synthesis not implemented")
