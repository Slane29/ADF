import rclpy
from rclpy.node import Node

from custom_interfaces.msg import Water                        # CHANGE


class WaterDispenserSubscriber(Node):

    def __init__(self):
        super().__init__('water_dispenser_subscriber')
        self.subscription = self.create_subscription(
            Water,                                               # CHANGE
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
             
             # If the count direction is 1, this means that the water has been filled and is currently being depleted by the dog drinking.
             # Keep the dispenser closed until the water level reaches a low enough level (in this case 3)
             if msg.count_direction == 1 and msg.water_level >= 3 :
                self.get_logger().info('Dispenser Closed, water level is "%d"' % msg.water_level)  # CHANGE
            
             # If the count direction is 0, that means it has reached the low level.
             # Open the water dispenser until the water level has reached 15.
             if msg.water_level <=15 and msg.count_direction == 0 :
                self.get_logger().info('Dispenser Open, water level is "%d"' % msg.water_level)

             # If the count direction is 0 but the water level has reached 15, keep the dispenser closed
             # This is to simulate that even if the water level reaches above the nominated height (say if the dog sticks his snout in the water), 
             # the water dispenser should remain closed. The water dispenser will only open if it has reached a low level.
             if msg.water_level > 15 and msg.count_direction == 0 :
                self.get_logger().info('Dispenser Closed, water level is "%d"' % msg.water_level)

              



def main(args=None):
    rclpy.init(args=args)

    water_dispenser_subscriber = WaterDispenserSubscriber()

    rclpy.spin(water_dispenser_subscriber)

    water_dispenser_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()