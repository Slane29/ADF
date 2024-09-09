import rclpy
from rclpy.node import Node

from custom_interfaces.msg import Water                            # CHANGE


class WaterSensorPublisher(Node):

    def __init__(self):
        super().__init__('water_sensor_publisher')
        self.publisher_ = self.create_publisher(Water, 'topic', 10)  # CHANGE
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 20
        self.flag = 1

    def timer_callback(self):
        msg = Water()                                                # CHANGE
        msg.water_level = self.i
        msg.count_direction = self.flag                                           # CHANGE
        self.publisher_.publish(msg)
        self.get_logger().info('Water Level: "%d", direction "%d' % (msg.water_level, msg.count_direction))       # CHANGE
        
        # Dummy data is a simple counter that counts down from 20 to 3 and then back up to 20, continuously. 
        # This is to simulate the water level going down and then being filled back up.

        if self.i == 20 :
            self.flag = 1
        
        if self.i <= 20 and self.flag == 1:
            self.i -= 1
        
        if self.i == 2 :
            self.flag = 0

        if self.i >=2 and self.flag == 0:
            self.i +=1




def main(args=None):
    rclpy.init(args=args)

    water_sensor_publisher = WaterSensorPublisher()

    rclpy.spin(water_sensor_publisher)

    water_sensor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()