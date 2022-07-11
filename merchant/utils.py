from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager

import ray

from merchant.config import Config


@contextmanager
def ray_runtime(config: Config) -> Generator[None, None, None]:
    ray.init()
    try:
        yield
    finally:
        ray.shutdown()
