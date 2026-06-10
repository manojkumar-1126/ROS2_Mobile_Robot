from os.path import join
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():

    pkg_path = get_package_share_directory('my_robot_controller')

    
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name="robot_state_publisher",
        output='screen',
        parameters=[
            {'robot_description': Command( \
            ['xacro ', join(pkg_path, 'urdf/my_robot.urdf.xacro'), 
            ' sim_ign:=', "true"

            ])}],
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-name', 'turtle_bot',  # Entity name
            '-topic', '/robot_description',
            '-x', '0', 
            '-y', '0', 
            '-z', '1.0' 
        ]
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        output='screen',    
        arguments=[
            "/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist",
            "/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock",
            "/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry",
            "/tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V",
            "/scan@sensor_msgs/msg/LaserScan[ignition.msgs.LaserScan",
            "/world/default/model/turtle_bot/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model"
        ],
        remappings=[
        
            ("/world/default/model/turtle_bot/joint_state", "/joint_states")
        ]
    )

    return LaunchDescription([
        robot_state_publisher,
        bridge,     # Connects ROS 2 to GZ
        spawn_robot
        
    ])