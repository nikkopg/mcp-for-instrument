from unitelabs.bus import Protocol, create_serial_connection


class McpForInstrumentProtocol(Protocol):
    """Underlying communication protocol for Mantis."""

    def __init__(self, **kwargs):
        kwargs["port"] = "/dev/ttyUSB0"  # FIXME: set device port
        super().__init__(create_serial_connection, **kwargs)
