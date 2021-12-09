import math
import turtle


def draw_triangle(t, length, pos, color):
    """
    Draws inverted triangle in position pos
    @param t: turtle object
    @param length: int, length to go forward
    @param pos: tuple, position in xy plane
    @param color: str, color of triangle
    @return: None, draws the inverted triangle
    """
    t.penup()
    t.goto(pos)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.right(120)
    t.end_fill()


def recursive_triangle(t, length, depth, color):
    """
    Recursively defines positions to draw Sierpinski's triangle
    @param t: turtle object
    @param length: int, length to go forward
    @param depth: int, how many cycles of Sierpinski's triangle
    @param color: str, color of triangle
    @return: None, draws the Sierpinski triangles
    """
    '''
    Idea: on each cycle we get 3 new points
    (namely, the start point itself + (upper left vertix + lower vertix) of newly drawn Sierpinski triangle ),
    from with with the distance [pos[0] + length / 4, pos[1] + length * math.sin(math.pi / 3) / 2]
    a new inverted Sierpinski triangle is drawn.
    Yes, I did spend too much time in order to figure this out.
    '''
    pos_ls = [[0, 0]]
    points_ls = []
    for i in range(depth):
        for point in points_ls:
            pos_ls.append([point[0] + length, point[1]])  # The lower point of Sierpinski triangle
            pos_ls.append([point[0] + length * 0.5, point[1] + length * math.sin(math.pi / 3)])  # the upper point
        for pos in pos_ls:
            points_ls.append(pos)
            pos = [pos[0] + length / 4, pos[1] + length * math.sin(math.pi / 3) / 2]  # the start point
            draw_triangle(t, length / 2, tuple(pos), color)  # Drawing triangle
        length /= 2


def draw_sierpinski_triangle(length, depth, color_background, color_inner):
    """
    Draws Sierpinski's triangle
    @param length: int, length to go forward
    @param depth: int, how many cycles of Sierpinski's triangle
    @param color_background: str, color of background triangle
    @param color_inner: str, color of Sierpinski's triangle
    @return: None, draws the Sierpinski triangles
    """
    screen = turtle.Screen()  # Getting screen, canvas
    t = turtle.Turtle(visible=False)  # Don't want to see the cursor (default visible = True)
    screen.tracer(False)  # Direct image, no animation
    # Drawing the background big triangle
    t.fillcolor(color_background)
    t.begin_fill()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()
    # Drawing the inner triangles
    recursive_triangle(t, length, depth, color_inner)
    t.hideturtle()
    screen.tracer(True)
    # Enable the code below exitonclick() if you want to save the image instead of seeing it
    screen.exitonclick()  # Exits the image only if you click on it
    # ts = turtle.getscreen()
    # ts.getcanvas().postscript(file="sierpinski_triangle.eps")


if __name__ == "__main__":
    draw_sierpinski_triangle(length=300, depth=5, color_background="purple", color_inner="orange")
