import os,math
def getMAE(method):
    area_width_segments = 5
    area_height_segments = 5
    area_width_split = 5
    area_height_split = 5

    cars_density_file = open(os.path.join(os.getcwd(), 'datas', 'cars_density.txt'), 'r')
    cars_density = eval(cars_density_file.read())

    cars_file = open(os.path.join(os.getcwd(), 'materials', 'cars.txt'), 'r')
    cars = eval(cars_file.read())
    num_cars = len(cars)
    cars_file.close()

    epsilon = [x * 0.1 for x in range(1, 41)]
    cars_MAE_file = open(os.path.join(os.getcwd(), 'datas', 'cars_MAE_file_in_'+str(method)+'.txt'), 'w')
    points_num = 5*5*5*5
    for e in epsilon:
        AE=0
        confusing_cars_file = open(os.path.join(os.getcwd(), 'datas', method,'confusing_cars_density_epsilon'+str(e)+'.txt'), 'r')
        confusing_cars = eval(confusing_cars_file.read())
        confusing_cars_file.close()
        for i in range(area_width_segments):
            for j in range(area_height_segments):
                for x in range(area_width_split):
                    for y in range(area_height_split):
                        AE += abs(cars_density[i][j][x][y] - confusing_cars[i][j][x][y])
        cars_MAE_file.write('MAE_confusing_cars_density_epsilon'+str(e)+':'+str(AE)+'\n')
    cars_MAE_file.close()

if __name__=='__main__':
    methods=['laplace','linprog']
    for method in methods:
        getMAE(method)