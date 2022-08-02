import requests
from loguru import logger

from balanced_exporter.config import settings


def get_last_tx(address: str, limit: int = 1):
    endpoint = f"{settings.COMMUNITY_API_ENDPOINT}/api/v1/transactions/address/{address}?limit={limit}"
    output = requests.get(endpoint)
    if output.status_code == 200:
        return output.json()
    else:
        logger.info(output.raw)
        return None
