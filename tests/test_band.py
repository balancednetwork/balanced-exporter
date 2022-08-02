from balanced_exporter.exporters.band import check_band
from balanced_exporter.metrics import prom_metrics


def test_check_band():
    check_band()

    # Check that balance is over 10 icx
    assert prom_metrics.band_oracle_balance._value.get() > 10
    # Check that band has run within 800 seconds
    assert prom_metrics.band_oracle_time_since_last_tx._value.get() < 800
