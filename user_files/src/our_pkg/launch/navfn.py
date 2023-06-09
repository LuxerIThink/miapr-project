import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            IncludeLaunchDescription, SetEnvironmentVariable)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import PushRosNamespace
import launch_ros

def generate_launch_description():
    pkg_share = get_package_share_directory('our_pkg')
    nav_config_path = LaunchConfiguration('nav_params')
    rviz_config_path = LaunchConfiguration('rviz_path')
    map_path = LaunchConfiguration('map_path')
    bringup_dir = get_package_share_directory('nav2_bringup')
    gazebo_dir = get_package_share_directory('turtlebot3_gazebo')

    nav_yaml_params = DeclareLaunchArgument(
        'nav_params',
        default_value=os.path.join(pkg_share, 'params', 'navfn.yaml'),
        description='.yaml file for navigation config')

    rviz_path = DeclareLaunchArgument(
        'rviz_path',
        default_value=os.path.join(bringup_dir, 'rviz', 'nav2_default_view.rviz'),
        description='path for .rviz file')

    map_yaml_path = DeclareLaunchArgument(
        'map_path',
        default_value=os.path.join(pkg_share, "map", "turtlebot3_world.yaml"),
        description='path for map file')

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(bringup_dir, 'launch', 'bringup_launch.py')),
        launch_arguments={
                            "map": map_path,
                            "use_sim_time": "False",
                        "params_file": nav_config_path
                    }.items()
    )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gazebo_dir, 'launch', 'turtlebot3_world.launch.py'))
    )

    # dist = launch_ros.actions.Node(
    #     package='our_pkg',
    #     executable='dist.py',
    #     name='dist_node'
    # )

    rviz = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_path]
    )   

    ld = LaunchDescription()
    ld.add_action(nav_yaml_params)
    ld.add_action(map_yaml_path)
    ld.add_action(rviz_path)
    ld.add_action(nav2_launch)
    ld.add_action(gazebo_launch)
    # ld.add_action(dist)
    ld.add_action(rviz)
    return ld