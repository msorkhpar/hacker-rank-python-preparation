from __future__ import annotations

import email.utils
import re


def run() -> None:

    n = int(input().strip())
    for _ in range(n):
        username, email_address = email.utils.parseaddr(input())
        if is_valid(email_address):
            print(email.utils.formataddr((username, email_address)))


def is_valid(email_address) -> re.Match | None:
    return re.match(r"^[a-zA-Z][\w\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", email_address)


if __name__ == '__main__':
    run()
