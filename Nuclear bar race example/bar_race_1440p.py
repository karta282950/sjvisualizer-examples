from sjvisualizer import DataHandler, Canvas, BarRace, StaticImage
import json

EXCEL_FILE = "data/Nuclear.xlsx"
FPS = 60
DURATION = 0.15

# reading the json file
with open("colors.json") as f:
    colors = json.load(f)

# load the data into a data frame
df = DataHandler.DataHandler(excel_file=EXCEL_FILE, number_of_frames=FPS*DURATION*60).df

# creating the canvas
canvas = Canvas.canvas()

# adding decoration with TkInter
line = canvas.canvas.create_line(800, 40, 800, 150, width=10, fill=Canvas._from_rgb((75, 75, 155)))

# adding the racing bar chart
bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas, colors=colors, width=2200, height=1000, x_pos=100)
canvas.add_sub_plot(bar_chart)

# adding a title
canvas.add_title("Nuclear Warheads by Country", color=(0,0,0))
canvas.add_sub_title("From 1950 - 2021", color=(150,150,150))

# adding a time
canvas.add_time(df=df, time_indicator="year")

# adding a logo
canvas.add_logo(logo="logo.png")

# adding a static image
ex = StaticImage.static_image(canvas=canvas.canvas, file="nuclear_explosion.png", x_pos = 650, y_pos=25, width=125, height=125)
canvas.add_sub_plot(ex)

# play the animation
canvas.play(fps=FPS)