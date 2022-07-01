from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

import ray
from traders.config import Config


@contextmanager
def ray_runtime(config: Config) -> Generator[None, None, None]:
    ray.init()
    try:
        yield
    finally:
        ray.shutdown()
