def run():
    year = int(input())
    print(is_leap(year))


def is_leap(year):
    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False


if __name__ == '__main__':
    run()
