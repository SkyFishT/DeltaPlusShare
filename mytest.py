import math,random,numpy as np

def myt():
    x=[0]*10
    y=[]
    for i in range(100000):
        tmp = int(random.random()*10)
        x[tmp] = x[tmp]+1
        tmpy=[0]*10
        tmpy[tmp] = 1
        for j in range(10):
            tmpy[j] = tmpy[j] + np.random.laplace(0,2,None)
        y.append(tmpy)
    result=[0]*10
    for i in range(10):
        for j in range(100000):
            result[i] = result[i]+y[j][i]
    print x
    print result

if __name__ == '__main__':
    myt()