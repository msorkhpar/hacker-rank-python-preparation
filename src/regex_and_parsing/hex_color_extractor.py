import re


def run() -> None:
    n = int(input().strip())
    input_lines = []
    for _ in range(n):
        input_lines.append(input())
    print("\n".join(extract_hex_codes(input_lines)))


def extract_hex_codes(input_lines: list) -> list:
    result = []
    for line in input_lines:
        locator = re.findall(r'(?<=[ :])(?=#[0-9a-fA-F]{3}[^0-9a-fA-F])#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}', line)
        if locator:
            for location in locator:
                result.append(location)
    return result


if __name__ == '__main__':
    run()
