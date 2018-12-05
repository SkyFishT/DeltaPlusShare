#coding:utf-8
import matplotlib.pyplot as plt
import os,numpy as np

def draw_plot():
    edges = np.load(os.path.join(os.getcwd(),'datas','linprog', 'delta_spanner.npy'))
    area_width_split = 5
    area_height_split = 5
    points=[]
    for i in range(area_width_split):
        for j in range(area_height_split):
            points.append([i,j])
    for i in points:
        plt.scatter(i[0],i[1],s=100,c='k')

    plt.show()
if __name__ == "__main__":
    draw_plot()