# README


## Getting Started
In order to run this code, it is assumed that you already have docker and git installed. If not, please install them now.

## 1 Setting up the Docker Container
Firstly, you will need to create a new docker container with an image of ROS 2 Iron.

### 1.1 Pull docker image
Run the following command to pull the ROS 2 iron docker image:

```sh
docker pull osrf/ros:iron-desktop
```

### 1.2 Start up the Docker contianer
Run the following command in order to start the docker container for the first time. This will start a container with a name of your choice using the image of ROS 2 iron that you just pulled.

```sh
Docker run --name <your_container_name> -it osrf/ros:iron-desktop
```

### 1.2.1 Entering the Docker container again
If you would like to enter this docker container again in a new terminal window or after closing the window, run the following command. This is the command you will use to enter the docker container from here on.

```sh
Docker exec -it <your_container_name> bash
```

## 2 Configuring the  environment

### 2.1 Source ROS 2 setup files
Once you have entered the container, you will need to source the setup files by running the following command.
```sh
source /opt/ros/iron/setup.bash
```
You will need to source in every new window that you open. However, please run the following command so that this will happen automatically.
```sh
echo "source /opt/ros/iron/setup.bash" >> ~/.bashrc
```

### 2.2 Making the ROS 2 workspace
To create a workspace to clone the code from github to, please use the following command.
```sh
mkdir root/ros2_ws
cd root/ros2_ws
```

## 3 Clone code from github
Please use the following command to clone the git repo. Make sure you are in your workspace when running this command.
```sh
git clone https://github.com/Slane29/ADF.git
```

Please enter the ADF folder now with the following command.
```sh
cd ADF
```


## 4 Running the Code
The following sections will describe what commands you will need to use to run the various publisher/subscriber and service/client nodes for the automatic dog feeder system. It will also describe briefly what the expected output should be. The publisher/subscriber nodes are run using launch files and thus can be run in one window. The service/client nodes however will need to be run in two separate windows.

### 4.1 Building and sourcing the workspace
In order to run the ros workspace, you will need to build it with the following command. Make sure that you are in your workspace file path (ros2_ws) not the source folder (ros2_ws/src).
```sh
colcon build
```

Open a new window and start the docker container using the instructions listed above (section 1.2.1). It is best practice to source the setup files and run the nodes in a separate terminal to the one you use to build the workspace in. For the following sections, you will use this new window. Please run the following command to enter the workspace.
```sh
cd /root/ros2_ws/ADF
```

Please run the following command to source the setup files. 

```sh
source setup/install.bash
```

### 4.2 Running the Water Level Publisher/Subscriber Nodes
To run the Water Level nodes, please run the following command.

```sh
ros2 launch water_level water_level_launch.py
```
You should see the publisher and subscriber outputs in one window, with each publisher output preceding the subscriber output. The water level package should publish the water level, starting at 20 and dropping to 3, before counting back up to 20. This will run in a loop. The water level subscriber should state that the dispenser is closed when the water is depleting to 3, the water dispenser is open once the level reaches 3, and that the dispenser closes once more after reaching the water level 15. This too should run in a loop. Use ctrl + C to quit at any time.

### 4.3 Running the Food Level Publisher/Subscriber Nodes
To run the Food Level nodes, please run the following command.

```sh
ros2 launch food_level food_level_launch.py
```
You should see the publisher and subscriber outputs in one window, with each publisher output preceding the subscriber output. The food level package should publish whether the hit sensor has been triggered (this is randomised) along with a timestamp (that increases by one each time). The food level subscriber should state that the dispenser is closed when no hit is detected, and should state that the dispenser is open when a hit is detected and it has not been opened in more than 5 time intervals. If a hit is detected by the dispenser was opened within the last 5 time intervals, the subscriber will state that a hit has been detected but the dog has received enough food.


### 4.4 Running the Record Doggo Publisher/Subscriber Nodes
To run the Record Doggo nodes, please run the following command.

```sh
ros2 launch record_doggo record_doggo_launch.py
```
You should see the publisher and subscriber outputs in one window, with each publisher output preceding the subscriber output. The record doggo package should publish mock data of the ultrasonic sensor. The publisher is designed to publish mock data by publishing a distance of 30 for the first 5 time intervals, before the dog hypothetically arrives and it begins publishing a distance of 3. The dog hypothetically leaves at time 15, after which the publisher will publish a distance of 30 again continuously. The subscriber will show that video is being recorded when it receives data from the publisher that indicates the dog is at the feeder.

### 4.5 Running the Sensor Check Service/Client Nodes
The Sensor Check is designed to check whether the sensors are working or not. This is a service/client relationship and will need to be run in two different windows. Please open a new terminal and enter the container following the instructions listed in section 1.3, and source the setup files as described in section 4.1.

In the first window, run the following command to start up the service. This means that the service is ready and waiting for a client request.

```sh
ros2 run sensor_check server
```

In the second window, run the following command to send a request from the client to the server. You can enter any number in <arg> to check that number sensor in the system.

```sh
ros2 run sensor_check client <arg>
```

After sending the client request:
- You should see the statement "Incoming request is sensor <arg> online?" in the window where you ran the service.
- You should see the response "Result of sensor check: for sensor number <arg>, sensor is online"in the window where you ran the client.





