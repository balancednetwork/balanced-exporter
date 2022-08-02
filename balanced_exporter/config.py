import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    NAME: str = "balanced-exporter"
    NETWORK_NAME: str = "mainnet"

    # Metrics
    METRICS_PORT: int = 9400
    METRICS_ADDRESS: str = "localhost"

    # ICON Nodes
    ICON_NODE_URL: str = "https://api.icon.community/api/v3"

    # Community API
    COMMUNITY_API_ENDPOINT: str = "https://tracker.icon.community"

    # Loop
    CRON_SLEEP_SEC: int = 30

    class Config:
        case_sensitive = True


if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
else:
    settings = Settings()
