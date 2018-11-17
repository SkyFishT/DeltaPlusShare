import os,random,math,numpy as np
def positionConfusingByLaplace(epsilon):
    def the_area_belongTo(position):
        indexs=[0]*4
        for i in range(area_width_segments):
            if o_x+area_width*i<=position[0]< o_x+area_width*(i+1):
                indexs[0] = i
                for j in range(area_width_split):
                    if o_x+area_width*i+split_width*j<=position[0]<o_x+area_width*i+split_width*(j+1):
                        indexs[2] = j
                        break
                break
        for i in range(area_height_segments):
            if o_y+area_height*i <= position[1]< o_y+area_height*(i+1):
                indexs[1] = i
                for j in range(area_height_split):
                    if o_y+area_height*i+split_height*j<=position[1]<o_y+area_height*i+split_height*(j+1):
                        indexs[3] = j
                        break
                break
        return indexs
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
    def mappingConfusingPositionByLaplace(position,epsilon,deltaF):
        dist = np.random.laplace(0,float(deltaF)/epsilon)
        angle = random.random() * math.pi * 2
        return [position[0]+dist * math.cos(angle),position[1]+dist * math.sin(angle)]
    confusing_cars=[]
    cars_file = open(os.path.join(os.getcwd(), 'materials', 'cars.txt'), 'r')
    cars = eval(cars_file.read())
    cars_file.close()
    for car in cars:
        tmp_car = mappingConfusingPositionByLaplace(car,epsilon,split_width)
        if 116.25<tmp_car[0]<116.5 and 39.8<tmp_car[1]<40.5:
            confusing_cars.append(tmp_car)
    confusing_cars_density = []
    for i in range(5):
        confusing_cars_density.append([])
        for j in range(5):
            tmp_cars_density = [[0] * area_width_split for k in range(area_height_split)]
            confusing_cars_density[i].append(tmp_cars_density)
    for car in confusing_cars:
        indexs = the_area_belongTo(car)
        confusing_cars_density[indexs[0]][indexs[1]][indexs[2]][indexs[3]] +=1
    cars_density_file = open(os.path.join(os.getcwd(), 'datas','laplace', 'confusing_cars_density_epsilon'+str(epsilon)+'.txt'), 'w')
    cars_density_file.write(str(confusing_cars_density))
    cars_density_file.close()


if __name__ == '__main__':
    epsilon = [x * 0.1 for x in range(1, 41)]
    for i in epsilon:
        positionConfusingByLaplace(i)