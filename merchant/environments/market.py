from __future__ import annotations

import random
from abc import ABC
from abc import abstractmethod
from abc import abstractproperty
from typing import Iterable
from typing import NamedTuple
from typing import Protocol

import pandas as pd

from merchant.datasources.base import BaseDatasource
from merchant.datasources.base import HisoricalDatasource
from merchant.environments.portfolio import VirtualPortfolio
from merchant.exceptions import FailedToFulfill
from merchant.exceptions import NoPosition
from merchant.exceptions import NotEnoughtAssets


class FeePolicy(Protocol):
    def __call__(self, price: float, amount: float) -> float:
        ...


def get_default_policy(pct: float) -> FeePolicy:
    def policy(price: float, amount: float) -> float:
        return price * amount * pct

    return policy


class Symbol(NamedTuple):
    symbol: str


class BaseMarket(ABC):

    _symbols: set[Symbol]
    _datasource: BaseDatasource

    @abstractmethod
    def wait_for_next_tick(self) -> None:
        ...

    @abstractmethod
    def market_price(self, symbol: Symbol) -> float:
        ...

    @abstractproperty
    def observation(self) -> pd.DataFrame:
        ...


class HistoricalMarket(BaseMarket):

    _fee_policy: FeePolicy
    _symbols: set[Symbol]
    _datasource: HisoricalDatasource

    def __init__(self, fee_policy: FeePolicy, symbols: Iterable[Symbol]) -> None:
        self._fee_policy = fee_policy
        self._symbols = set(symbols)

    def market_price(self, symbol: Symbol) -> float:
        return 100 * random.random()

    @property
    def observation(self) -> pd.DataFrame:
        return pd.DataFrame()

    def buy(self, symbol: Symbol, amount: float, price: float) -> None:
        raise FailedToFulfill()

    def sell(self, symbol: Symbol, amount: float, price: float) -> None:
        raise FailedToFulfill()
