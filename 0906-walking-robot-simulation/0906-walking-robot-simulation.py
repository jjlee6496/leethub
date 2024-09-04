class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ind = 0
        x, y = 0, 0
        obstacles = set(map(tuple, obstacles))
        res = 0

        for cmd in commands:
            if cmd == -1:
                ind = (ind + 1) % 4
            elif cmd == -2:
                ind = (ind - 1 + 4) % 4
            else:
                dx, dy = directions[ind]
                for _ in range(cmd):
                    if (x + dx, y + dy) not in obstacles:
                        x += dx
                        y += dy
                        res = max(res, x**2 + y**2)
        return res