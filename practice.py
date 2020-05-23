import tkinter
import time

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 800

N_RAWS = 8
N_COLMS = 10
SPACING = 5
BRICK_START_Y = 50
BRICK_HEIGHT = 20
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLMS+1) * SPACING) / N_COLMS
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 20


def main():

    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')  # calling canvas function

    bricks_list = []

    for raw in range(N_RAWS):  # to draw all raws
        for col in range(N_COLMS):  # to draw all columns
            bricks_list.append(draw_rectangle(canvas, raw, col))  # calling rect function

    ball = make_ball(canvas)
    paddle = canvas.create_rectangle(CANVAS_WIDTH/2 - PADDLE_WIDTH/2, CANVAS_HEIGHT - 40,
                                     (CANVAS_WIDTH/2 - PADDLE_WIDTH/2) + PADDLE_WIDTH,
                                     (CANVAS_HEIGHT - 40) + PADDLE_HEIGHT, fill='blue', outline='blue')

    change_x = 10
    change_y = 20

    while True:
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, PADDLE_Y)

        canvas.move(ball, change_x, change_y)

        if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
            change_y = change_y * -1

        if hit_right_wall(canvas, ball) or hit_left_wall(canvas, ball):
            change_x = change_x * -1

        if hit_paddle(canvas, ball, paddle):
            change_y = change_y * -1

        if hit_bricks(canvas, ball, bricks_list):
            change_y = change_y * -1

        canvas.update()
        time.sleep(1/17)
    #canvas.mainloop()

    
def draw_rectangle(canvas, raw, col):  # define function to create rectangle

    x1 = SPACING + (SPACING * col) + (BRICK_WIDTH * col)  # calculating x1 location, changes by col value changes
    y1 = BRICK_START_Y + (SPACING * raw) + (BRICK_HEIGHT * raw)  # calculating y1 location, changes by raw value changes
    x2 = x1 + BRICK_WIDTH
    y2 = y1 + BRICK_HEIGHT
    color = 'red'

    return canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)  # to draw rectangle at proper place


def make_ball(canvas):

    x1 = (CANVAS_WIDTH / 2) - (BALL_SIZE / 2)
    y1 = (CANVAS_HEIGHT / 2) - (BALL_SIZE / 2)
    return canvas.create_oval(x1, y1, x1 + BALL_SIZE, y1 + BALL_SIZE, fill='black')


def hit_bottom_wall(canvas, ball):  # you can put three turns with  this function later
    ball_top_y = get_top_y(canvas, ball)
    return ball_top_y > CANVAS_HEIGHT - BALL_SIZE


def hit_right_wall(canvas, ball):
    ball_left_x = get_left_x(canvas, ball)
    return ball_left_x > CANVAS_WIDTH - BALL_SIZE


def hit_top_wall(canvas, ball):
    ball_top_y = get_top_y(canvas, ball)
    return ball_top_y == 0


def hit_left_wall(canvas, ball):
    ball_left_x = get_left_x(canvas, ball)
    return ball_left_x == 0


def hit_paddle(canvas, ball, paddle):
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    y1 = ball_coords[1]
    x2 = ball_coords[2]
    y2 = ball_coords[3]

    colliding_list = canvas.find_overlapping(x1, y1, x2, y2)

    return len(colliding_list) > 1 and (colliding_list[0] == paddle or colliding_list[1] == paddle)


def hit_bricks(canvas, ball, bricks_list):
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    y1 = ball_coords[1]
    x2 = ball_coords[2]
    y2 = ball_coords[3]

    colliding_list = canvas.find_overlapping(x1, y1, x2, y2)

    brick_hit = False
    for collided_object in colliding_list:
        if collided_object in bricks_list:
            canvas.delete(collided_object)
            brick_hit = True

    return brick_hit


def get_left_x(canvas, obj):
    return canvas.coords(obj)[0]


def get_top_y(canvas, obj):
    return canvas.coords(obj)[1]


# don't modify below coding, done to create canvas
def make_canvas(width, height, title):  # define function to create canvas

    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
