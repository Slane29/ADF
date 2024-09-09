from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor_check',
            executable='service',
            name='service'),
        Node(
            package='sensor_check',
            executable='client',
            name='client',
            parameters = [{'sensor_number': 1}]),
  ])