import rclpy
from rclpy.node import Node

from custom_interfaces.msg import Food                        


class FoodDispenserSubscriber(Node):

    def __init__(self):
        super().__init__('food_dispenser_subscriber')
        self.subscription = self.create_subscription(
            Food,                                               
            'topic',
            self.listener_callback,
            10)
        self.subscription

        #initalise variables
        self.gap = 5
        self.lastfeed = 0

    def listener_callback(self, msg):
             
             
            # Logic for how the dispensing mechanism should be triggered based on what the subscriber has heard from the hit sensors published data
            # If the hit sensor has not been triggered, leave the dispenser closed.
            # If the hit sensor has been triggered and the dispenser hasn't been opened in a while (in this case, in over 5 time points), open the dispenser
            # If the hit sensor has been triggered but the bowl has recently been filled (within the last 5 time points), do not open the dispenser
             if msg.hit == 0 :
                self.get_logger().info('Dispenser Closed, no hit detected')  
             
             if msg.hit == 1 and self.gap < 5 :
                self.get_logger().info('Dispenser Closed, hit detected but you have had enough food. Last fed at "%d"' % (self.lastfeed))
            
             if msg.hit == 1 and self.gap >= 5 :
                self.get_logger().info('Dispenser Open, hit detected, last fed at "%d"' % (self.lastfeed))
                self.lastfeed = msg.timestamp
                self.gap = 0
             
             if self.lastfeed != 0 :
                self.gap = msg.timestamp - self.lastfeed

             
 
              



def main(args=None):
    rclpy.init(args=args)

    food_dispenser_subscriber = FoodDispenserSubscriber()

    rclpy.spin(food_dispenser_subscriber)

    food_dispenser_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()