FROM osrf/ros:humble-desktop

# Enviromental variables
ENV DEBIAN_FRONTEND=noninteractive
ENV WORKDIR=/usr/src/ros2_ws

WORKDIR $WORKDIR

# Copy apt-get required libraries list
COPY packages.txt .
RUN echo "Installing dependencies..." \
    && apt update -yq \
    && apt upgrade -y \
    && apt-get update -yq \
    && apt-get install -yq $(cat packages.txt) \
    && rm -rf /var/lib/apt/lists/*

# Copy python required libraries list
COPY requirements.txt .
RUN echo "Installing python libraries..." \
    && pip3 install -r requirements.txt

COPY user_files  .

# Source Ros
RUN echo ". install/setup.bash" >> ~/.bashrc \
    && bash -c "source ~/.bashrc" \
    && . /opt/ros/humble/setup.sh \
    # && bash -c "chmod +x /exec/dist.py" \
    && colcon build \
    && bash -c "source /opt/ros/humble/setup.bash" \
    && bash -c "source install/setup.bash" 
    # && bash -c "export TURTLEBOT3_MODEL=waffle" \
    # && bash -c "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models" 


    # && export GAZEBO_MODEL_DATABASE_URI="" 

ENV TURTLEBOT3_MODEL=waffle
ENV GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models

# Set settings
RUN touch /root/.Xauthority
