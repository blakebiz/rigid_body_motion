# import the rigid body module
import rbm
import math
import numpy as np

if __name__ == '__main__':
    psi = math.pi / 2
    theta = math.pi / 2
    phi = math.pi / 2
    np.set_printoptions(precision=2, suppress=True)
    v0 = rbm.vec(0, 1, 1)
    Rx = rbm.rot_x(psi)
    Ry = rbm.rot_y(theta)
    Rz = rbm.rot_z(phi)
    R = np.matmul(Rz, Ry, Rx)
    v01 = R.dot(v0)
    print('The transformed vector (rotations about FIXED FRAME) is:\n', v01)