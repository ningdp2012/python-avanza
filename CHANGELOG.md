# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-07

### Added
- Initial release of python-avanza
- yfinance-style API for stocks, ETFs, and funds
- Search functionality for instruments by name and type
- Historical price data retrieval with flexible time periods
- Current price and NAV data access
- Dividend information for stocks and ETFs
- Automatic caching with configurable TTL
- Comprehensive test suite
- Type hints throughout the codebase
- Error handling with custom exceptions
- Retry logic with exponential backoff
- GitHub Actions workflows for testing, linting, and publishing

### Features
- **Stock class**: Access stock data with orderbook ID
- **ETF class**: Access ETF data with orderbook ID
- **Fund class**: Access fund data with orderbook ID
- **search()**: Search for instruments by name and type
- **TimePeriod enum**: Predefined time periods for historical data
- **Cache management**: Configurable TTL and manual refresh capability

### Documentation
- Comprehensive README with examples
- API usage examples in example.py
- Inline code documentation and docstrings
- Clear disclaimer about unofficial API usage
