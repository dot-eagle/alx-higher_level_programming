#!/usr/bin/python3


def func():
    raise ConnectionError

try:
    func()

except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
