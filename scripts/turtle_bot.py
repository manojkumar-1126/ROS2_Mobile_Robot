import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import LaserScan #for obstacle detection 
from geometry_msgs.msg import Twist #for turning momentum
from nav_msgs.msg import Odometry #distance tracking of bot
import math

class Turtlebot(Node):
    def __init__(self):
        super().__init__('turtle_bot_node')

        self.pub=self.create_publisher(Twist,'/cmd_vel',10)
        self.laser_sub=self.create_subscription(LaserScan,'/scan',self.scan_cb,10)
        self.odom_sub=self.create_subscription(Odometry,'/odom',self.odom_cb,10)

        #distance tracking variables
        self.total_dist = 0.0
        self.previous_x = None
        self.previous_y = None

        self.safety_limit = 1.2 # meters
        self.linear_speed = 0.5 # m/s

        self.get_logger().info(f'turtle bot with odometry initialized')

    def odom_cb(self,msg):

         current_x = msg.pose.pose.position.x
         current_y = msg.pose.pose.position.y

         if self.previous_x is None or self.previous_y is None :
             self.previous_x = current_x
             self.previous_y = current_y
             return
         
         dist_step = math.sqrt((current_x-self.previous_x)**2 + (current_y-self.previous_y)**2)

         self.total_dist+=dist_step

         self.previous_x = current_x
         self.previous_y = current_y

    def scan_cb(self,msg):
        
        # ---------------- FRONT ----------------

        front_ranges = msg.ranges[165:195]

        front_ranges = [
            x for x in front_ranges
            if not math.isinf(x) and not math.isnan(x)
        ]

        # ---------------- LEFT ----------------

        left_ranges = msg.ranges[255:285]

        left_ranges = [
            x for x in left_ranges
            if not math.isinf(x) and not math.isnan(x)
        ]

        # ---------------- RIGHT ----------------

        right_ranges = msg.ranges[75:105]

        right_ranges = [
            x for x in right_ranges
            if not math.isinf(x) and not math.isnan(x)
        ]

        # Safe defaults

        front_dist = min(front_ranges) if front_ranges else 10.0
        left_dist = min(left_ranges) if left_ranges else 10.0
        right_dist = min(right_ranges) if right_ranges else 10.0

        # Debug info

        self.get_logger().info(
            f"Front: {front_dist:.2f} | "
            f"Left: {left_dist:.2f} | "
            f"Right: {right_dist:.2f}"
        )

        move_cmd = Twist()

        deg = 30
        rad = deg*math.pi/180  # m/s

        # Front is clear -> Move Forward
        if front_dist > self.safety_limit:
            move_cmd.linear.x = self.linear_speed
            move_cmd.angular.z = 0.0

        # Front is blocked! Stop immediately and evaluate sides
        else:
            move_cmd.linear.x = 0.0  # STOPPED
            
            # TRAPPED! Front, Left, and Right are ALL blocked below safety limit
            if left_dist <= self.safety_limit and right_dist <= self.safety_limit:
                move_cmd.angular.z = rad  # Spin left fast to escape
                self.get_logger().warn("TOTAL AREA BLOCKED! Making a full turn to escape.")

            #  Left side has more space than Right side -> Turn Left
            elif left_dist > right_dist:
                move_cmd.angular.z = rad
                self.get_logger().info(f"Front blocked. Turning LEFT (Left: {left_dist:.2f}m | Right: {right_dist:.2f}m)")

            # Right side has more space than Left side -> Turn Right
            elif right_dist > left_dist:
                move_cmd.angular.z = -rad
                self.get_logger().info(f"Front blocked. Turning RIGHT (Right: {right_dist:.2f}m | Left: {left_dist:.2f}m)")
                
            # Sides are equal but clear enough to turn into Left
            else:
                move_cmd.angular.z = rad
                self.get_logger().info("Sides equal. Defaulting LEFT turn.")

        self.pub.publish(move_cmd)
        
def main(args=None):
    rclpy.init(args=args)
    node=Turtlebot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info(f"total distance travelled = {node.total_dist :.2f} meters")

    finally:
        node.destroy_node()
        import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import LaserScan #for obstacle detection 
from geometry_msgs.msg import Twist #for turning momentum
from nav_msgs.msg import Odometry #distance tracking of bot
import math

class Turtlebot(Node):
    def __init__(self):
        super().__init__('turtle_bot_node')

        self.pub=self.create_publisher(Twist,'/cmd_vel',10)
        self.laser_sub=self.create_subscription(LaserScan,'/scan',self.scan_cb,10)
        self.odom_sub=self.create_subscription(Odometry,'/odom',self.odom_cb,10)

        #distance tracking variables
        self.total_dist = 0.0
        self.previous_x = None
        self.previous_y = None

        self.safety_limit = 1.2 # meters
        self.linear_speed = 0.5 # m/s

        self.get_logger().info(f'turtle bot with odometry initialized')

    def odom_cb(self,msg):

         current_x = msg.pose.pose.position.x
         current_y = msg.pose.pose.position.y

         if self.previous_x is None or self.previous_y is None :
             self.previous_x = current_x
             self.previous_y = current_y
             return
         
         dist_step = math.sqrt((current_x-self.previous_x)**2 + (current_y-self.previous_y)**2)

         self.total_dist+=dist_step

         self.previous_x = current_x
         self.previous_y = current_y

    def scan_cb(self,msg):
        
        # ---------------- FRONT ----------------

        front_ranges = msg.ranges[165:195]

        front_ranges = [
            x for x in front_ranges
            if not math.isinf(x) and not math.isnan(x)
        ]

        # ---------------- LEFT ----------------

        left_ranges = msg.ranges[255:285]

        left_ranges = [
            x for x in left_ranges
            if not math.isinf(x) and not math.isnan(x)
        ]

        # ---------------- RIGHT ----------------

        right_ranges = msg.ranges[75:105]

        right_ranges = [
            x for x in right_ranges
            if not math.isinf(x) and not math.isnan(x)
        ]

        # Safe defaults

        front_dist = min(front_ranges) if front_ranges else 10.0
        left_dist = min(left_ranges) if left_ranges else 10.0
        right_dist = min(right_ranges) if right_ranges else 10.0

        # Debug info

        self.get_logger().info(
            f"Front: {front_dist:.2f} | "
            f"Left: {left_dist:.2f} | "
            f"Right: {right_dist:.2f}"
        )

        move_cmd = Twist()

        deg = 30
        rad = deg*math.pi/180  # m/s

        # Front is clear -> Move Forward
        if front_dist > self.safety_limit:
            move_cmd.linear.x = self.linear_speed
            move_cmd.angular.z = 0.0

        # Front is blocked! Stop immediately and evaluate sides
        else:
            move_cmd.linear.x = 0.0  # STOPPED
            
            # TRAPPED! Front, Left, and Right are ALL blocked below safety limit
            if left_dist <= self.safety_limit and right_dist <= self.safety_limit:
                move_cmd.angular.z = rad  # Spin left fast to escape
                self.get_logger().warn("TOTAL AREA BLOCKED! Making a full turn to escape.")

            #  Left side has more space than Right side -> Turn Left
            elif left_dist > right_dist:
                move_cmd.angular.z = rad
                self.get_logger().info(f"Front blocked. Turning LEFT (Left: {left_dist:.2f}m | Right: {right_dist:.2f}m)")

            # Right side has more space than Left side -> Turn Right
            elif right_dist > left_dist:
                move_cmd.angular.z = -rad
                self.get_logger().info(f"Front blocked. Turning RIGHT (Right: {right_dist:.2f}m | Left: {left_dist:.2f}m)")
                
            # Sides are equal but clear enough to turn into Left
            else:
                move_cmd.angular.z = rad
                self.get_logger().info("Sides equal. Defaulting LEFT turn.")

        self.pub.publish(move_cmd)
        
def main(args=None):
    rclpy.init(args=args)
    node=Turtlebot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print(f"\nFinal distance travelled = {node.total_dist:.2f} meters")

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()
        

if __name__ == '__main__':
    main()

