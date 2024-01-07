"""
Module: hurricane_tracker

Program to visualize the path of a Hurrican in the North Atlantic Basin.

Authors:
1) Will Dobrzanski - wdobrzanski@sandiego.edu
2) Jared Gutierrez - jaredgutierrez@sandiego.edu
"""
import turtle


def screen_setup():
    """
    Creates the Turtle and the Screen with the map background
    and coordinate system set to match latitude and longitude.

    Returns:
    A list containing the turtle, the screen, and the background image.

    DO NOT MODIFY THIS FUNCTION IN ANY WAY!!!
    """

    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()

    # set the coordinate system to match lat/long
    turtle.setworldcoordinates(-90, 0, -17.66, 45)

    map_bg_img = tkinter.PhotoImage(file="atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricane.gif")
    t.shape("hurricane.gif")

    return [t, wn, map_bg_img]


# Define the get_category function here
def get_category(windSpeed):
    """Get category from a certain windspeed

    Parameters: the wind speed

    Returns: the category"""
    if windSpeed > 156:
        return 5
    elif windSpeed > 130:
        return 4
    elif windSpeed > 111:
        return 3
    elif windSpeed > 96:
        return 2
    elif windSpeed > 74:
        return 1
    else:
        return 0

def animate(csv_filename):
    """
    Animates the path of a hurricane.

    Parameters:
    csv_filename (string): Name of file containing hurricane data (CSV format).
    """

    # screen_setup returns a list of three items: the turtle to draw with, the
    # screen object for the window, and the background image of the window.
    # We only care about the turtle though.
    setup_data = screen_setup()

    # Give a name to the turtle that we were given back.
    hurricane_turtle = setup_data[0]


    # Your code to perform the animation will go after this line.
    h = open(csv_filename, "r")
    hurricane_turtle.penup()
    hurricane_turtle.hideturtle()
    for vals in h:
        vals = vals.split(",")
        c = get_category(int(vals[4]))
        hurricane_turtle.pensize(c + 1)
        if c == 5:
            hurricane_turtle.pencolor("red")
        elif c == 4:
            hurricane_turtle.pencolor("orange")
        elif c == 3:
            hurricane_turtle.pencolor("yellow")
        elif c == 2:
            hurricane_turtle.pencolor("green")
        elif c == 1:
            hurricane_turtle.pencolor("blue")
        else:
            hurricane_turtle.pencolor("white")
        hurricane_turtle.goto(float(vals[3]), float(vals[2]))
        hurricane_turtle.showturtle()
        hurricane_turtle.pendown()
        if c > 0:
            hurricane_turtle.write(c)
    h.close

    # DO NOT MODIFY THE FOLLOWING LINE! (It make sure the turtle window stays
    # open).
    turtle.done()


# Do not modify anything after this point.
if __name__ == "__main__":
    filename = input("Enter the name of the hurricane data file: ")
    animate(filename)
