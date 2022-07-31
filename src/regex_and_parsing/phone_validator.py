from __future__ import annotations

import re


def run():
    n = int(input().strip())
    for _ in range(n):
        number = input()
        if is_valid(number):
            print("YES")
        else:
            print("NO")


def is_valid(number) -> re.Match | None:
    return re.match(r'^[789]\d{9}$', number)


if __name__ == '__main__':
    run()
