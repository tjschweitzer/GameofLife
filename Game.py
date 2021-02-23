import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal


def game(A,bc = "Periodic"):

    A_NN = nearest_neibour_interp_fast(A,bc)

    remains_alive_condition = np.logical_and(A==1, np.logical_or(A_NN==2, A_NN==3))
    random_life = np.logical_and(A==0, A_NN==3)

    A_new = np.where(np.logical_or(remains_alive_condition,random_life),1,0)

    return A_new

def nearest_neibour_interp_fast(A, bc):

    k = [[True, True, True],
         [True, False, True],
         [True, True, True]]

    if bc == "Periodic":
        convolution = signal.convolve2d(A, k, mode='same', boundary='wrap')
    elif bc == "Symmetric":
        convolution = signal.convolve2d(A, k, mode='same', boundary='symm')
    else:
        convolution = signal.convolve2d(A, k, mode='same', boundary='fill')
    # print(convolution)
    return convolution


def _init(size, p=.5, shape="Random"):
    if shape == "Random":
        A = np.random.random(size)

        return np.where(A > p, 0, 1)
    A = np.zeros(size)
    if shape == 1:
        A[3, 3] = 1
        A[4, 3] = 1
        A[5, 3] = 1
    if shape == 2:
        A[3, 3] = 1
        A[4, 4] = 1
        A[3, 4] = 1
    if shape == 3:
        A[3, 3] = 1
        A[4, 3] = 1
        A[5, 3] = 1
        A[6, 3] = 1
    if shape == 4:
        A[3, 3] = 1
        A[4, 3] = 1
        A[5, 3] = 1
        A[4, 4] = 1
    if shape == 5:
        A[3, 3] = 1
        A[4, 3] = 1
        A[5, 3] = 1
        A[4, 4] = 1
    if shape == 6:
        A[3, 3] = 1
        A[4, 3] = 1
        A[5, 3] = 1
        A[5, 2] = 1
        A[4, 1] = 1
    if shape == 7:
        A[3, 4] = 1
        A[4, 3] = 1
        A[5, 3] = 1
        A[5, 2] = 1
        A[4, 1] = 1
    if shape == 8:
        A[3, 3] = 1
        A[4, 3] = 1
        A[5, 3] = 1
        A[4, 4] = 1
        A[5, 4] = 1
        A[6, 4] = 1

    return A



inital_prob = 0.7
life = _init((32,32), inital_prob,5)

frames = 1000

fig, ax = plt.subplots(constrained_layout=False)
image = ax.imshow(life)


def update(i):
    global life
    image.set_data(life)
    life = game(life, bc='Periodic')
    biodensity = np.mean(life)*100
    ax.set_title("Life after {} interations. \n Enviroment is {:.2f}% full of life".format(i+1,biodensity))

ani = animation.FuncAnimation(fig, update,repeat=False ,frames=50, interval=500)
plt.show()