import dataclasses
import enum
from typing import List, Optional, Sequence, Set, Tuple

import pytest
from typing_extensions import Literal

import dcargs


def test_tuples_fixed():
    @dataclasses.dataclass
    class A:
        x: Tuple[int, int, int]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=(1, 2, 3))
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_tuples_fixed_mixed():
    @dataclasses.dataclass
    class A:
        x: Tuple[int, str, int]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=(1, "2", 3))
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_tuples_with_default():
    @dataclasses.dataclass
    class A:
        x: Tuple[int, int, int] = (0, 1, 2)

    assert dcargs.cli(A, args=[]) == A(x=(0, 1, 2))
    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=(1, 2, 3))
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])


def test_tuples_fixed_multitype():
    @dataclasses.dataclass
    class A:
        x: Tuple[int, str, float]

    assert dcargs.cli(A, args=["--x", "1", "2", "3.5"]) == A(x=(1, "2", 3.5))
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_tuples_fixed_bool():
    @dataclasses.dataclass
    class A:
        x: Tuple[bool, bool, bool]

    assert dcargs.cli(A, args=["--x", "True", "True", "False"]) == A(
        x=(True, True, False)
    )
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_tuples_variable():
    @dataclasses.dataclass
    class A:
        x: Tuple[int, ...]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=(1, 2, 3))
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_tuples_variable_bool():
    @dataclasses.dataclass
    class A:
        x: Tuple[bool, ...]

    assert dcargs.cli(A, args=["--x", "True", "True", "False"]) == A(
        x=(True, True, False)
    )
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_tuples_variable_optional():
    @dataclasses.dataclass
    class A:
        x: Optional[Tuple[int, ...]]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=(1, 2, 3))
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    assert dcargs.cli(A, args=[]) == A(x=None)


def test_sequences():
    @dataclasses.dataclass
    class A:
        x: Sequence[int]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=[1, 2, 3])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_lists():
    @dataclasses.dataclass
    class A:
        x: List[int]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=[1, 2, 3])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_list_with_literal():
    @dataclasses.dataclass
    class A:
        x: List[Literal[1, 2, 3]]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=[1, 2, 3])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x", "1", "2", "3", "4"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_list_with_enums():
    class Color(enum.Enum):
        RED = enum.auto()
        GREEN = enum.auto()
        BLUE = enum.auto()

    @dataclasses.dataclass
    class A:
        x: List[Color]

    assert dcargs.cli(A, args=["--x", "RED", "RED", "BLUE"]) == A(
        x=[Color.RED, Color.RED, Color.BLUE]
    )
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x", "RED", "RED", "YELLOW"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_lists_with_default():
    class Color(enum.Enum):
        RED = enum.auto()
        GREEN = enum.auto()
        BLUE = enum.auto()

    @dataclasses.dataclass
    class A:
        x: List[Color] = dataclasses.field(
            default_factory=[Color.RED, Color.GREEN].copy
        )

    assert dcargs.cli(A, args=[]) == A(x=[Color.RED, Color.GREEN])
    assert dcargs.cli(A, args=["--x", "RED", "GREEN", "BLUE"]) == A(
        x=[Color.RED, Color.GREEN, Color.BLUE]
    )


def test_lists_bool():
    @dataclasses.dataclass
    class A:
        x: List[bool]

    assert dcargs.cli(A, args=["--x", "True", "False", "True"]) == A(
        x=[True, False, True]
    )
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_sets():
    @dataclasses.dataclass
    class A:
        x: Set[int]

    assert dcargs.cli(A, args=["--x", "1", "2", "3", "3"]) == A(x={1, 2, 3})
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=[])


def test_sets_with_default():
    @dataclasses.dataclass
    class A:
        x: Set[int] = dataclasses.field(default_factory={0, 1, 2}.copy)

    assert dcargs.cli(A, args=[]) == A(x={0, 1, 2})
    assert dcargs.cli(A, args=["--x", "1", "2", "3", "3"]) == A(x={1, 2, 3})
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])


def test_optional_sequences():
    @dataclasses.dataclass
    class A:
        x: Optional[Sequence[int]]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=[1, 2, 3])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    assert dcargs.cli(A, args=[]) == A(x=None)


def test_optional_lists():
    @dataclasses.dataclass
    class A:
        x: Optional[List[int]]

    assert dcargs.cli(A, args=["--x", "1", "2", "3"]) == A(x=[1, 2, 3])
    with pytest.raises(SystemExit):
        dcargs.cli(A, args=["--x"])
    assert dcargs.cli(A, args=[]) == A(x=None)
