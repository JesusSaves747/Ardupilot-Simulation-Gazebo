#!/usr/bin/env python

import rospy
import sys
import random
import rospkg
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

class Environment:
    small_target = '/models/target/model.sdf'

    def __init__(self, service_proxy, package_directory):
        self.service_proxy = service_proxy
        self.package_directory = package_directory

    def spawn_small_static_targets(self, count, min_x, min_y, max_x, max_y):
        initial_pose = Pose()
        sdf_model = open(self.package_directory + self.small_target, 'r').read()
        for i in range(0, count):
            initial_pose.position.x = random.uniform(min_x, max_x)
            initial_pose.position.y = random.uniform(min_y, max_y)
            self.service_proxy('target' + str(i), sdf_model, 'targets', initial_pose, 'world')

    # def spawn_small_moving_targets(self, count, min_x, min_y, max_x, max_y):

    # def spawn_large_targets(self, count, min_x, min_y, max_x, max_y):


if len(sys.argv) == 8:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    n1 = int(sys.argv[3])
    n2 = int(sys.argv[4])
    n3 = int(sys.argv[5])
    rospy.init_node('environment_manager_3')
    rospy.wait_for_service('gazebo/spawn_sdf_model')
    service_proxy = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
    package_directory = rospkg.RosPack().get_path('mbzirc_gazebo')
    environment = Environment(service_proxy, package_directory)
    environment.spawn_small_static_targets(n1, -x/2, -y/2, x/2, y/2)
    # environment.spawn_small_moving_targets(n2, -x/2, -y/2, x/2, y/2)
    # environment.spawn_large_targets(n3, -x/2, -y/2, x/2, y/2)
    rospy.spin()
