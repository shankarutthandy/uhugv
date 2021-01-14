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
<img src="./images/uhugv.gif" height="500" width="700">

## Underwater simulation:

```
$ roslaunch uhugv uw.launch 
```
<img src="./images/uw.png" height="500" width="700">

### Topics:

<img src="./images/topics.png" height="700" width="800">