from functools import partial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pycpd import RigidRegistration
import numpy as np


# target_file = file that is being transformed
# source_file = file that is being matched
# This algorithm takes in two .txt files and matches
# the point clouds with a Rigid Registration.
# see las_to_txt.py to generate properly formatted .txt
# files from a .las file.

def visualize(iteration, error, X, Y, ax):
    plt.cla()
    ax.scatter(X[:, 0],  X[:, 1], X[:, 2], color='red', label='Target')
    ax.scatter(Y[:, 0],  Y[:, 1], Y[:, 2], color='blue', label='Source')
    ax.text2D(0.87, 0.92, 'Iteration: {:d}\nQ: {:06.4f}'.format(
        iteration, error), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize='x-large')
    ax.legend(loc='upper left', fontsize='x-large')
    plt.draw()
    plt.pause(0.001)


def main():
    target_file = '' # put target file name here
    target = np.loadtxt(target_file)
    X = np.zeros((target.shape[0], target.shape[1] + 1))
    X[:, :-1] = target

    source_file = '' # put source file name here
    source = np.loadtxt(source_file)
    Y = np.zeros((source.shape[0], source.shape[1] + 1))
    Y[:, :-1] = source

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    callback = partial(visualize, ax=ax)

    reg = RigidRegistration(**{'X': X, 'Y': Y})
    reg.register(callback)
    # plt.show()


if __name__ == '__main__':
    main()
