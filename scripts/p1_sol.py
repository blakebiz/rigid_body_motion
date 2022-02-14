import rbm
import math
import numpy as np


def roll_pitch_yaw(vector):
    # roll
    Rx = rbm.rot_x(psi)
    # pitch
    Ry = rbm.rot_y(theta)
    # roll
    Rz = rbm.rot_z(phi)
    R = np.matmul(Rz, Ry, Rx)
    return R.dot(vector)

if __name__ == '__main__':
    # set constants
    psi = math.pi / 2
    theta = math.pi / 2
    phi = math.pi / 2
    # numpy print config
    np.set_printoptions(precision=2, suppress=True)
    # declare vector
    v0 = rbm.vec(0, 1, 1)
    # call function with vector
    v01 = roll_pitch_yaw(v0)
    # display original and final
    print('The original vector is:\n', v0)
    print('The transformed vector (rotations about FIXED FRAME) is:\n', v01)