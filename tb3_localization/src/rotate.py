#!/usr/bin/env python
import math 
import time
import rospy
from geometry_msgs.msg import Twist


x=0
y=0
yaw=0


def rotate(angular_speed_degree, relative_angle_degree, clockwise):
    global yaw
    velocity_message= Twist()
    velocity_message.linear.x=0
    velocity_message.linear.y=0
    velocity_message.linear.z=0
    velocity_message.angular.x=0
    velocity_message.angular.y=0
    velocity_message.angular.z=0

    #theta0= yaw
    angular_speed = math.radians(abs(angular_speed_degree))

    if(clockwise):
        velocity_message.angular.z= -abs(angular_speed)
    else:
        velocity_message.angular.z= abs(angular_speed)
    
    #angle_moved=0.0
    loop_rate=rospy.Rate(20)
    cmd_vel_topic='/cmd_vel'
    velocity_publisher=rospy.Publisher(cmd_vel_topic,Twist,queue_size=1)

    t0 = rospy.Time.now().to_sec()

    while True:
        rospy.loginfo("Turtlebot3 rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()

        if(current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break
    
    velocity_message.angular.z=0
    velocity_publisher.publish(velocity_message)



if __name__ == "__main__":

    try:
        rospy.init_node('rotate_node',anonymous=True)

        rotate(30,90,False)
        time.sleep(1)
        rotate(30,90,True)
        time.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("node finished")
