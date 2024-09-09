import rclpy
import random
# Below would be used if arduino connected and trransmitting data over serial port
# import serial
from rclpy.node import Node

#import custom message
from custom_interfaces.msg import Food                            


class HitSensorPublisher(Node):

    def __init__(self):
        super().__init__('hit_sensor_publisher')
        self.publisher_ = self.create_publisher(Food, 'topic', 10)  
        timer_period = 0.5
        # Below line used if arduino attached
        # self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.time = 0

    def timer_callback(self):

        # The following code would be used if arduino was attached and 
        # live data was being published from the hit sensor connected to the arduino.
        
        #if self.serial_port.in_waiting :
            # self.i = self.serial_port.realine()decode(útf-8').rstrip()

        msg = Food()                                                
        msg.hit = self.i
        msg.timestamp = self.time                                           
        self.publisher_.publish(msg)

        #publish mock data
        self.get_logger().info('Hit: "%d", at time "%d' % (msg.hit, msg.timestamp))       
        
        #each call back, increase time by 1 and randomise whether the hit sensor has been hit
        self.time += 1
        self.i = random.randint(0,1)



def main(args=None):
    rclpy.init(args=args)

    hit_sensor_publisher = HitSensorPublisher()

    rclpy.spin(hit_sensor_publisher)

    hit_sensor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()