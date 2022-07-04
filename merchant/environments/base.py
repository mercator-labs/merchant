from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any

import gym
from gym.spaces import MultiDiscrete

from merchant.environments.market import BaseMarket
from merchant.environments.market import Symbol
from merchant.environments.portfolio import BasePortfolio


class Action(ABC):

    _dispatch_timestamp: int
    _execution_timestamp: None | int = None

    @abstractmethod
    def execute(self, pf: BasePortfolio, mt: BaseMarket) -> None:
        ...


class BuyAction(Action):

    _symbol: Symbol
    _amount: float

    def __init__(self, ts: int, symbol: Symbol, amount: float) -> None:
        self._dispatch_timestamp = ts
        self._symbol = symbol
        self._amount = amount

    def execute(self, pf: BasePortfolio, mt: BaseMarket) -> None:
        raise NotImplementedError


class SellAction(Action):

    _symbol: Symbol
    _amount: float

    def __init__(self, ts: int, symbol: Symbol, amount: float) -> None:
        self._dispatch_timestamp = ts
        self._symbol = symbol
        self._amount = amount

    def execute(self, pf: BasePortfolio, mt: BaseMarket) -> None:
        raise NotImplementedError


class NoAction(Action):
    def __init__(self, ts: int) -> None:
        self._dispatch_timestamp = ts

    def execute(self, pf: BasePortfolio, mt: BaseMarket) -> None:
        return


class BaseMarketEnvironment(gym.Env):
    _action_history: list[Action]
    _symbols: list[Symbol]

    # add realtime view with plotly?
    metadata: dict[str, Any] = {'render_modes': []}

    def __init__(self, symbols: list[Symbol]) -> None:
        self._symbols = symbols
        self._action_history = []
        self.action_space = MultiDiscrete([3] * len(symbols))

    def reset(self) -> None:
        self._action_history = []

    def step(self, action: list[int]) -> tuple[Any, float, bool, dict[str, Any]]:
        ...
