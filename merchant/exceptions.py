from __future__ import annotations


class MerchantException(Exception):
    pass


class PortfolioException(Exception):
    pass


class NoPosition(PortfolioException):
    pass


class NotEnoughtAssets(PortfolioException):
    pass
