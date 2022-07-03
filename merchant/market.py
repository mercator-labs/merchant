from __future__ import annotations

import random
from abc import ABC
from typing import Protocol

from merchant.exceptions import NoPosition
from merchant.exceptions import NotEnoughtAssets
from merchant.portfolio import Portfolio


class FeePolicy(Protocol):
    def __call__(self, price: float, amount: float) -> float:
        ...


def get_default_policy(pct: float) -> FeePolicy:
    def policy(price: float, amount: float) -> float:
        return price * amount * pct

    return policy


class BaseMarket:

    _fee_policy: FeePolicy
    _symbol: str = '__base__'

    def __init__(self, fee_policy: float | FeePolicy) -> None:
        if isinstance(fee_policy, float):
            self._fee_policy = get_default_policy(fee_policy)
        else:
            self._fee_policy = fee_policy

    @property
    def price(self) -> float:
        return 100 * random.random()

    def buy(self, pf: Portfolio, amount: int) -> None:
        cost = self.price * amount + self._fee_policy(self.price, amount)
        pf.liquidity.decrease(cost)
        pf.positions[self._symbol].increase(amount)
        return

    def sell(self, pf: Portfolio, amount: int) -> None:
        if self._symbol not in pf.positions:
            raise NoPosition()
        cost = self.price * amount
        pf.positions[self._symbol].decrease(amount)
        pf.liquidity.increase(cost)
        return
