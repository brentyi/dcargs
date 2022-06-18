from __future__ import annotations

import dataclasses
import enum
import pathlib
from typing import Tuple

import dcargs


def main(
    source: pathlib.Path,
    dest: pathlib.Path,
    /,  # Mark the end of positional arguments.
    optimizer: OptimizerConfig,
    force: bool = False,
    verbose: bool = False,
    background_rgb: Tuple[float, float, float] = (1.0, 0.0, 0.0),
) -> None:
    """Command-line interface defined using a function signature. Note that this
    docstring is parsed to generate helptext.

    Args:
        source: Path to move data from.
        dest: Path to move data to.
        optimizer: Configuration for our optimizer object.
        force: Do not prompt before overwriting.
        verbose: Explain what is being done.
        background_rgb: Background color. Red by default.
    """
    print(
        f"{source.absolute()=}"
        "\n"
        f"{dest.absolute()=}"
        "\n"
        f"{optimizer=}"
        "\n"
        f"{force=}"
        "\n"
        f"{verbose=}"
        "\n"
        f"{background_rgb=}"
    )


class OptimizerType(enum.Enum):
    ADAM = enum.auto()
    SGD = enum.auto()


@dataclasses.dataclass(frozen=True)
class OptimizerConfig:
    algorithm: OptimizerType = OptimizerType.ADAM
    """Gradient-based optimizer to use."""

    learning_rate: float = 3e-4
    """Learning rate to use."""

    weight_decay: float = 1e-2
    """Coefficient for L2 regularization."""


if __name__ == "__main__":
    dcargs.cli(main)
