cmake_minimum_required(VERSION 3.0.2)
project(mouse)

add_compile_options(-std=c++11)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

find_package(raylib REQUIRED)
# Add these lines to your CMakeLists.txt file

find_package(Threads REQUIRED)


include_directories(${CMAKE_SOURCE_DIR}/include)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES mouse
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)



add_executable(random src/randombutton.cpp)
target_include_directories(random PRIVATE ${XFIXES_INCLUDE_DIRS} )
target_link_libraries(random raylib m dl pthread ${CMAKE_THREAD_LIBS_INIT}) 


