#!/bin/python3
def run():
    n = int(input().strip())

    is_even = n % 2 == 0
    if not is_even:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")


if __name__ == '__main__':
    run()
