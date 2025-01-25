from utils_anviks import stopwatch

row, column = 2978, 3083


@stopwatch
def part1():
    n = sum(range(column + 1))
    for i in range(row - 1):
        n += column + i
    code = 20151125
    for _ in range(n - 1):
        code = code * 252533 % 33554393
    return code


if __name__ == '__main__':
    print(part1())  # 2650453   | 1.30 seconds
