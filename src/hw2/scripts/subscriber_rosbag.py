#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


class Subscriber():

    def __init__(self):
        # Defin the subscriber and initialize the node along with the necessary commmand to keep the node running 
        # Make sure that the topic corresponds to the image topic of the rosbag
        rospy.Subscriber('/camera/depth/image_raw', Image, self.raw_callback)
        self.raw_count = 1
        rospy.Subscriber('/camera/rgb/image_color', Image, self.color_callback)
        self.color_count = 1
        self.bridge = CvBridge()

    def raw_callback(self, msg):
        try:
           # Read in the images in cv2 format from topic using bridge imgmsg_to_cv2 function
           cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
           self.raw_count += 1
        except CvBridgeError as e:
            print(e)
        else:
            # write cv2 image in a local file 'camera_image{COUNT}.jpeg' 
            # Start the COUNT from 1 and increment it as you iterate through the images
            path = '~/catkin_ws/src/hw2/images_raw/'
            name = "camera_image{}".format(self.raw_count)
            cv2.imwrite(path+name, cv_image)    

    def color_callback(self, msg):
        try:
           # Read in the images in cv2 format from topic using bridge imgmsg_to_cv2 function
           cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
           self.color_count += 1
        except CvBridgeError as e:
            print(e)
        else:
            # write cv2 image in a local file 'camera_image{COUNT}.jpeg' 
            # Start the COUNT from 1 and increment it as you iterate through the images
            path = '~/catkin_ws/src/hw2/images_color/'
            name = "camera_image{}".format(self.color_count)
            cv2.imwrite(path+name, cv_image)  
            
if __name__ == '__main__':
    try:
        node = Subscriber()
    except rospy.ROSInterruptException:
        pass
