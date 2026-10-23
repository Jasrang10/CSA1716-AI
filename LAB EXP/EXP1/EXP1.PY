
from heapq import heappush, heappop

def heuristic(state):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])

def solve(start):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            for step in path + [state]:
                print(step[:3])
                print(step[3:6])
                print(step[6:])
                print()
            return

        z = state.index(0)
        for move in [-3, 3, -1, 1]:
            nz = z + move

            if nz < 0 or nz > 8:
                continue
            if move == -1 and z % 3 == 0:
                continue
            if move == 1 and z % 3 == 2:
                continue

            new = list(state)
            new[z], new[nz] = new[nz], new[z]
            new = tuple(new)

            if new not in visited:
                heappush(pq, (g + 1 + heuristic(new),
                              g + 1, new, path + [state]))

    print("No solution found")

start = tuple(map(int, input("Enter 9 numbers (use 0 for blank): ").split()))
solve(start)
