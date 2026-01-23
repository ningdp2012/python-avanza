"""
Avanza API Client Package
A Python package for interacting with Avanza's unofficial APIs
"""

__version__ = "0.1.0"

from .client import AvanzaClient
from .constants import InstrumentType, TimePeriod
from .exceptions import (
    AvanzaAPIError,
    AvanzaError,
    AvanzaNetworkError,
    AvanzaRateLimitError,
)
from .ticker import ETF, Fund, Stock, search

__all__ = [
    "AvanzaClient",
    "Stock",
    "ETF",
    "Fund",
    "search",
    "TimePeriod",
    "InstrumentType",
    "AvanzaError",
    "AvanzaAPIError",
    "AvanzaRateLimitError",
    "AvanzaNetworkError",
]
