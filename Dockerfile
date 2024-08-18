FROM ros:noetic-ros-base

ENV ROS_DISTRO=noetic
ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-pip \
    python3-catkin-tools \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
    opencv-python \
    numpy \
    pyautogui 

WORKDIR /home/mouse_ws

RUN mkdir -p src && cd src\
    catkin_init_workspace

COPY src/ ./src/

RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && catkin_make"

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc

ENTRYPOINT ["/bin/bash"]
   