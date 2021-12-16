from heapq import heappop, heappush

# file = 'test15.txt'
file = 'input15.txt'

with open(file) as f:
    M = [[int(l) for l in line.strip()] for line in f.readlines()]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def neighbour(pos):
    r, c = pos
    n_row = [r + row for row in dr]
    n_col = [c + col for col in dc]
    n = list(zip(n_row, n_col))
    return n


def scale_map(some_array, multiplier):
    R = len(some_array)
    C = len(some_array[0])
    new_R = R * multiplier
    new_C = C * multiplier
    new_array = [[0] * new_C for row in range(new_R)]
    for r in range(new_R):
        for c in range(new_C):
            new_array[r][c] = (some_array[r % R][c % C] + c // C + r // R) % 9
            if new_array[r][c] == 0:
                new_array[r][c] = 9
    return new_array


def find_path(arr):
    ROWS = len(arr)
    COLS = len(arr[0])
    visited = set()
    queue = [(0, (0, 0))]  # this is a list of tuples that contains information on the distance of point (x,y) from the source
    end = (ROWS - 1, COLS - 1)
    while queue:
        risk, pos = heappop(queue)  # removes and returns the lowest value from the list of queue tuples (sorted from first value in that tuple)
        if pos == end:
            return risk
        if pos in visited:
            continue
        visited.add(pos)
        for r, c in neighbour(pos):
            if 0 <= r < ROWS and 0 <= c < COLS:
                heappush(queue, (risk + arr[r][c], (r, c)))


new_M = scale_map(M, 5)

print(f'part1: {find_path(M)}')
print(f'part2: {find_path(new_M)}')
