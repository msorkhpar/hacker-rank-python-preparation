def decorator(method_name, elements: set, item: int):
    return method_name(elements, item)


def pop_from_elements(elements: set):
    try:
        elements.pop()
    except KeyError:
        pass


def remove_from_elements(elements: set, item: int):
    try:
        elements.remove(item)
    except KeyError:
        pass


def discard_from_elements(elements: set, item: int):
    elements.discard(item)


def run():
    n = int(input())
    elements = set(map(int, input().split()))
    number_of_commands = int(input())
    commands = {
        "pop": pop_from_elements,
        "remove": remove_from_elements,
        "discard": discard_from_elements
    }
    for _ in range(number_of_commands):
        order = input().strip()
        if order == "pop":
            pop_from_elements(elements)
        else:
            command, item = order.split()
            decorator(commands.get(command), elements, int(item))
    print(sum(elements))


if __name__ == '__main__':
    run()
