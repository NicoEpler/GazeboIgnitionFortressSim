import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class FlightController(Node):
    def __init__(self):
        super().__init__('flight_controller')
        self.publisher_0 = self.create_publisher(Float64, '/x500/rotor_0_joint/cmd_vel', 10)
        self.publisher_1 = self.create_publisher(Float64, '/x500/rotor_1_joint/cmd_vel', 10)
        self.publisher_2 = self.create_publisher(Float64, '/x500/rotor_2_joint/cmd_vel', 10)
        self.publisher_3 = self.create_publisher(Float64, '/x500/rotor_3_joint/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10)

    def cmd_vel_callback(self, msg):
        # Convert Twist message to motor speed commands
        linear_x = msg.linear.x
        angular_z = msg.angular.z

        # Example: Convert linear and angular velocities to motor speed commands
        # Adjust as needed based on your drone's dynamics
        motor_speed_0 = linear_x + angular_z
        motor_speed_1 = linear_x - angular_z
        motor_speed_2 = linear_x + angular_z
        motor_speed_3 = linear_x - angular_z

        # Publish motor speed commands
        self.publisher_0.publish(Float64(data=motor_speed_0))
        self.publisher_1.publish(Float64(data=motor_speed_1))
        self.publisher_2.publish(Float64(data=motor_speed_2))
        self.publisher_3.publish(Float64(data=motor_speed_3))

def main(args=None):
    rclpy.init(args=args)
    flight_controller = FlightController()
    rclpy.spin(flight_controller)
    flight_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
