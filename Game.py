import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


M = np.zeros((16, 16))

def _init(row,col):
    global M
    M = np.zeros((row,col), dtype=int)

    M[1,1]=1
    M[2,2]=1
    M[3,3]=1
    M[4,4]=1
    M[5,5]=1
    M[4,5]=1
    M[2, 5] = 1
    M[1, 5] = 1

    M[5, 4] = 1
    M[5, 3] = 1
    M[5,2]=1
    M[5,1]=1


def check(N):
    count = N.sum()
    if N[1,1] == 0 and count == 2:
        return 1
    if N[1,1] == 1 and (count ==3 or count == 4):
        return 1
    return 0


def update(i):
    global M
    row, col =  M.shape
    temp = np.zeros((row,col))
    for i in range(row):
        for j in range(row):
            neighborhood = np.zeros((3,3))
            for k in range(-1,1):
                for l in range(-1, 1):
                    neighborhood[k+1,l+1] = M[(k+i+row)%row,(l+j+col)%col]
            temp[i,j]= check(neighborhood)
    M=temp
    matrice.set_array(M)

_init(16,16)

fig, ax = plt.subplots()
matrice = ax.matshow(M)
plt.colorbar(matrice)

ani = animation.FuncAnimation(fig, update, frames=19, interval=500)
plt.show()