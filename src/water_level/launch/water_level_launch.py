from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='water_level',
            executable='talker',
            name='talker'),
        Node(
            package='water_level',
            executable='listener',
            name='listener'),
  ])