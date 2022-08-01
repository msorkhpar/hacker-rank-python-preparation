import statistics


def run():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(f'{statistics.mean(student_marks[query_name]):.2f}')


if __name__ == '__main__':
    run()
