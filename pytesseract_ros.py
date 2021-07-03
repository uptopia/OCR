#!/usr/bin/python
# -*- coding: UTF-8 -*-
# roscore

# cd ~/realsense_ws
# . devel/setup.bash
# roslaunch realsense2_camera rs_camera.launch

# rostopic list

# cd ~/Documents/learn_ros/src/beginner_tutorials/src
# python aruco_ros.py

# written by Shang-Wen, Wong
# 2021.3.22

import rospy
from sensor_msgs.msg import Image as msg_Image

import cv2
# from cv_bridge import CvBridge, CvBridgeError
from cv_bridge.boost.cv_bridge_boost import getCvType

import numpy as np

import pytesseract

def imageOCR(data):
    bridge = CvBridge()
    try:
        img = bridge.imgmsg_to_cv2(data, data.encoding)
    except CvBridgeError as e:
        print(e)
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # OCR (Optical Character Recognition)
    img_h , img_w, _ = np.array(img).shape
    decode2 = pytesseract.image_to_boxes(img)
    print('decode2\n', decode2)

    #==================#
    # 標示文字及文字位置
    #==================#
    ### 使用pytesseract.image_to_boxes資訊
    ### (letter, x1, y1, x2, y2, ?)
    info_array = decode2.split(None) #separate by "blank"

    idx = int(np.size(info_array)/6)

    for i in range(idx):
        cnt = i*6

        letter = info_array[cnt]
        x1 = int(info_array[cnt + 1])
        y1 = img_h - int(info_array[cnt + 2])
        x2 = int(info_array[cnt + 3])
        y2 = img_h - int(info_array[cnt + 4])
        center_x = int((x1 + x2)/2)
        center_y = int((y1 + y2)/2)

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(img, letter, (center_x, center_y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow('cv_image', cv_image)
    cv2.waitKey(1)

if __name__ == '__main__':
    
    rospy.init_node("product_OCR")

    #============#
    # Subscriber  
    #============#    
    sub_marker = rospy.Subscriber('/camera/color/image_raw', msg_Image, imageOCR)

 
    # #============#
    # # Service  
    # #============#
    # top3_cloud_pub = nh.advertise<sensor_msgs::PointCloud2> ("/top3_cloud_pub", 1);
    # target_sauce_center_pub = nh.advertise<sensor_msgs::PointCloud2> ("/target_sauce_center_pub", 1);
    # ros::ServiceServer service = nh.advertiseService("/get_highest_sauce", response_highest);

    rospy.spin()