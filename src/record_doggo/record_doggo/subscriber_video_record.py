#Following imports are for using opencv to record from usb cam
# import cv2
# import os
# from matplotlib import pyplot as plt


import rclpy
from rclpy.node import Node

from custom_interfaces.msg import Ultrasonic                        


class VideoRecordSubscriber(Node):

    def __init__(self):
        super().__init__('video_record_subscriber')
        self.subscription = self.create_subscription(
            Ultrasonic,                                               
            'topic',
            self.listener_callback,
            10)
        self.subscription


    def listener_callback(self, msg):
             
             if msg.ultrasonic_distance < 10 :
                 # Record when object within 10 centimetres of ultrasonic sensor

                 # Example code for recording from usb cam
                 # Connect to webcam when doggo is detected as close
                 # cap = cv2.VideoCapture(0)  # Assuming usb cam is connected to 0, would need to check
                 # 
                 # Get some key values from webcam
                 # frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                 # frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                 # frameRate = int(cap.get(cv2.CAP_PROP_FPS))
                 #
                 # Specify viedo properties
                 # fourccCode=cv2.VideoWriter_fourcc(*'MJPG')
                 # 
                 # Specify file name
                 # videoFileName= os.path.join('data', 'recordedVideo.mp4')  # define file path for saved video
                 # 
                 # define the recorded video dimensions
                 # videoDimension=(frameWidth, frameHeight)
                 # 
                 # Create VideoWriter
                 # recordedVideo = cv2.VideoWriter(videoFileName, fourccCode, frameRate, videoDimension)

                 # Print statement that recording is in progress
                 self.get_logger().info('RECORDING IN PROGRESS...')  

             # while cap.isOpened():
                    # ret, frame = cap.read()

                    #show image
                    # cv2.imshow('Webcam', frame)
                    # record video
                    # recordedVideo.write(frame)

                    #Check if doggo has moved away and stop recording if so
                    # if msg.ultrasonic_distance >= 10 :
                         #break     
             # recordedVideo.release()
             # cap.realese()
             # cv2.destroyAllWindows

                  



def main(args=None):
    rclpy.init(args=args)

    video_record_subscriber = VideoRecordSubscriber()

    rclpy.spin(video_record_subscriber)

    video_record_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()