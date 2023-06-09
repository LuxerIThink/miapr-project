#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from tf2_msgs.msg import TFMessage
import math

class Dist(Node):
    def __init__(self):
        super().__init__('planner_distance')
        self.pathSubscriber = self.create_subscription(Path, '/received_global_plan',self.sub_callback,10)
        self.goalPublisher = self.create_publisher(PoseStamped, '/goal_pose', 10)

        self.boool = True

        self.goalX = -1.
        self.goalY = -1.

        self.startTime = self.get_clock().now()
        self.publish_goal(self.goalX, self.goalY)

    def publish_goal(self, goalX, goalY):
        goal = PoseStamped()
        goal.pose.position.x = goalX
        goal.pose.position.y = goalY
        header = Header()
        header.frame_id = 'map'
        self.startTime = self.get_clock().now()
        header.stamp = self.startTime.to_msg()
        goal.header = header
        self.goalPublisher.publish(goal)
        print('Goal set')
    
    def sub_callback(self, data: Path):
        if self.boool == True:
            self.boool = False
            pathLength = 0
            for i in range(len(data.poses) - 1):
                pathLength += math.sqrt(math.pow((data.poses[i].pose.position.x - data.poses[i+1].pose.position.x), 2) + math.pow((data.poses[i].pose.position.y- data.poses[i+1].pose.position.y), 2))
            print('Path length : ', pathLength)
        
def main(args=None):
    rclpy.init(args=args)
    dist = Dist()
    rclpy.spin(dist)
    dist.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
