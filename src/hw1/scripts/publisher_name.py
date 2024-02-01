#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher_name():

    rospy.init_node('publisher_name')
    pub = rospy.Publisher('HW1/name', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        pub_str = "Hello Devesh"
        rospy.loginfo(pub_str)
        pub.publish(pub_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_name()
    except rospy.ROSInterruptException:
        pass
