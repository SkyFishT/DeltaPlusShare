import os,math,numpy as np
def positionConfusing():
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
    cars_file = open(os.path.join(os.getcwd(), 'materials', 'cars.txt'), 'r')
    cars = eval(cars_file.read())
    cars_density= []
    for i in range(5):
        cars_density.append([])
        for j in range(5):
            tmp_cars_density = [[0]*area_width_split for k in range(area_height_split)]
            cars_density[i].append(tmp_cars_density)
    for car in cars:
        indexs = the_area_belongTo(car)
        cars_density[indexs[0]][indexs[1]][indexs[2]][indexs[3]] +=1
    cars_density_file = open(os.path.join(os.getcwd(), 'datas', 'cars_density.txt'), 'w')
    cars_density_file.write(str(cars_density))
    cars_density_file.close()
    # epsilon = [x * 0.1 for x in range(1, 21)]
    # for e in epsilon:
    #     matrix_file = open(os.path.join(os.getcwd(), 'datas', 'linprog' + str(epsilon) + '.txt'), 'r')
    #     matrix = eval(matrix_file.read())
    #     matrix_file.close()
    # travers_cars = []
    # def distance_of_two_point(x, y, ndigits=2):
    #     return round(math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2)), ndigits)
    #
    # def closest_points(x):
    #     closest_dist = float('Inf')
    #     for i in points:
    #         cur_dist = distance_of_two_point(x, i)
    #         if closest_dist > cur_dist:
    #             closest_dist = cur_dist
    #             closest_point = i
    #     return closest_point
    #
    # def traverse(point):
    #     closest_point = closest_points(point)
    #     index = -1
    #     for i in points:
    #         index += 1
    #         if closest_point == i:
    #             break
    #     map_array = matrix[index]
    #     probability = random.random()
    #     sum = 0
    #     for i in range(len(map_array)):
    #         sum += map_array[i]
    #         if sum > probability:
    #             return points[i]
    #     return points[-1]
    #
    # for i in cars:
    #     travers_cars.append(traverse(i))
    # return travers_cars

if __name__ == '__main__':
    positionConfusing()