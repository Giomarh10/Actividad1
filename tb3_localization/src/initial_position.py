#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def Posicion_Inicial(xpose, ypose, zpose):
    InitialPosition=PoseWithCovarianceStamped()
    InitialPosition.pose.x=xpose
    InitialPosition.pose.y=ypose
    InitialPosition.pose.z=zpose

    loop_rate=rospy.Rate(20)
    initialpose_topic='/initialpose'
    initialpose_publisher=rospy.Publisher(initialpose_topic,PoseWithCovarianceStamped,queue_size=1)
    initialpose_publisher.publish(InitialPosition)
    loop_rate.sleep()

if __name__ == "__main__":

    try:
        rospy.init_node('rotate_node',anonymous=True)

        Posicion_Inicial(2,2,2)
        
    except rospy.ROSInterruptException:
        rospy.loginfo("node finished")