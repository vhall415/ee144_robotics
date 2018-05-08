#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist

class turtlebot_move():
    def __init__(self):
        rospy.init_node('turtlebot_move', anonymous=False)  		

	rospy.loginfo("Press CTRL + C to terminate")
 
        rospy.on_shutdown(self.shutdown)
        
        self.set_velocity = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

        vel = Twist()
        vel.linear.x = 0.5
	vel.angular.z = 0

	#START LAB2 CODE
	rate = rospy.Rate(1); 	#initialize clockspeed TO 1 hertz
	currT = rospy.Time(0); 	#obtain initial time
	diffT = 0; 		#diffT tracks counter of 10 secs before turning
	prevT = currT 		#assign currT to prevT for next iteration


        while not rospy.is_shutdown():
	    currT = rospy.Time.now();	#retrieve updated time each cylce			
	    diffT = diffT + currT.to_sec() - prevT.to_sec() #diff between clock cycles
	
	#if diff >= 10, turn robot 90 degrees clockwise
	#else, reset linear speed to 0.5 and angular to zero
	    if diffT >= 10:
		diffT = 0
		vel.linear.x = 0
		vel.angular.z = 3.14
	    else:
	    	vel.linear.x = .5
	    	vel.angular.z = 0

	    print(currT.to_sec(), diffT)
	    prevT = currT		
            self.set_velocity.publish(vel) #published command to robot
            rate.sleep()
	#END LAB2 CODE
                        
        
    def shutdown(self):

        rospy.loginfo("Stop Action")
	stop_vel = Twist()
        stop_vel.linear.x = 0
	stop_vel.angular.z = 0
        self.set_velocity.publish(stop_vel)

        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        turtlebot_move()
    except rospy.ROSInterruptException:
        rospy.loginfo("Action terminated.")

