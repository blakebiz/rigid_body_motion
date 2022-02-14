# import numpy for arrays
import numpy as np
# import math for rotations
from math import sin, cos


def hom_trans_x(a):
    # homogenous translation over x
    return np.array([[1, 0, 0, a],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])


def hom_trans_y(b):
    # homogenous translation over y
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, b],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])


def hom_trans_z(c):
    # homogenous translation over z
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, c],
                     [0, 0, 0, 1]])


def hom_rot_x(a):
    # homogenous rotation over x
    return np.array([[1, 0, 0, 0],
                     [0, cos(a), -sin(a), 0],
                     [0, sin(a), cos(a), 0],
                     [0, 0, 0, 1]])


def hom_rot_y(b):
    # homogenous rotation over y
    return np.array([[cos(b), 0, sin(b), 0],
                     [0, 1, 0, 0],
                     [-sin(b), 0, cos(b), 0],
                     [0, 0, 0, 1]])


def hom_rot_z(c):
    # homogenous rotation over z
    return np.array([[cos(c), -sin(c), 0, 0],
                     [sin(c), cos(c), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

