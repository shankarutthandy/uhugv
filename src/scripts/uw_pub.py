#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import numpy as np

class JointPub:
    def __init__(self):
        rospy.init_node('servo_cmd',anonymous=True)
        self.joints=[]
        self.joint_cmd={}
        self.t=0
        for i in range(1,5):
            self.joints.append('servoL'+str(i))
        for i in range(1,5):
            self.joints.append('servoR'+str(i))

    def update(self,dt):
        self.t+=dt
        amp=np.pi*0.5
        for i,j in enumerate(self.joints):
            self.joint_cmd[j]=amp*np.sin(self.t*5+i)

    def pubs(self):
        pub={}
        for j in self.joints:
            pub[j]=rospy.Publisher('/track'+'/'+j+'_position_controller'+'/command',Float64,queue_size=100)
        while not rospy.is_shutdown():
            self.update(dt=0.01)
            for j in self.joints:
                pub[j].publish(self.joint_cmd[j])
            rospy.sleep(0.01)

if __name__=='__main__':
    j=JointPub()
    j.pubs()