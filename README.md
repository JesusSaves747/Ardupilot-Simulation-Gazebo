# MBZIRC Workspace

This repository contains all the ROS source code developed for the [MBZIRC](http://www.mbzirc.com).

#### Maintainers:
[Murat Ambarkutuk](https://github.com/eroniki)

[Mickey Cowden](https://github.com/mickey13)

[Savio Pereira](https://github.com/JesusSaves747)

## Installation Instructions:

    # Add this to your .bashrc file
    export GAZEBO_MODEL_PATH=<absolute_path_to_cmsvt_mbzirc_project>/src/mbzirc_gazebo/models

## Build Worlds

    rosrun xacro xacro --inorder src/mbzirc_gazebo/worlds/mbzirc_arena.world.xacro > src/mbzirc_gazebo/worlds/mbzirc_arena.world

    rosrun xacro xacro --inorder src/mbzirc_gazebo/worlds/kentland_farm.world.xacro > src/mbzirc_gazebo/worlds/kentland_farm.world
