from __future__ import annotations

from argparse import Namespace
from dataclasses import dataclass


@dataclass
class Config:
    pass


def get_config(ns: Namespace) -> Config:
    return Config()
