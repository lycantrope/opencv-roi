import pathlib
import struct
import sys
from subprocess import PIPE
from subprocess import Popen


def retrieve() -> tuple[int, int]:
    home = pathlib.Path(__file__).resolve().parent
    runner = home.joinpath("__runner__.py")
    cache_file = home.joinpath("__pycache__", "__cache__")
    if not cache_file.is_file():
        proc = Popen(
            [sys.executable, str(runner).encode()],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        )
        proc.communicate()
    recv = cache_file.read_bytes()
    return struct.unpack("<ll", recv)


SCREEN_WIDTH, SCREEN_HEIGHT = retrieve()

__all__ = ["SCREEN_WIDTH", "SCREEN_HEIGHT"]
