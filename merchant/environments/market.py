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
from merchant.environments.portfolio import BasePortfolio
from merchant.exceptions import OrderDidNotFill


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

    @abstractproperty
    def observation(self) -> pd.DataFrame:
        ...

    @abstractmethod
    def get_quote(self, symbol: Symbol) -> float:
        ...

    @abstractmethod
    def buy_at(self, symbol: Symbol, amount: float, price: float) -> None:
        ...

    @abstractmethod
    def sell_at(self, symbol: Symbol, amount: float, price: float) -> None:
        ...


class HistoricalMarket(BaseMarket):

    _fee_policy: FeePolicy
    _symbols: set[Symbol]
    _datasource: HisoricalDatasource

    def __init__(self, fee_policy: FeePolicy, symbols: Iterable[Symbol]) -> None:
        self._fee_policy = fee_policy
        self._symbols = set(symbols)

    @property
    def observation(self) -> pd.DataFrame:
        return pd.DataFrame()

    def get_quote(self, symbol: Symbol) -> float:
        return 100 * random.random()

    def buy_at(self, symbol: Symbol, amount: float, price: float) -> None:
        raise OrderDidNotFill()

    def sell_at(self, symbol: Symbol, amount: float, price: float) -> None:
        raise OrderDidNotFill()
