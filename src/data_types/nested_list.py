def compare(item):
    return item[1], item[0]


def run():
    n = int(input())
    records = [[input(), float(input())] for _ in range(n)]
    sorted_records = sorted(records, key=compare)
    print_second_lowest_mark(sorted_records)


def print_second_lowest_mark(sorted_records: list):
    result = []
    lowest_mark = sorted_records[0][1]
    for i in range(1, len(sorted_records)):
        if sorted_records[i][1] == lowest_mark:
            continue
        elif len(result) == 0:
            result.append(sorted_records[i])
        else:
            if sorted_records[i][1] == result[0][1]:
                result.append(sorted_records[i])
            else:
                break
    print("\n".join(name for name, mark in result))


if __name__ == '__main__':
    run()
