#!/bin/bash
xhost +local:root
docker run -it --rm\
        --name=miapr_project \
        --shm-size=1g \
	      --ipc=host \
        -e DISPLAY=$DISPLAY \
        -e XDG_RUNTIME_DIR=/tmp \
        -e QT_X11_NO_MITSHM=1 \
        -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /usr/bin/docker:/usr/bin/docker \
        --device=/dev/dri:/dev/dri \
        --device=/dev/video0 \
        --network=host \
        miapr_project \
        bash
