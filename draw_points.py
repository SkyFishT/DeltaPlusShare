import os,math,matplotlib.pyplot as plt

def draw_plot_points(path):
    pointsFile = open(path, 'r')
    points = eval(pointsFile.read())
    plt.axis([116.25, 116.50, 39.8, 40.05])
    o_x = 116.25
    o_y = 39.8
    map_width = 0.25
    map_height = 0.25
    area_width_segments = 5
    area_height_segments = 5
    area_width_split = 5
    area_height_split = 5
    area_width = map_width / area_width_segments
    area_height = map_height / area_height_segments
    split_width = area_width / area_width_split
    split_height = area_height / area_height_split
    colors = ['#DA70D6','#EE82EE','#FF00FF','#FF1493','#FF0000','#DC143C','#9400D3','#8B008B','#4B0082','#0000CD','#00008B','#000000']
    for i in range(5):
        for j in range(5):
            for x in range(area_width_split):
                for y in range(area_height_split):
                    c=0
                    while c<12:
                        if points[i][j][x][y]==0:
                            plt.scatter(o_x + i * area_width + (x + 0.5) * split_width,
                                        o_y + j * area_height + (y + 0.5) * split_height, s = 20,c = '#ffffff',marker='s')
                            break
                        if c*10<=points[i][j][x][y]<(c+1)*10:
                            plt.scatter(o_x+i*area_width+(x+0.5)*split_width,o_y+j*area_height+(y+0.5)*split_height,s = 20,c =colors[c],marker='s')
                            break
                        c+=1
                    if c>=12:
                        plt.scatter(o_x + i * area_width + (x + 0.5) * split_width,
                                    o_y + j * area_height + (y + 0.5) * split_height, s=20, c='#000000', marker='s')
    plt.show()
def draw_plot_cars(path):
    cars_file = open(path, 'r')
    cars = eval(cars_file.read())
    plt.axis([116.25, 116.50, 39.8, 40.05])
    for car in cars:
        plt.scatter(car[0], car[1], 2,'#000000')
    plt.show()
if __name__ == '__main__':
    path1 = os.path.join(os.getcwd(), 'datas', 'exponent','confusing_cars_density_epsilon4.0.txt')
    #path2 = os.path.join(os.getcwd(), 'materials', 'cars.txt')
    draw_plot_points(path1)
    #draw_plot_cars(path2)

