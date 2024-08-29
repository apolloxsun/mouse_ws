tried to use docker but could not run both scripts in simultanuously on the same display. 

build with:
sudo docker build -it image_name

run with:
sudo docker run -it -e DISPLAY=$DISPLAY --net=host  -v ${PWD}:/home/ros_user/mouse_ws image_name

