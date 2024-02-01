#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher_count():

    rospy.init_node('publisher_count')
    pub = rospy.Publisher('HW1/count', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    count = 0

    while not rospy.is_shutdown():
        pub_str = "The current count is " + str(count)
        rospy.loginfo(pub_str)
        pub.publish(pub_str)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_count()
    except rospy.ROSInterruptException:
        pass
