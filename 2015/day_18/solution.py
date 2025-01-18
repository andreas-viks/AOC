from utils_anviks import parse_file_content, stopwatch, Grid, Cell

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', ''), str)


@stopwatch
def part1():
    grid = Grid(data)
    grid = grid.map(lambda _, val: val == '#')
    neighbour_cache = {cell: list(grid.neighbours(cell, 'all')) for cell, v in grid.items()}

    for _ in range(100):
        turn_on = []
        turn_off = []

        for cell, v in grid.items():
            on_neighbours = 0
            for nb in neighbour_cache[cell]:
                if grid[nb]:
                    on_neighbours += 1

            if v:
                if on_neighbours < 2 or on_neighbours > 3:
                    turn_off.append(cell)
            else:
                if on_neighbours == 3:
                    turn_on.append(cell)

        grid[turn_on] = True
        grid[turn_off] = False

    return len(list(grid.find(True)))


@stopwatch
def part2():
    grid = Grid(data)
    for _ in range(100):
        grid_copy = grid.copy()
        for cell, v in grid_copy.items():
            if cell in [Cell(0, 0), Cell(0, grid.width - 1),
                        Cell(grid.height - 1, 0), Cell(grid.height - 1, grid.width - 1)]:
                continue
            on_neighbours = 0
            for nb in grid_copy.neighbours(cell, 'all'):
                if grid_copy[nb] == '#':
                    on_neighbours += 1
            if v == '#':
                if on_neighbours < 2 or on_neighbours > 3:
                    grid[cell] = '.'
            else:  # '.'
                if on_neighbours == 3:
                    grid[cell] = '#'
    return len(list(grid.find('#')))


if __name__ == '__main__':
    print(part1())  # 768   | 5.86 seconds
    # print(part2())  # 781   | 15.20 seconds