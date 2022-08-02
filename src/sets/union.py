def get_enrollment():
    input()
    return set(map(int, input().split()))


def run():
    english_class = get_enrollment()
    french_class = get_enrollment()

    print(len(english_class.union(french_class)))


if __name__ == '__main__':
    run()
