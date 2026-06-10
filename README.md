# Turtle_bot : Autonomous Obstacle Avoidance & SLAM Pipeline
[Screencast from 06-10-2026 08:37:18 AM.webm](https://github.com/user-attachments/assets/72e5fa92-98f5-4998-a1f8-129dee78c287)

## Humble + Ignition + Rviz2 (Ubuntu 22.04)

We built an autonomous robot that can explore a space on its own without bumping into walls while drawing a 2D map of the room as it moves.

### Core Feature Pipeline

* **The Brain (ROS 2 Humble):** Runs our custom code that acts like a smart driver. If an obstacle gets within 1.2 meters, it tells the robot to stop completely, look around for open space, and turn cleanly without any shaky movements.
* **The Eyes & World (Ignition Gazebo):** A 3D virtual simulation world where our robot lives, drives around, and uses a laser scanner (LiDAR) to measure distances to walls and objects.
* **The Mapmaker (SLAM Toolbox):** Takes the laser scans and converts them into a live, detailed 2D blueprint grid of the environment.
* **The Dashboard (RViz2):** Our visual screen that shows us exactly what the robot is thinking, where it has driven (tracking its distance route), and the map it is building in real-time.

### Build the workspace

'''bash
cd ~/ros2_ws
rm -rf build/ install/ log/
colcon build --packages-select my_robot_controller
source install/setup.bash

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
