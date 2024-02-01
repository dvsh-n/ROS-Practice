#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_name(data):
    rospy.loginfo(rospy.get_caller_id()+ " I heard %s", data.data)

def callback_count(data):
    rospy.loginfo(rospy.get_caller_id()+ " I heard %s", data.data)

def subscriber_name():

    rospy.init_node('subscriber_name')
    rospy.Subscriber('HW1/name', String, callback_name)
    rospy.Subscriber('HW1/count', String, callback_count)
    rospy.spin()

if __name__ == '__main__':
    subscriber_name()
