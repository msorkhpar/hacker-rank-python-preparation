def inclusive_range(upper_bound):
    return range(upper_bound + 1)


def run():
    x, y, z, n = (int(input()) for _ in range(4))
    numbers = [
        [a, b, c]
        for a in inclusive_range(x)
        for b in inclusive_range(y)
        for c in inclusive_range(z)
        if a + b + c != n
    ]
    print(numbers)


if __name__ == '__main__':
    run()
