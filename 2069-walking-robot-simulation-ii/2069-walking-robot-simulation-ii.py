class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height

        self.x = 0
        self.y = 0
        self.d = 0

        # East, North, West, South
        self.dirs = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        self.names = ["East", "North", "West", "South"]

        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        num %= self.perimeter

        # Important:
        # a complete cycle returns to (0,0) facing South
        if num == 0:
            num = self.perimeter

        while num > 0:
            dx, dy = self.dirs[self.d]

            nx = self.x + dx
            ny = self.y + dy

            if 0 <= nx < self.w and 0 <= ny < self.h:
                self.x = nx
                self.y = ny
                num -= 1
            else:
                # Counterclockwise turn
                self.d = (self.d + 1) % 4

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.names[self.d]