#import custom srv
from custom_interfaces.srv import Check                                                           

import rclpy
from rclpy.node import Node


class CheckSensorService(Node):

    def __init__(self):
        super().__init__('check_sensor_service')
        self.srv = self.create_service(Check, 'check_sensors', self.check_callback)       

    def check_callback(self, request, response):

        # Here is where code would go to test if the sensor that corresponds to the number given by request.sensor_number is online

        #Input dummy response that particular sensor is online
        response.status = 1 
        # Print that the request has been received                                                 
        self.get_logger().info('Incoming request\nis sensor number %d online?' % (request.sensor_number))  

        return response

def main(args=None):
    rclpy.init(args=args)

    check_sensor_service = CheckSensorService()

    rclpy.spin(check_sensor_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()