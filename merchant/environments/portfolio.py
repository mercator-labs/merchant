from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from abc import abstractproperty

import pandas as pd

from merchant.environments.market import Symbol
from merchant.exceptions import NotEnoughtAssets


class Asset(ABC):
    @abstractmethod
    def decrease(self, amount: float) -> None:
        ...

    @abstractmethod
    def increase(self, amount: float) -> None:
        ...

    @abstractproperty
    def amount(self) -> float:
        ...


class Position(Asset):
    _symbol: Symbol
    _amount: float

    def __init__(self, symbol: Symbol) -> None:
        self._symbol = symbol
        self._amount = 0

    def decrease(self, amount: float) -> None:
        if self._amount < amount:
            raise NotEnoughtAssets('position is too small')
        self._amount -= amount

    def increase(self, amount: float) -> None:
        self._amount += amount

    @property
    def amount(self) -> float:
        return self._amount

    def __repr__(self) -> str:
        return f'{type(self).__name__}(symbol={self._symbol}, amount={self._amount})'


class Liquidity(Asset):
    _currency: str
    _liquidity: float

    def __init__(self, liquidity: float = 1000, currency: str = 'USD') -> None:
        self._liquidity = liquidity
        self._currency = currency

    def increase(self, amount: float) -> None:
        if self._liquidity < amount:
            raise NotEnoughtAssets('liquidity is too small')
        self._liquidity -= amount

    def decrease(self, amount: float) -> None:
        self._liquidity += amount

    @property
    def amount(self) -> float:
        return self._liquidity

    @property
    def liquidity(self) -> float:
        '''alias for amount'''
        return self.amount

    def __repr__(self) -> str:
        return f'{type(self).__name__}(liquidity={self._liquidity}, currency={self._currency})'


class BasePortfolio(ABC):
    _positions: dict[Symbol, Position]
    _liquidity: Liquidity

    @abstractproperty
    def buying_power(self) -> float:
        ...

    @abstractproperty
    def observation(self) -> pd.DataFrame:
        ...


class VirtualPortfolio(BasePortfolio):
    def __init__(self, starting_capital: float) -> None:
        self._positions = {}
        self._liquidity = Liquidity(starting_capital)

    @property
    def buying_power(self) -> float:
        return self._liquidity.amount

    def incrase_position(self, symbol: Symbol, amount: float) -> None:
        if symbol not in self._positions:
            self._positions[symbol] = Position(symbol=symbol)
        self._positions[symbol].increase(amount)

    def decrease_position(self, symbol: Symbol, amount: float) -> None:
        if symbol not in self._positions or self._positions[symbol].amount < amount:
            raise NotEnoughtAssets('position is too small')
        self._positions[symbol].decrease(amount)

    def incrase_liquidity(self, amount: float) -> None:
        self._liquidity.increase(amount)

    def decrease_liquidity(self, amount: float) -> None:
        if self._liquidity.amount < amount:
            raise NotEnoughtAssets('liquidity is too small')
        self._liquidity.decrease(amount)

    @property
    def observation(self) -> pd.DataFrame:
        return pd.DataFrame()
