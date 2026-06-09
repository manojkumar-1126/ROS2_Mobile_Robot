from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', 'my_robot_controller', 'launch'), glob('launch/*')),

        (os.path.join('share', 'my_robot_controller', 'urdf'), glob('urdf/*')),

        (os.path.join('share', 'my_robot_controller', 'worlds'), glob('worlds/*')),

        (os.path.join('share', 'my_robot_controller', 'meshes'), glob('meshes/*')),
    ],
    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='manoj',
    maintainer_email='manoj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "star_loop=my_robot_controller.star_loop:main",
            "star_builder=my_robot_controller.star_drawer:main",
            "custom_pub=my_robot_controller.custom_publisher:main",
            "custom_sub=my_robot_controller.custom_subscriber:main",
            'client_node = my_robot_controller.custom_client:main',
            'server_node = my_robot_controller.custom_server:main',
            'obstacle_runner = my_robot_controller.obstacle_avd:main',
            'smart_mover = my_robot_controller.custom_odom:main',
            'turtle_bot_node = my_robot_controller.turtle_bot:main',
        ],
    },
)
