#!/usr/bin/env python
# license removed for brevity
# author: hwang
# created on: 06/14/2017
# modified on: XX/XX/XXXX
import rospy
from sensor_msgs.msg import JointState
import csv

def update_state_and_publish():
    joint_angle_table = []
    pub = rospy.Publisher("ur5/joint_states", JointState, queue_size=10)
    rospy.init_node("test_playback_node", anonymous=True)
    rate = rospy.Rate(100) # 1kHz
    with open("out_js_disp.csv", 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
            joint_angle_table.append([float(r) for r in row])
#    robot_data_reader = UR5_dataReader()
#    while not rospy.is_shutdown():
#	robot_data_reader.update()
#        verify_str = "%.4f, %.4f, %.4f, %.4f, %.4f, %.4f" % (robot_data_reader.q_actual[0],robot_data_reader.q_actual[1], robot_data_reader.q_actual[2],robot_data_reader.q_actual[3],robot_data_reader.q_actual[4],robot_data_reader.q_actual[5])
#        rospy.loginfo(verify_str)
#	rospy.loginfo(robot_data_reader.joint_state.position)
    js = JointState()
    js.name = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
    js.position = [ 3.47172217e+00,  -2.14456987e+00,  -1.91532757e+00,   9.18540937e-01,
  -3.30283928e-01,  -3.21397317e-04]
    ''' 
    while not rospy.is_shutdown():
        js.header.stamp = rospy.Time.now()
	pub.publish(js)
        rate.sleep()
    '''
    for i in range(len(joint_angle_table)):
        cur_joint_anlge = joint_angle_table[i]
        js.position = cur_joint_anlge
        js.header.stamp = rospy.Time.now()
        print js
        pub.publish(js)
        rate.sleep()
if __name__ == '__main__':
    try:
        update_state_and_publish()
    except rospy.ROSInterruptException:
        pass
