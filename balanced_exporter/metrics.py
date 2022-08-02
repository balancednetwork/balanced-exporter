from prometheus_client import Counter, Gauge


class Metrics:
    def __init__(self):

        self.crons_ran = Counter(
            "crons_ran",
            "Cron jobs ran.",
        )

        self.crons_last_timestamp = Gauge(
            "crons_last_timestamp",
            "Last timestamp running a cron.",
        )

        self.band_oracle_balance = Gauge(
            "band_oracle_balance",
            "Balance of the band oracle contract.",
        )

        self.band_oracle_last_tx_timestamp = Gauge(
            "band_oracle_last_tx_timestamp",
            "Last tx timestamp of the band oracle contract.",
        )

        self.band_oracle_time_since_last_tx = Gauge(
            "band_oracle_time_since_last_tx",
            "Last tx timestamp of the band oracle contract.",
        )



prom_metrics = Metrics()
