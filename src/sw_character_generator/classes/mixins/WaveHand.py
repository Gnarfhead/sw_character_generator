class WaveMixin:
    """Mixin für das 'wave_hand'-Verhalten."""

    def wave_hand(self) -> None:
        """Let the character wave their hand."""
        name = getattr(self, "name", None) or "Unknown"
        print(f"{name} waves hand")