import tkinter

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 800

N_RAWS = 8
N_COLMS = 10
SPACING = 5
BRICK_START_Y = 50
BRICK_HEIGHT = 20
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLMS+1) * SPACING) / N_COLMS
BALL_SIZE = 40


def main():

    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')  # calling canvas function

    for raw in range(N_RAWS):  # to draw all raws
        for col in range(N_COLMS):  # to draw all columns
            draw_rectangle(canvas, raw, col)  # calling rect function
    canvas.mainloop()  # try to run program without mainloop and see what happens


def draw_rectangle(canvas, raw, col):  # define function to create rectangle

    x1 = SPACING + (SPACING * col) + (BRICK_WIDTH * col)  # calculating x1 location, changes by col value change
    y1 = BRICK_START_Y + (SPACING * raw) + (BRICK_HEIGHT * raw)  # calculating y1 location, changes by raw value change
    x2 = x1 + BRICK_WIDTH
    y2 = y1 + BRICK_HEIGHT
    color = 'red'

    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)  # to draw rectangle at proper place


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


