#import custom srv
from custom_interfaces.srv import Check                           
import sys
import rclpy
from rclpy.node import Node


class SensorCheckClientAsync(Node):

    def __init__(self):
        super().__init__('sensor_check_client_async')
        self.cli = self.create_client(Check, 'check_sensors')       
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Check.Request()                                   

    def send_request(self):
        self.req.sensor_number = int(sys.argv[1])
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    sensor_check_client = SensorCheckClientAsync()
    sensor_check_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(sensor_check_client)
        if sensor_check_client.future.done():
            try:
                response = sensor_check_client.future.result()
            except Exception as e:
                sensor_check_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                # Logic for what happens upon response from sensor checking service.
                # If the service has responded that the nominated sensor is online, print this statement (always the case with this dummy data)
                # If the service has responded that the nominated sensor is offline, print this statement
                if response.status == 1 :
                    sensor_check_client.get_logger().info('Result of sensor check: for sensor number %d, sensor is online' %  (sensor_check_client.req.sensor_number))                              # CHANGE
                
                else :
                    sensor_check_client.get_logger().info('Result of sensor check: for sensor number %d, sensor is offline' % (sensor_check_client.req.sensor_number))
            break

    sensor_check_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()