# import p2_sol for trans/rot functions
import p2_sol
# import numpy for array multiplication
import numpy as np
# import math for pi constant
from math import pi

def transformation_1():
    # x translation of 2.5
    t1 = p2_sol.hom_trans_x(2.5)
    # z translation of .5
    t2 = p2_sol.hom_trans_z(.5)
    # y translation of -1.5
    t3 = p2_sol.hom_trans_y(-1.5)
    # combine and return all transformations
    return np.matmul(t1, t2, t3)

def transformation_2():
    # z translation of .5
    t1 = p2_sol.hom_trans_z(.5)
    # x translation of 2.5
    t2 = p2_sol.hom_trans_x(2.5)
    # y translation of -1.5
    t3 = p2_sol.hom_trans_y(-1.5)
    # combine and return all transformations
    return np.matmul(t1, t2, t3)

def transformation_3():
    # x rotation of 2.5
    t1 = p2_sol.hom_rot_x(2.5)
    # z rotation of .5
    t2 = p2_sol.hom_trans_z(.5)
    # y translation of -1.5
    t3 = p2_sol.hom_trans_y(-1.5)
    # combine and return all transformations (fixed order)
    return np.matmul(t3, t2, t1)

def transformation_4():
    # z translation of .5
    t1 = p2_sol.hom_trans_z(.5)
    # x translation of 2.5
    t2 = p2_sol.hom_trans_x(2.5)
    # y translation of -1.5
    t3 = p2_sol.hom_trans_y(-1.5)
    # combine and return all transformations (fixed order)
    return np.matmul(np.matmul(t3, t2), t1)

def transformation_5():
    # x rotation of pi/2
    t1 = p2_sol.hom_rot_x(pi/2)
    # x translation of 3
    t2 = p2_sol.hom_trans_x(3)
    # z translation of -3
    t3 = p2_sol.hom_trans_z(-3)
    # z rotation of -pi/2
    t4 = p2_sol.hom_rot_z(-pi/2)
    # combine and return all transformations
    return np.matmul(np.matmul(t1, t2), np.matmul(t3, t4))


if __name__ == '__main__':
    # call each function and print result
    H_1 = transformation_1()
    print('H_1:\n', H_1, '\n\n', sep='')

    H_2 = transformation_2()
    print('H_2:\n', H_2, '\n\n', sep='')

    H_3 = transformation_3()
    print('H_3:\n', H_3, '\n\n', sep='')

    H_4 = transformation_4()
    print('H_4:\n', H_4, '\n\n', sep='')

    H_5 = transformation_5()
    print('H_5:\n', H_5, '\n\n', sep='')



