import os,math,datetime
def extractPosition():
    path = os.path.join(os.getcwd(), 'taxi_log_2008_by_id')
    carsfile = open(os.path.join(os.getcwd(), 'materials', 'cars.txt'), 'w')  # set of points
    cars=[]
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        rawfile = open(file_path, 'r')
        line = rawfile.readline()
        while line:
            line = line.split(',')
            cmp_time = datetime.datetime.strptime('2008-02-02 16:10:00','%Y-%m-%d %H:%M:%S')
            our_time = datetime.datetime.strptime(line[1],'%Y-%m-%d %H:%M:%S')
            x = float(line[2])
            y = float(line[3])
            if our_time>cmp_time and x>=116.25 and x<=116.50 and y>=39.8 and y<= 40.05:
                cars.append([x,y])
                break
            else:
                line = rawfile.readline()
        rawfile.close()
    carsfile.write(str(cars))
    carsfile.close()

    #product points
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
    split_width = area_width/area_width_split
    split_height = area_height/area_height_split
    points=[]
    pointsfile = open(os.path.join(os.getcwd(), 'materials', 'points.txt'), 'w')  # set of points
    for i in range(area_width_segments):
        points.append([])
        for j in range(area_height_segments):
            points[i].append([])
            x_array = []
            y_array = []
            for x in range(area_width_split):
                x_array.append(o_x+i*area_width+split_width/2+x*split_width)
            for y in range(area_width_split):
                y_array.append(o_y+j*area_height+split_height/2+y*split_height)
            for x in range(area_width_split):
                for y in range(area_height_split):
                    points[i][j].append([x_array[x],y_array[y]])
    pointsfile.write(str(points))
    pointsfile.close()
if __name__ == '__main__':
    extractPosition()