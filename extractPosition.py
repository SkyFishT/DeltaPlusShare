import os,datetime
def extractPosition():
    path = os.path.join(os.getcwd(), 'taxi_log_2008_by_id')
    pointsfile = open(os.path.join(os.getcwd(), 'materials', 'cars.txt'), 'w')  # set of points
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
    pointsfile.write(str(cars))
    pointsfile.close()

if __name__ == '__main__':
    extractPosition()