from time import sleep, time
from loguru import logger
from prometheus_client import start_http_server

from balanced_exporter.metrics import prom_metrics
from balanced_exporter.config import settings
# Exporters
from balanced_exporter.exporters.band import check_band


def main():
    logger.info("Starting metrics server.")
    start_http_server(settings.METRICS_PORT, settings.METRICS_ADDRESS)

    while True:
        check_band()

        prom_metrics.crons_ran.inc()
        prom_metrics.crons_last_timestamp.set(time())
        logger.info("Sleeping after crons.")
        sleep(settings.CRON_SLEEP_SEC)


if __name__ == '__main__':
    main()
