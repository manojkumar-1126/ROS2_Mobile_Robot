from os.path import join
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import AppendEnvironmentVariable, TimerAction

def generate_launch_description():

    pkg_path = get_package_share_directory('my_robot_controller')
    world_path = join(pkg_path, "worlds", "simple_world.sdf")
    
    gz_sim_share = get_package_share_directory("ros_gz_sim")

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(join(gz_sim_share, "launch", "gz_sim.launch.py")),
        launch_arguments={"gz_args" : "-r " + world_path}.items()
    )

    spawn_turtle_bot_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(join(pkg_path, "launch" , "turtle_bot.launch.py"))
    )

    return LaunchDescription([
    
    AppendEnvironmentVariable(
    name='IGN_GAZEBO_RESOURCE_PATH',
    value=join(pkg_path, "worlds")),
    
        gz_sim,
    ])