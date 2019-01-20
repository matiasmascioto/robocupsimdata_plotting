# RoboCupSimData (Plotting)
## Plotting *spatiotemporal* soccer data

*keywords: python, jupyter notebook, pandas, matplotlib, soccer, robocup, robocupsimdata, spatiotemporal*

This project works with spatiotemporal soccer data. The dataset used is from RoboCupSimData project ([Paper](https://arxiv.org/pdf/1711.01703.pdf)) ([Files Overview](http://oliver.obst.eu/data/RoboCupSimData/overview.html)). 

![Initial positions](data/output/initial_positions.png?raw=true "Initial positions")
![Match video!](data/output/video.gif?raw=true "Match video!")

## Project files
*  *robocupsimdata_cleaning.ipynb*: Cleans the original dataset
*  *robocupsimdata_plotting.ipynb*: Static plots
*  *robocupsimdata_plotting_animation.py*: Animated plots (videos)
*  *robocupsimdata_plotting_animation.yml*: Configuration file for *robocupsimdata_plotting_animation.py*

## Data
*  */data/input/groundtruth.csv*:  CSV file from RoboCupSimData project ([Paper](https://arxiv.org/pdf/1711.01703.pdf)) ([Files Overview](http://oliver.obst.eu/data/RoboCupSimData/overview.html)). In this project, we used a *groundtruth* file from an example game between Gliders2016 and HELIOS2016, winner and runner up of RoboCup 2016. This file recorded for each time point the play mode (e.g. kickoff), the current ball position coordinates and its velocity. Furthermore, the positions and velocities of each player of the left (L) and the right (R) team including the goalkeeper (G) is stated.
*  */data/output/groundtruth_cleaned.csv*: Dataset cleaned 
* */data/output/soccer_pitch.png*: Soccer pitch
* */data/output/initial_positions.png*: Soccer pitch with initial ball and player positions
* */data/output/trajectories.png*: Soccer pitch with ball and goalkeeper trajectory 
*  */data/output/video.mp4*: Match video!
*  */data/output/video.gif*: Match video converted to .gif

## Sources
  * [RoboCupSimData Files Overview](http://oliver.obst.eu/data/RoboCupSimData/overview.html)
  * [FC Python: Drawing a Pitchmap – Adding Lines & Circles in Matplotlib](https://fcpython.com/visualisation/drawing-pitchmap-adding-lines-circles-matplotlib)
  * [xyFootyPy](https://github.com/znstrider/xyFootyPy)