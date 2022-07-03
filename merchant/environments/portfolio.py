from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from abc import abstractproperty

from merchant.exceptions import NotEnoughtAssets


class Asset(ABC):
    @abstractmethod
    def decrease(self, amount: float) -> None:
        ...

    @abstractmethod
    def increase(self, amount: float) -> None:
        ...

    @abstractproperty
    def size(self) -> float:
        ...


class Position(Asset):
    symbol: str
    amount: float

    def decrease(self, amount: float) -> None:
        if self.amount < amount:
            raise NotEnoughtAssets('position is too small')
        self.amount -= amount

    def increase(self, amount: float) -> None:
        self.amount += amount

    @property
    def size(self) -> float:
        return self.amount


class LiquidityPool(Asset):
    liquidity: float

    def __init__(self, liquidity: float) -> None:
        self.liquidity = liquidity

    def increase(self, amount: float) -> None:
        if self.liquidity < amount:
            raise NotEnoughtAssets('liquidity is too small')
        self.liquidity -= amount

    def decrease(self, amount: float) -> None:
        self.liquidity += amount

    @property
    def size(self) -> float:
        return self.liquidity


class VirtualPortfolio:
    positions: dict[str, Position]
    liquidity: LiquidityPool

    def __init__(self, starting_capital: float) -> None:
        self.positions = {}
        self.liquidity = LiquidityPool(starting_capital)
