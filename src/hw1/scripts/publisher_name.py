#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher_name():
    """Fill here """

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub_str = """ Fill here  """
        """Fill here"""
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_name()
    except rospy.ROSInterruptException:
        pass
