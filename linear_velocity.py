import rospy
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Imu

global velocity_x
global velocity_y
global velocity_z

velocity_x = 0
velocity_y = 0
velocity_z = 0
# publish velocity data on new topic
def data_callback(data: Imu):
	delta_t = 1/20

	for i in range(2):
        velocity_x += (data.linear_acceleration.x * delta_t)
    	velocity_y += (data.linear_acceleration.y * delta_t)
    	velocity_z += (data.linear_acceleration.z * delta_t)
	velocity_msg = Vector3(velocity_x, velocity_y, velocity_z, 0)
	pub.publish(velocity_msg)


# subscriber to imu data
sub = rospy.Subscriber("imu_topic", Imu, callback=data_callback)
pub = rospy.Publisher("velocity_topic", Vector3, queue_size=10) # might modify queue size


