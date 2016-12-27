#!/usr/bin/env python
# license removed for brevity
import rospy as rp
from std_msgs.msg import String
from  mavros_msgs.msg import PositionTarget
from geometry_msgs.msg import PoseStamped
import sys

def setPosLocal():

    rp.init_node('setPosLocal')
    pub = rp.Publisher('/savio/Pose', PoseStamped, queue_size=10)

    rate = rp.Rate(10) # 10hz

    pose = PoseStamped()

    pose.pose.position.x=float(sys.argv[1])
    pose.pose.position.y=float(sys.argv[2])
    pose.pose.position.z=float(sys.argv[3])


    while not rp.is_shutdown():

        rp.loginfo(pose)
        pub.publish(pose)
        rate.sleep()



if __name__ == '__main__':
    try:
        setPosLocal()
    except rp.ROSInterruptException:
        pass
