import os,math,matplotlib.pyplot as plt

def draw_plot(path):
    pointsFile = open(path, 'r')
    points = eval(pointsFile.read())
    plt.axis([116.25, 116.50, 39.8, 40.05])
    o_x = 116.25
    o_y = 39.8
    map_width = 0.25
    map_height = 0.25
    area_width_segments = 5
    area_height_segments = 5
    area_width_split = 10
    area_height_split = 10
    area_width = map_width / area_width_segments
    area_height = map_height / area_height_segments
    split_width = area_width / area_width_split
    split_height = area_height / area_height_split
    for i in range(5):
        for j in range(5):
            for x in range(area_width_split):
                for y in range(area_height_split):
                    if points[i][j][x][y]==0:
                        continue
                    plt.scatter(o_x+i*area_width+(x+0.5)*split_width,o_y+j*area_height+(y+0.5)*split_height,2,'#000000')
    plt.show()

if __name__ == '__main__':
    path = os.path.join(os.getcwd(), 'datas', 'cars_density.txt')
    draw_plot(path)

