def run():
    n = int(input())
    stamps = set()
    for _ in range(n):
        stamps.add(input())
    print(len(stamps))


if __name__ == '__main__':
    run()
