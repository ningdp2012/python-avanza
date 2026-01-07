"""
Example usage of Avanza API client
"""

import avanza

# =============================================================================
# Stock Usage
# =============================================================================

# Create a stock ticker
stock = avanza.Stock("5361")  # Avanza Bank Holding

# Basic info
info = stock.info
price = stock.price
history = stock.history("one_month")
dividend = stock.dividend

# Dynamic attributes from get_stock_details()
company = stock.company
stock_details = stock.stock
events = stock.companyEvents

# Access nested data with dot notation
ceo = stock.company.ceo
total_shares = stock.company.totalNumberOfShares
num_shares = stock.stock.numberOfShares


# =============================================================================
# ETF Usage
# =============================================================================

# Create an ETF ticker
etf = avanza.ETF("1063549")

# Basic info
info = etf.info
price = etf.price
history = etf.history("three_months")
dividend = etf.dividend

# Dynamic attributes from get_etf_details()
# All keys from API response are accessible as attributes


# =============================================================================
# Fund Usage
# =============================================================================

# Create a fund ticker
fund = avanza.Fund("41567")

# Basic info
info = fund.info
price = fund.price
history = fund.history("one_year")


# =============================================================================
# Search
# =============================================================================

# Search for instruments
results = avanza.search("avanza", instrument_type="stock", limit=5)


# =============================================================================
# Cache Management
# =============================================================================

# Default cache: 60 seconds
stock = avanza.Stock("5361")

# Custom cache: 5 minutes
stock = avanza.Stock("5361", cache_ttl=300)

# No cache
stock = avanza.Stock("5361", cache_ttl=0)

# Manual refresh
stock.refresh()


# =============================================================================
# TimePeriod Options
# =============================================================================

# Using strings
history = stock.history("one_week")
history = stock.history("one_month")
history = stock.history("three_months")
history = stock.history("one_year")

# Using enum
history = stock.history(avanza.TimePeriod.ONE_WEEK)
history = stock.history(avanza.TimePeriod.ONE_MONTH)
