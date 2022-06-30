from __future__ import annotations

import gym


class BaseEnvironment(gym.Env):
    virtual: bool = True
