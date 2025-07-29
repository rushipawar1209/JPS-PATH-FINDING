import math, heapq


def blocked(cX, cY, dX, dY, matrix):
    if cX + dX < 0 or cX + dX >= matrix.shape[0]:
        return True
    if cY + dY < 0 or cY + dY >= matrix.shape[1]:
        return True
    if dX != 0 and dY != 0:
        if matrix[cX + dX][cY] == 1 and matrix[cX][cY + dY] == 1:
            return True
        if matrix[cX + dX][cY + dY] == 1:
            return True
    else:
        if dX != 0:
            if matrix[cX + dX][cY] == 1:
                return True
        else:
            if matrix[cX][cY + dY] == 1:
                return True
    return False


def heuristic(a, b):
    # Euclidean distance heuristic
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def method(matrix, start, goal):
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}

    pqueue = []

    heapq.heappush(pqueue, (fscore[start], start))

    while pqueue:
        current = heapq.heappop(pqueue)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return the path in correct order

        close_set.add(current)

        for dX, dY in [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]:

            if blocked(current[0], current[1], dX, dY, matrix):
                continue

            neighbour = current[0] + dX, current[1] + dY

            tentative_g_score = gscore[current] + (math.sqrt(2) if dX != 0 and dY != 0 else 1)

            if neighbour in close_set:
                continue

            if tentative_g_score < gscore.get(neighbour, float('inf')):
                came_from[neighbour] = current
                gscore[neighbour] = tentative_g_score
                fscore[neighbour] = tentative_g_score + heuristic(neighbour, goal)
                heapq.heappush(pqueue, (fscore[neighbour], neighbour))

    return None  # Return empty list if no path found
