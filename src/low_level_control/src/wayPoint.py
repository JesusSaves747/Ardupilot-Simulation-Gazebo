#!/usr/bin/env python
# license removed for brevity
import rospy as rp
from std_msgs.msg import String
from  mavros_msgs.msg import PositionTarget
from geometry_msgs.msg import Twist,Vector3,TwistStamped

def talker():

    rp.init_node('VelCmd')
    pub = rp.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)

    rate = rp.Rate(10) # 10hz

    while not rp.is_shutdown():
        #hello_str = "hello world %s" % rp.get_time()
        #
        velCmd= sendVelCmd()

        rp.loginfo(velCmd)
        pub.publish(velCmd)
        rate.sleep()

def sendVelCmd():

    # Define the target waypoint in Local NED frame here:
    vel = TwistStamped(header=rp.Header())

    vel.twist = Twist(Vector3(0,0,2),Vector3(0,0,0))

    # Type: mavros_msgs
    #wp.header = "Random Text"
    #wp.coordinate_frame = 1
    #wp.type_mask = 64
    #wp.position =p

    return vel

if __name__ == '__main__':
    try:
        talker()
    except rp.ROSInterruptException:
        pass
