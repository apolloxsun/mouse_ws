# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ros_user/mouse_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ros_user/mouse_ws/build

# Include any dependencies generated for this target.
include mouse/CMakeFiles/random.dir/depend.make

# Include the progress variables for this target.
include mouse/CMakeFiles/random.dir/progress.make

# Include the compile flags for this target's objects.
include mouse/CMakeFiles/random.dir/flags.make

mouse/CMakeFiles/random.dir/src/randombutton.cpp.o: mouse/CMakeFiles/random.dir/flags.make
mouse/CMakeFiles/random.dir/src/randombutton.cpp.o: /home/ros_user/mouse_ws/src/mouse/src/randombutton.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ros_user/mouse_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object mouse/CMakeFiles/random.dir/src/randombutton.cpp.o"
	cd /home/ros_user/mouse_ws/build/mouse && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/random.dir/src/randombutton.cpp.o -c /home/ros_user/mouse_ws/src/mouse/src/randombutton.cpp

mouse/CMakeFiles/random.dir/src/randombutton.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/random.dir/src/randombutton.cpp.i"
	cd /home/ros_user/mouse_ws/build/mouse && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ros_user/mouse_ws/src/mouse/src/randombutton.cpp > CMakeFiles/random.dir/src/randombutton.cpp.i

mouse/CMakeFiles/random.dir/src/randombutton.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/random.dir/src/randombutton.cpp.s"
	cd /home/ros_user/mouse_ws/build/mouse && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ros_user/mouse_ws/src/mouse/src/randombutton.cpp -o CMakeFiles/random.dir/src/randombutton.cpp.s

# Object files for target random
random_OBJECTS = \
"CMakeFiles/random.dir/src/randombutton.cpp.o"

# External object files for target random
random_EXTERNAL_OBJECTS =

/home/ros_user/mouse_ws/devel/lib/mouse/random: mouse/CMakeFiles/random.dir/src/randombutton.cpp.o
/home/ros_user/mouse_ws/devel/lib/mouse/random: mouse/CMakeFiles/random.dir/build.make
/home/ros_user/mouse_ws/devel/lib/mouse/random: /usr/local/lib/libraylib.a
/home/ros_user/mouse_ws/devel/lib/mouse/random: mouse/CMakeFiles/random.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ros_user/mouse_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/ros_user/mouse_ws/devel/lib/mouse/random"
	cd /home/ros_user/mouse_ws/build/mouse && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/random.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
mouse/CMakeFiles/random.dir/build: /home/ros_user/mouse_ws/devel/lib/mouse/random

.PHONY : mouse/CMakeFiles/random.dir/build

mouse/CMakeFiles/random.dir/clean:
	cd /home/ros_user/mouse_ws/build/mouse && $(CMAKE_COMMAND) -P CMakeFiles/random.dir/cmake_clean.cmake
.PHONY : mouse/CMakeFiles/random.dir/clean

mouse/CMakeFiles/random.dir/depend:
	cd /home/ros_user/mouse_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ros_user/mouse_ws/src /home/ros_user/mouse_ws/src/mouse /home/ros_user/mouse_ws/build /home/ros_user/mouse_ws/build/mouse /home/ros_user/mouse_ws/build/mouse/CMakeFiles/random.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : mouse/CMakeFiles/random.dir/depend

