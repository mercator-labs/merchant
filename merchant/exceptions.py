from __future__ import annotations


class MerchantException(Exception):
    pass


class PortfolioException(Exception):
    pass


class NoPosition(PortfolioException):
    pass


class NotEnoughtAssets(PortfolioException):
    pass


class MarketError(Exception):
    pass


class OrderDidNotFill(MarketError):
    pass


class ActionError(MerchantException):
    pass
