import re


def decode_text(matrix: [[]]) -> [[]]:
    result = ""
    for row in matrix:
        result += str.join("", row)
    return result


def clean_it(decoded_text: str) -> str:
    return re.sub(r"([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])", r"\1 \2", decoded_text)


def run() -> None:
    n, m = map(int, input().rstrip().split())
    matrix = [[] * m] * n

    for i in range(n):
        matrix[i] = list(input())

    matrix = zip(*matrix)
    decoded_text = decode_text(matrix)
    result = clean_it(decoded_text)
    print(result)


if __name__ == '__main__':
    run()
