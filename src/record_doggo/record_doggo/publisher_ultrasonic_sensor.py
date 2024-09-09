import rclpy
import random
from rclpy.node import Node

#import custom message
from custom_interfaces.msg import Ultrasonic                            


class UltrasonicSensorPublisher(Node):

    def __init__(self):
        super().__init__('ultrasonic_sensor_publisher')
        self.publisher_ = self.create_publisher(Ultrasonic, 'topic', 10)  
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 30
        self.counter = 0

    def timer_callback(self):
        msg = Ultrasonic()                                                
        msg.ultrasonic_distance = self.i                                           
        self.publisher_.publish(msg)

        if self.counter > 4 and self.counter < 15:
            # Doggo appears between time 5 and 15, make distance short during this time to trigger video recording of dog
            self.i = 3
        
        if self.counter >= 15 :
            self.i = 30

        #publish mock data
        self.get_logger().info('Distance: "%d" at time "%d"' % (msg.ultrasonic_distance, self.counter))       
        
        
            
        #each call back, increase time by 1
        self.counter += 1



def main(args=None):
    rclpy.init(args=args)

    ultrasonic_sensor_publisher = UltrasonicSensorPublisher()

    rclpy.spin(ultrasonic_sensor_publisher)

    ultrasonic_sensor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()