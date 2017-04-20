# Ardupilot Gazebo Simulation Repository

This repository contains all the source code for simulating an Ardupilot Controller in Gazebo

#### Maintainers:


[Savio Pereira](https://github.com/JesusSaves747)



## Installation Instructions:

    # Clone dependent repositories
    wstool update -t src

    # Add this to your .bashrc file
    export GAZEBO_MODEL_PATH=<absolute_path_to_Ardupilot_Simualtion_repo>/src/mbzirc_gazebo/models


## Building the sitl_gazebo package:

# Set the plugin path so Gazebo finds our model and sim
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:<absolute_path_to_Ardupilot_Simualtion_repo>/src/sitl_gazebo/Build

# Set the model path so Gazebo finds the airframes
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:<absolute_path_to_Ardupilot_Simualtion_repo>/src/sitl_gazebo/models

# Disable online model lookup since this is quite experimental and unstable
export GAZEBO_MODEL_DATABASE_URI=""

# Set path to sitl_gazebo repository
export SITL_GAZEBO_PATH=<absolute_path_to_Ardupilot_Simualtion_repo>/src/sitl_gazebo

## Make a build directory in the sitl_gazebo package and then run cmake (make sure to add the two dots in front of cmake)
cd <absolute_path_to_Ardupilot_Simualtion_repo>/src/sitl_gazebo
mkdir Build
cd Build
cmake ..

## Autogenerate the sdf file with the command
make sdf

## Now build the gazebo plugins by typing:
make

## Building the px4/Firmware package:
cd <absolute_path_to_Ardupilot_Simualtion_repo>/src/Firmware
make posix_sitl_default gazebo
