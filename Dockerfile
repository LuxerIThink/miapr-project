FROM osrf/ros:humble-desktop

# Enviromental variables
ENV DEBIAN_FRONTEND=noninteractive
ENV WORKDIR=/usr/src/ros2_ws

WORKDIR $WORKDIR

# Copy apt-get required libraries list
COPY packages.txt .
RUN echo "Installing dependencies..." \
    && apt update -yq \
    && apt-get update -yq \
    && apt-get install -yq --no-install-recommends $(cat packages.txt) \
    && rm -rf /var/lib/apt/lists/*

# Copy python required libraries list
COPY requirements.txt .
RUN echo "Installing python libraries..." \
    && pip3 install --no-cache-dir -r requirements.txt

COPY user_files  .

# Source Ros
RUN echo ". install/setup.bash" >> ~/.bashrc \
    && bash -c "source ~/.bashrc" \
    && . /opt/ros/humble/setup.sh \
    && colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
    && bash -c "source /opt/ros/humble/setup.bash" \
    && bash -c "source install/local_setup.bash"

# Set settings
RUN touch /root/.Xauthority

# Set enviromental variables
ENV TURTLEBOT3_MODEL=waffle
ENV GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models



