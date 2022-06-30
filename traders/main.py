from __future__ import annotations

from argparse import ArgumentParser
from argparse import Namespace

from traders.commands.backtest import backtest_main
from traders.commands.trade import trade_main
from traders.commands.train import train_main
from traders.config import get_config
from traders.ray_runtime import ray_runtime


def parser_args() -> Namespace:
    parser = ArgumentParser()
    return parser.parse_args()


def main() -> int:
    args = parser_args()
    config = get_config(args)  # noqa

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
