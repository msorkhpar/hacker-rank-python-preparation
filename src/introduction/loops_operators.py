def run(func):
    number = int(input())
    func(number)


def run_with_for(number):
    for i in range(0, number):
        print(i ** 2)


def run_with_while(number):
    i = 0
    while i < number:
        print(i ** 2)
        i += 1


def run_with_lambda(number):
    [print(i ** 2) for i in range(0, number)]


if __name__ == '__main__':
    run(run_with_for)
