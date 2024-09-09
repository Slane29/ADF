from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='record_doggo',
            executable='talker',
            name='talker'),
        Node(
            package='record_doggo',
            executable='listener',
            name='listener'),
  ])