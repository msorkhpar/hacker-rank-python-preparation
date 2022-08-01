def run():
    n = int(input())
    largest = runner_up = -101
    for number in map(int, input().strip().split(" ")):
        if runner_up < number:
            if number > largest:
                runner_up, largest = largest, number
            elif runner_up < number != largest:
                runner_up = number
    print(runner_up)


if __name__ == '__main__':
    run()
