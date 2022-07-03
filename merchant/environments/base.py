from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import gym

from merchant.environments.market import BaseMarket
from merchant.environments.portfolio import VirtualPortfolio


class Action(ABC):
    @abstractmethod
    def execute(self, pf: VirtualPortfolio, mt: BaseMarket) -> None:
        ...


class BuyAction(Action):
    def execute(self, pf: VirtualPortfolio, mt: BaseMarket) -> None:
        raise NotImplementedError


class SellAction(Action):
    def execute(self, pf: VirtualPortfolio, mt: BaseMarket) -> None:
        raise NotImplementedError


class NoAction(Action):
    def execute(self, pf: VirtualPortfolio, mt: BaseMarket) -> None:
        return


class BaseMarketEnvironment(gym.Env):
    virtual: bool = True
