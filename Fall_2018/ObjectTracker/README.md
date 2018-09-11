# Real-Time Object Tracker

Author: Kris Nguyen
[GitHub](https://github.com/KrisNguyen135)
[LinkedIn](https://www.linkedin.com/in/quan-m-nguyen/)
[Kaggle](https://www.kaggle.com/quannguyen135)

## Intro
Computer vision is an exciting, ever-growing field in computer science, and data
science specifically. With the development of powerful memory and processors,
real-time computer vision applications are becoming more and more popular.

Object detection and tracking in particular can provide significant useful
applications: vehicle tracking is used in self-driving cars so that autonomous
engines are able to effectively avoid collisions; movement tracking is used for
security purposes to identify unauthorized activities in off-limit areas;
tracking players in sports can be implemented for automatic foul detection.

In this project we will be building a real-time object tracking engine that
dynamically tracks objects in a computer webcam video and other video feeds.
The program allows its users to highlight a specific region in a video feed by
dragging the computer cursor. It then detects the particular object inside that
region, draws a rectangle around the object in the processed output video, and
finally tracks it throughout the whole video by moving the tracking rectangle
following the target.

Sample end result:

[![](http://img.youtube.com/vi/mZrJs-YWlc0/0.jpg)](http://www.youtube.com/watch?v=mZrJs-YWlc0)

## Installation
This section will walk you through the process of installing the necessary tool
for this project, namely Python and OpenCV.

Go to the [homepage of Anaconda](https://www.anaconda.com/download/#macos) and
download the distribution for your specific operating system. Be sure to check the "Add to path" option
while running the installer.

Open your command line and type in the following commands:

`conda create -n myenv python=3.6` (creating a virtual environment with Python 3.6)

`source activate myenv` (activating the virtual environment)

`conda install anaconda-client` (installing Anaconda-Client interface)

`conda install opencv=3.4 -c conda-forge` (installing OpenCV version 3.4 from
the `conda-forge` channel)

`pip install imutils` (installing the `imutils` package)

After entering these commands and waiting for each of them to finish executing,
you should have all the dependencies you need to start the project!
