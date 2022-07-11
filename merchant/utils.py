from __future__ import annotations

from contextlib import contextmanager
from collections.abc import Generator

import ray

from merchant.config import Config


@contextmanager
def ray_runtime(config: Config) -> Generator[None, None, None]:
    ray.init()
    try:
        yield
    finally:
        ray.shutdown()
