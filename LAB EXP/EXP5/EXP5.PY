
from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()
        m, c, boat = state

        if state == goal:
            for step in path + [state]:
                print(step)
            return

        for dm, dc in moves:
            if boat == 1:
                nm, nc = m - dm, c - dc
                nb = 0
            else:
                nm, nc = m + dm, c + dc
                nb = 1

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            rm, rc = 3 - nm, 3 - nc

            if (nm > 0 and nm < nc) or (rm > 0 and rm < rc):
                continue

            new = (nm, nc, nb)

            if new not in visited:
                visited.add(new)
                q.append((new, path + [state]))

    print("No solution")

solve()
