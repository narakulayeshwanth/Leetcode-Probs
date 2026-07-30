from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # North

        x = y = 0
        ans = 0

        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx = x + dx
                    ny = y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans