from datetime import datetime
from time import time

from balanced_exporter.addresses import addresses
from balanced_exporter.utils.rpc import get_balance, convert_hex_int
from balanced_exporter.utils.retry import retry
from balanced_exporter.metrics import prom_metrics
from balanced_exporter.utils.api import get_last_tx


def check_band():
    # Get balance
    balance_response = retry(get_balance, address=addresses.BAND_ORACLE)
    if balance_response is not None:
        balance = convert_hex_int(balance_response.json()['result']) / 1e18
        prom_metrics.band_oracle_balance.set(balance)


    # Get last Tx
    last_tx_response = retry(get_last_tx, address=addresses.BAND_ORACLE)
    if last_tx_response is not None:
        last_tx_timestamp = last_tx_response[0]['block_timestamp']
        prom_metrics.band_oracle_last_tx_timestamp.set(last_tx_timestamp)

        time_since_last_tx = (time() * 1e6 - last_tx_timestamp) / 1e6
        prom_metrics.band_oracle_time_since_last_tx.set(time_since_last_tx)
