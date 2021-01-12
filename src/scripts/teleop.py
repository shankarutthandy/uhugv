#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys
import tty
import termios

rospy.init_node('teleop_node',anonymous=True)
pub=rospy.Publisher('/track/cmd_vel',Twist,queue_size=10)
file_desc=sys.stdin.fileno()
old=termios.tcgetattr(file_desc)
tty.setraw(sys.stdin)
v=Twist()
while not rospy.is_shutdown():
    char=sys.stdin.read(1)
    if char=='w':
        v.linear.x=5.0
        pub.publish(v)
        rospy.sleep(0.015)
    elif char=='s':
        v.linear.x=-5.0
        pub.publish(v)
        rospy.sleep(0.015)
    elif char=='a':
        v.angular.z=3.0
        pub.publish(v)
        rospy.sleep(0.015)
    elif char=='d':
        v.angular.z=-3.0
        pub.publish(v)
        rospy.sleep(0.015)
    v.angular.z=0
    v.linear.x=0
    pub.publish(v)
    
termios.tcsetattr(file_desc,termios.TCSADRAIN,old)