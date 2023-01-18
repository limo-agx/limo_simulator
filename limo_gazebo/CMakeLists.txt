cmake_minimum_required(VERSION 3.0.2)
project(limo_gazebo)

find_package(catkin REQUIRED COMPONENTS)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES limo_gazebo
#  CATKIN_DEPENDS gazebo_plugins gazebo_ros gazebo_ros_control limo_control limo_description
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
