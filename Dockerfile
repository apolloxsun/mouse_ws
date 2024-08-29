FROM ros:noetic-ros-base

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]
ENV shell=/bin/bash

# Install dependencies and Raylib
RUN apt-get update && apt-get install -y \
    sudo \
    build-essential \
    python3-pip \
    python3-catkin-tools \
    libasound2-dev\
    libx11-dev\
    libxrandr-dev\
    libxi-dev\
    libglu1-mesa-dev\
    libglfw3-dev \
    libxext-dev \
    libxrender-dev \
    libxtst-dev \
    libgl1-mesa-dev \
    libxcursor-dev\
    libxinerama-dev\
    libwayland-dev \
    wayland-protocols \
    libxkbcommon-dev \
    freeglut3-dev \
    libglew-dev \
    g++ \
    x11-apps \
    mesa-utils \
    cmake \
    git \
    xorg \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pyautogui

ENV DISPLAY=:0
ENV XDG_RUNTIME_DIR=/run/user/1000  
# Assuming the UID of the user is 1000, adjust if different

# Clone Raylib repository
RUN git clone https://github.com/raysan5/raylib.git /raylib

# Build Raylib
WORKDIR /raylib
RUN mkdir build && cd build && \
    cmake .. && \
    make && \
    make install

# Verify Raylib installation (optional)
RUN ls /usr/local/lib | grep raylib
RUN ls /usr/local/include | grep raylib

# Create and configure user
ARG UID=1000
RUN useradd -m -s /bin/bash ros_user && \
    echo 'ros_user:ros' | chpasswd && \
    adduser ros_user sudo && \
    adduser ros_user dialout && \
    echo "ros_user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set up workspace and permissions
WORKDIR /home/ros_user/mouse_ws
RUN chown -R ros_user:ros_user /home/ros_user/mouse_ws

USER ros_user

# Build catkin workspace
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc 

VOLUME /tmp/.X11-unix:/tmp/.X11-unix

# Default command
CMD ["bash"] 
