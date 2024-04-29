import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class Gosper_curve(Node):

    def __init__(self):
        super().__init__('curve_drawer')
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel',10)
        self.timer = self.create_timer(1.0, self.publish_twist)
        self.A_rule = "A-B--B+A++AA+B-"
        self.B_rule = "+A-BB--B-A++A+B"

    def gospercurve(self, n, size, rule):
         if n == 0:
            twist = Twist()
            twist.linear.x += size
            self.publisher_.publish(twist)
            return

         selected_rule = self.A_rule if rule=='A' else self.B_rule
         for i in selected_rule:
             print(n)
             print(i)
             time.sleep(1.0)
             if i == 'A':
                self.gospercurve(n-1,size,'A')
             elif i == 'B':
                self.gospercurve(n-1,size,'B')
             elif i == '-':
                self.rotate(-60)
             else:
                self.rotate(60)

    def rotate(self, angle):
        twist = Twist()
        print(angle)
        twist.angular.z = math.radians(angle)
        self.publisher_.publish(twist)

    def publish_twist(self):
        size = 0.2
        n = 4.0
        self.gospercurve(n,size,'A')

def main(args=None):
    rclpy.init(args=args)
    gosper_c = Gosper_curve()
    rclpy.spin(gosper_c)
    gosper_c.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

