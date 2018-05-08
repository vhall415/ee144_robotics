from __future__ import division
from math import pi, cos, sin, atan2, acos
import numpy as np
import math
from collections import namedtuple

EPSILON = 1e-3

position = namedtuple('position', ['x', 'y'])
jointangle = namedtuple('jointangle', ['theta1', 'theta2'])
makeVector = namedtuple('makeVector', ['x', 'y'])

class Arm(object):
        #q0 - initial positions of joints
        #origin - position of the base of the arm in carthesian space
    def __init__(self, link1=1.0, link2=1.0, q0=jointangle(0,0), origin=makeVector(0,0)):
        self.link1 = link1
        self.link2 = link2
        self.lsq = link1 ** 2 + link2 ** 2
        self.joints = q0
        self.origin = origin
        self.end_effector = self.compute_end_effector()

    def forward_kinematics(self, input_joints):
        self.joints = input_joints
        self.end_effector = self.compute_end_effector()
        return self.end_effector

    def compute_end_effector(self):
	#the return of the function is the position of end_effector, start with self.joints.theta1 and self.joints.theta2
        ################################ Computes end_effector position knowing joint angles, your code goes between ##############################
        Ang1 = self.joints.theta1
        Ang2 = self.joints.theta2

        x = self.link1*math.cos(Ang1) + self.link2*math.cos(Ang1 + Ang2) + self.origin.x
        y = self.link1*math.sin(Ang1) + self.link2*math.sin(Ang1 + Ang2) + self.origin.y
		###########################################################################################################################################
        return position(x, y)

    def inverse_kinematics(self, input_ee):
	############################### check if the end effector position is reachable, your code goes below #####################################
	#in your code, please include 
	#raise ValueError('your words')
	#so that your code can pass the test case
        if(input_ee.x == 0 and input_ee.y == 0):
            raise ValueError('Out of Range')

        self.end_effector = input_ee
        self.joints = self.compute_joints()
        return self.joints

    def compute_joints(self):
	#the return of the function are angles of joints, which should stay between -pi and pi. Start with self.end_effector.x and self.end_effector.y.
        ################################# Computes joint angle knowing end effector position, your code goes below #################################

        x = self.end_effector.x - self.origin.x
        y = self.end_effector.y - self.origin.y
        
        if(x != 0 or y != 0):
            L2 = self.link2 # length a
            L1 = self.link1 # length c
            b = math.sqrt(x**2 + y**2)

            alpha = math.acos((-L2**2 + b**2 + L1**2)/(2*b*L1))
            beta = math.acos((L2**2 -b**2 + L1**2)/(2*L2*L1))
            gamma = math.atan2(y,x)

            theta1 = gamma - alpha
            theta2 = pi - beta
        else:
            theta1 = 0
            theta2 = 0

        return jointangle(theta1, theta2)

