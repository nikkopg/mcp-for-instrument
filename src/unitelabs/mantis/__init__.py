import dataclasses
import collections.abc
from importlib.metadata import version

from unitelabs.cdk import Connector, ConnectorBaseConfig, SiLAServerConfig

from .io.mantis_protocol import McpForInstrumentProtocol

__version__ = version("unitelabs-mcp-for-instrument")


@dataclasses.dataclass
class McpForInstrumentConfig(ConnectorBaseConfig):
    """Configuration for the Mantis."""

    sila_server: SiLAServerConfig = dataclasses.field(
        default_factory=lambda: SiLAServerConfig(
            name="Mantis",
            type="Example",
            description=(
                """
            A connector for the Mantis built with the UniteLabs CDK.
            """
            ),
            version=str(__version__),
            vendor_url="https://unitelabs.io/",
        )
    )


async def create_app(config: McpForInstrumentConfig) -> collections.abc.AsyncGenerator[Connector, None]:
    """Create the connector application."""
    app = Connector(config)

    protocol = McpForInstrumentProtocol()
    await protocol.open()

    yield app

    protocol.close()
