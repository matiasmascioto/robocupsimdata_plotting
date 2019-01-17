"""
Plotting Spatiotemporal soccer data from RoboCupSimData
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import re
import yaml


config = yaml.safe_load(open("robocupsimdata_plotting_animation.yml", encoding="utf-8"))


def create_pitch(ax, len_x=105, len_y=68, penalty_area_width=16.5, penalty_area_length=40, six_yard_box_width=5.5,
                six_yard_box_length=9):
    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, len_y], color="black")
    plt.plot([0, len_x], [len_y, len_y], color="black")
    plt.plot([len_x, len_x], [len_y, 0], color="black")
    plt.plot([len_x, 0], [0, 0], color="black")
    plt.plot([len_x/2, len_x/2], [0, len_y], color="black")

    # Left Penalty Area
    plt.plot([penalty_area_width, penalty_area_width], [len_x/2, (len_y/2) - (penalty_area_length/2)], color="black")
    plt.plot([0, penalty_area_width], [len_x/2, len_x/2], color="black")
    plt.plot([penalty_area_width, 0], [(len_y/2) - (penalty_area_length/2), (len_y/2) - (penalty_area_length/2)], color="black")

    # Right Penalty Area
    plt.plot([len_x, len_x - penalty_area_width], [len_x/2, len_x/2], color="black")
    plt.plot([len_x - penalty_area_width, len_x - penalty_area_width], [len_x/2, (len_y/2) - (penalty_area_length/2)], color="black")
    plt.plot([len_x - penalty_area_width, len_x], [(len_y/2) - (penalty_area_length/2), (len_y/2) - (penalty_area_length/2)], color="black")

    # Left 6-yard Box
    plt.plot([0, six_yard_box_width], [(len_y/2) + six_yard_box_length, (len_y/2) + six_yard_box_length], color="black")
    plt.plot([six_yard_box_width, six_yard_box_width], [(len_y/2) + six_yard_box_length, (len_y/2) - six_yard_box_length], color="black")
    plt.plot([six_yard_box_width, 0], [(len_y/2) - six_yard_box_length, (len_y/2) - six_yard_box_length], color="black")

    # Right 6-yard Box
    plt.plot([len_x, len_x - six_yard_box_width], [(len_y/2) + six_yard_box_length, (len_y/2) + six_yard_box_length], color="black")
    plt.plot([len_x - six_yard_box_width, len_x - six_yard_box_width], [(len_y/2) + six_yard_box_length, (len_y/2) - six_yard_box_length], color="black")
    plt.plot([len_x - six_yard_box_width, len_x], [(len_y/2) - six_yard_box_length, (len_y/2) - six_yard_box_length], color="black")

    # Prepare Circles
    centreCircle = plt.Circle((len_x/2, len_y/2), 9.15, color="black", fill=False)
    centreSpot = plt.Circle((len_x/2, len_y/2), 0.5, color="black")
    leftPenSpot = plt.Circle((11, len_y/2), 0.5, color="black")
    rightPenSpot = plt.Circle((len_x - 11, len_y/2), 0.5, color="black")

    # Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    # Tidy Axes
    plt.axis('off')


def init():
    create_pitch(ax)
    team_L.set_data([], [])
    team_R.set_data([], [])
    ball.set_data([], [])


def animate(i, df):
    actual_row = df.iloc[i]
    time = actual_row["time"]
    score_L = actual_row["score_L"]
    score_R = actual_row["score_R"]
    playmode = actual_row["playmode"]
    ax.set_title("Time {time}\n{score_L} L - {score_R} R - {playmode}".format(time=time, score_L=score_L,
                                                                             score_R=score_R, playmode=playmode))

    team_L.set_data(df.iloc[i][team_L_pos_x_columns].values, df.iloc[i][team_L_pos_y_columns].values)
    team_R.set_data(df.iloc[i][team_R_pos_x_columns].values, df.iloc[i][team_R_pos_y_columns].values)
    ball.set_data(df.iloc[i]["ball_pos_x"], df.iloc[i]["ball_pos_y"])


# Load data
df = pd.read_csv(**config["input"])

# Create figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

team_L, = ax.plot([], [], **config["team_L_style"])
team_R, = ax.plot([], [], **config["team_R_style"])
ball, = ax.plot([], [], **config["ball_style"])


# Columns with positional data for each team
team_L_pos_x_columns = [c for c in df.columns if re.search("L_[0-9]{2}_pos_x", c) is not None]
team_L_pos_y_columns = [c for c in df.columns if re.search("L_[0-9]{2}_pos_y", c) is not None]
team_R_pos_x_columns = [c for c in df.columns if re.search("R_[0-9]{2}_pos_x", c) is not None]
team_R_pos_y_columns = [c for c in df.columns if re.search("R_[0-9]{2}_pos_y", c) is not None]


time_frames = range(config["initial_time"], config["final_time"])
anim = FuncAnimation(fig, animate, init_func=init, interval=config["interval_ms"], frames=time_frames, repeat=True,
                     fargs=(df,))

if config["output"]["export_video"]:
    anim.save(config["output"]["filepath"]) # Plays the whole video to save it


# Display Pitch
plt.draw()
plt.show()




