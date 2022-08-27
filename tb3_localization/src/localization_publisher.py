#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def poseCallback(pose_message):
    print("x:"+str(pose_message.position.x))
    print("y:"+str(pose_message.position.y))
    print("z:"+str(pose_message.position.z))

if __name__ == "__main__":

  rospy.init_node('localization_publisher')
  rate = rospy.Rate(5) # 5 Hz
  position_topic="/initialpose"
  
  for count in range(1,6):
    pose_subscriber=rospy.Subscriber(position_topic,String,poseCallback)
    
    rate.sleep()