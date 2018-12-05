import os,math,matplotlib.pyplot as plt

def draw_plot_points(path):
    pointsFile = open(path, 'r')
    points = eval(pointsFile.read())
    plt.axis([116.25, 116.50, 39.8, 40.05])
    o_x = 116.25
    o_y = 39.8
    map_width = 0.25
    map_height = 0.25
    area_width_segments = 10
    area_height_segments = 10
    area_width_split = 5
    area_height_split = 5
    area_width = map_width / area_width_segments
    area_height = map_height / area_height_segments
    split_width = area_width / area_width_split
    split_height = area_height / area_height_split
    colors = ['#FFFFFF','#F5F5F5','#DCDCDC','#D3D3D3','#C0C0C0','#A9A9A9','#808080','#696969','#000000']
    for i in range(area_width_segments):
        for j in range(area_height_segments):
            for x in range(area_width_split):
                for y in range(area_height_split):
                    c=0
                    while c<9:
                        if points[i][j][x][y]==0:
                            plt.scatter(o_x + i * area_width + (x + 0.5) * split_width,
                                        o_y + j * area_height + (y + 0.5) * split_height, s = 100,c = '#ffffff',marker='s')
                            break
                        if c*5<=points[i][j][x][y]<(c+1)*5:
                            plt.scatter(o_x+i*area_width+(x+0.5)*split_width,o_y+j*area_height+(y+0.5)*split_height,s = 100,c =colors[c],marker='s')
                            break
                        c+=1
                    if c>=9:
                        plt.scatter(o_x + i * area_width + (x + 0.5) * split_width,
                                    o_y + j * area_height + (y + 0.5) * split_height, s=100, c='#000000', marker='s')
    plt.show()
def draw_plot_cars(path):
    cars_file = open(path, 'r')
    cars = eval(cars_file.read())
    plt.axis([116.25, 116.50, 39.8, 40.05])
    for car in cars:
        plt.scatter(car[0], car[1], 2,'#000000')
    plt.show()
if __name__ == '__main__':
    path1 = os.path.join(os.getcwd(), 'datas','cars_density.txt')
    #path2 = os.path.join(os.getcwd(), 'materials', 'cars.txt')
    draw_plot_points(path1)
    #draw_plot_cars(path2)

