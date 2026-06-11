# ROS2_Mobile_Robot : Autonomous Obstacle Avoidance & SLAM Pipeline
[Screencast from 06-11-2026 07:47:50 PM.webm](https://github.com/user-attachments/assets/956ff788-0d4e-4f78-a94b-fcbcde6ebd12)

## Humble + Ignition + Rviz2 (Ubuntu 22.04)

We built an autonomous robot that can explore a space on its own without bumping into walls while drawing a 2D map of the room as it moves.

### Core Feature Pipeline

* **The Brain (ROS 2 Humble):** Runs our custom code that acts like a smart driver. When it senses a wall or obstacle ahead, it tells the robot to stop completely, look around for an open path, and turn cleanly.
* **The Eyes & World (Ignition Gazebo):** A 3D virtual simulation world where our robot lives, drives around, and uses a laser scanner (LiDAR) to measure distances to walls and objects.
* **The Mapmaker (SLAM Toolbox):** Takes the laser scans and converts them into a live, detailed 2D blueprint grid of the environment.
* **The Dashboard (RViz2):** Our visual screen that shows us exactly what the robot is thinking, where it has driven (tracking its distance route), and the map it is building in real-time.

### Build the workspace

```bash
colcon build --packages-select my_robot_controller
source install/setup.bash
```
### Execution Sequence

#### Run each command in a separate terminal tab:

* **Terminal 1 (Simulation Environment):**

```bash
ros2 launch my_robot_controller gazebo.launch.py
```
* **Terminal 2 (SLAM Mapping):**

```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_robot_controller/config/mapper_params_online_async.yaml use_sim_time:=true
```
* **Terminal 3 (Collision Avoidance Node):**

```bash
ros2 run my_robot_controller turtle_bot_node
```
* **Terminal 4 (RViz 2 Visualization):**

```bash
ros2 run rviz2 rviz2 --ros-args -p use_sim_time:=true
```
## Conclusion

This project proves that a robot can successfully think for itself, safely avoid walls, and create a 2D map inside a 3D world all at the same time using ROS2 Humble.
