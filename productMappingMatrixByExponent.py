import random,math,os

def distance_of_two_point(x, y, ndigits=2):
    return round(math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2)), ndigits)
def productMappingMatrix(area_width_segments,area_height_segments,area_width_split,area_height_split,epsilon):
    expo_file = open(os.path.join(os.getcwd(), 'datas', 'exponent', 'exponent' + str(epsilon) + '.txt'), 'w')
    map_width = 0.25
    map_height = 0.25
    area_width = map_width / area_width_segments
    area_height = map_height / area_height_segments
    split_width = area_width / area_width_split
    split_height = area_height / area_height_split
    mapping_array=[]
    for x in range(area_width_split*area_height_split):
        mapping_array.append([])
        for i in range(area_width_split):
            for j in range(area_height_split):
                max_distance = math.sqrt(2)*area_width
                point_A = [x%area_width_split*split_width,x/area_width_split*split_height]
                point_B = [split_width*i,split_height*j]
                mapping_array[len(mapping_array)-1].append(math.pow(math.e,epsilon*(max_distance-distance_of_two_point(point_A,point_B))/(2*max_distance*math.sqrt(2))))
        sum=0
        for tmp in mapping_array[len(mapping_array)-1]:
            sum+=tmp
        for index in range(area_width_split*area_height_split):
            mapping_array[len(mapping_array)-1][index] = round(mapping_array[len(mapping_array)-1][index]/sum,5)
    expo_file.write(str(mapping_array))

if __name__ == '__main__':
    epsilon = [x * 0.1 for x in range(1, 41)]
    for i in epsilon:
        productMappingMatrix(5, 5, 5, 5, i)