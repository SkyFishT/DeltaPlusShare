import os,math,matplotlib.pyplot as plt

def draw_plot(path):
    pointsFile = open(path, 'r')
    points = eval(pointsFile.read())
    plt.axis([116.25, 116.50, 39.8, 40.05])
    for i in points:
        plt.scatter(i[0],i[1],2,'#000000')
    plt.show()

if __name__ == '__main__':
    path = os.path.join(os.getcwd(), 'materials', 'cars.txt')
    draw_plot(path)

