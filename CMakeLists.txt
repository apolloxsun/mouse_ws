cmake_minimum_required(VERSION 3.22)

project(mouse_ws)
add_compile_options(-std=c++11)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(raylib REQUIRED)

include_directories(${CMAKE_SOURCE_DIR}/include)

add_executable(random src/randombutton.cpp)
target_link_libraries(random ${X11_LIBRARIES} ${XFIXES_LIBRARIES})
target_include_directories(random PRIVATE ${XFIXES_INCLUDE_DIRS} )
target_link_libraries(random raylib)

