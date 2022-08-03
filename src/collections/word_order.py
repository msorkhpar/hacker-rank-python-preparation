def run():
    words = []
    word_catalog = dict()
    for _ in range(int(input())):
        word = input().strip()
        words.append(word)
        word_frequency = word_catalog.get(word, 0)
        word_catalog[word] = word_frequency + 1

    print(len(word_catalog))

    printed_cache = set()
    for word in words:
        if word not in printed_cache:
            print(word_catalog.get(word), end=" ")
            printed_cache.add(word)


if __name__ == '__main__':
    run()
