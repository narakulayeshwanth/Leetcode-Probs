class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        # Find the closest point of the rectangle to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Check if that point lies inside/on the circle
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        return dx * dx + dy * dy <= radius * radius