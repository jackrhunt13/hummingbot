from decimal import Decimal

from hummingbot.client.config.config_methods import using_exchange
from hummingbot.client.config.config_var import ConfigVar
from hummingbot.connector.exchange.gate_io import gate_io_constants as CONSTANTS
from hummingbot.core.data_type.trade_fee import TradeFeeSchema


import time

CENTRALIZED = True
EXAMPLE_PAIR = "BTC-USDT"
DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.002"),
    taker_percent_fee_decimal=Decimal("0.002"),
)

KEYS = {
    "gate_io_api_key":
        ConfigVar(key="gate_io_api_key",
                  prompt=f"Enter your {CONSTANTS.EXCHANGE_NAME} API key >>> ",
                  required_if=using_exchange("gate_io"),
                  is_secure=True,
                  is_connect_key=True),
    "gate_io_secret_key":
        ConfigVar(key="gate_io_secret_key",
                  prompt=f"Enter your {CONSTANTS.EXCHANGE_NAME} secret key >>> ",
                  required_if=using_exchange("gate_io"),
                  is_secure=True,
                  is_connect_key=True),
}

def seconds():
    return int(time.time())


def milliseconds():
    return int(time.time() * 1000)


def microseconds():
    return int(time.time() * 1000000)


def convert_from_exchange_trading_pair(exchange_trading_pair: str) -> str:
    return exchange_trading_pair.replace("_", "-")


def convert_to_exchange_trading_pair(hb_trading_pair: str) -> str:
    return hb_trading_pair.replace("-", "_")