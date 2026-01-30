from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    # 이동 방향: 상, 하, 좌, 우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    queue = deque()
    queue.append((0, 0))  # 시작 위치

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 맵 범위 안이고, 이동 가능(1)한 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1  # 거리 누적
                queue.append((nx, ny))

    # 도착 지점 확인
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
