# Unmanned Hybrid Underwater Ground Vehicle

ROS-MELODIC package to simulate tracked underwater hybrid vehicle in gazebo-9

## Getting Started

Clone this repo and build it in your catkin-workspace

```
$ cd <catkin-workspace>/src
$ git clone https://github.com/shankarutthandy/uhugv.git
$ cd ..
$ catkin_make
$ source devel/setup.bash
```
## tracked vehicle simulation :

```
$ roslaunch uhugv tracks.launch 
```
>or with keyboard-teleop:
```
$ roslaunch uhugv tracks.launch teleop:=true
```
<img src="./images/tracks.png" height="500" width="800">

## Underwater simulation:

```
$ roslaunch uhugv uw.launch 
```
<img src="./images/uw.gif" height="500" width="800">

