#!/usr/bin/env python
## Nonesense publisher to avoid the robot driving infinitely when receiving intermittent manual commands

import rospy
from geometry_msgs.msg import Twist

def dummy_zero():
    pub = rospy.Publisher('dummy_zero', Twist, queue_size=10)
    rospy.init_node('dummy_zero', anonymous=True)

    msg = Twist()

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        dummy_zero()
    except rospy.ROSInterruptException:
        pass