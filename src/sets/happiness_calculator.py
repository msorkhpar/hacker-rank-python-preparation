def run():
    n, m = input().split()
    arr = list(map(int, input().split()))
    like_set = set(map(int, input().split()))
    dislike_set = set(map(int, input().split()))
    happiness_score = 0
    for item in arr:
        if item in like_set and item not in dislike_set:
            happiness_score += 1
        elif item in dislike_set:
            happiness_score -= 1
    print(happiness_score)


if __name__ == '__main__':
    run()
