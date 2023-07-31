# point is an (x, y) tuple
"""def function(parameter): #point is a parameter
    match parameter:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
function((0,3))"""

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y =y
def where_is(point):
    match point:
        case Point(x = 0, y = 0): #or u can just writet Point(0,0)
            print("origin")

where_is(Point(0,0))