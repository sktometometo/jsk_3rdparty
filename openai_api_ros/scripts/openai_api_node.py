#!/usr/bin/env python

import rospy
from openai_api_ros.openai_api_interface import OpenAIAPIInterface


if __name__ == '__main__':

    rospy.init_node('openai_api_ros')
    api_key = rospy.get_param('~api_key')
    node = OpenAIAPIInterface(api_key=api_key)
    rospy.spin()
