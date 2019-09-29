#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
    msg = String()
    i = 0
    while not rospy.is_shutdown():
        string = "%s" % i
        i += 2
        rospy.loginfo(string)

        msg.data = string
        pub.publish(msg)

        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')




