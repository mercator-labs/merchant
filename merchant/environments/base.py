from __future__ import annotations

import gym


class BaseMarketEnvironment(gym.Env):
    virtual: bool = True
