#!/usr/bin/env python

import rospy
import sys
import random
import rospkg
import math
import tf
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

class Environment:
    small_static_target = '/models/target_small_static/model.sdf'
    small_moving_target = '/models/target_small_moving/model.sdf'
    large_target = '/models/target_large/model.sdf'
    target_bin = '/models/target_bin/model.sdf'

    def __init__(self, service_proxy, package_directory, min_x, min_y, max_x, max_y):
        self.service_proxy = service_proxy
        self.package_directory = package_directory
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.target_id = 0

    def spawn_small_static_targets(self, count):
        self.spawn_target(count, self.small_static_target)

    def spawn_small_moving_targets(self, count):
        self.spawn_target(count, self.small_moving_target)

    def spawn_large_targets(self, count):
        self.spawn_target(count, self.large_target)

    def spawn_target(self, count, model):
        initial_pose = Pose()
        sdf_model = open(self.package_directory + model, 'r').read()
        for i in range(0, count):
            initial_pose.position.x = random.uniform(self.min_x, self.max_x)
            initial_pose.position.y = random.uniform(self.min_y, self.max_y)
            quaternion = tf.transformations.quaternion_from_euler(0, 0, random.uniform(0, 2 * math.pi))
            initial_pose.orientation.x = quaternion[0]
            initial_pose.orientation.y = quaternion[1]
            initial_pose.orientation.z = quaternion[2]
            initial_pose.orientation.w = quaternion[3]
            self.service_proxy('target' + str(self.target_id), sdf_model, 'targets', initial_pose, 'world')
            self.target_id += 1

    def spawn_target_bin(self):
        initial_pose = Pose()
        initial_pose.position.x = -self.max_x + 7
        initial_pose.position.y = self.max_y - 7
        sdf_model = open(self.package_directory + self.target_bin, 'r').read()
        self.service_proxy('target_bin', sdf_model, 'targets', initial_pose, 'world')


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
    environment = Environment(service_proxy, package_directory, -x/2, -y/2, x/2, y/2)
    environment.spawn_small_static_targets(n1)
    environment.spawn_small_moving_targets(n2)
    environment.spawn_large_targets(n3)
    environment.spawn_target_bin()
    rospy.spin()
