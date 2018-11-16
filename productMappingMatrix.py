import os,math,numpy as np
from scipy.optimize import linprog

#width,height denotes the map's width and height
#segments denotes the segments we want to split

class AdjacentNode:  # link node
    def __init__(self, index, distance=float('Inf'), next_adjacent=None):
        self.index = index
        self.distance = distance
        self.next_adjacent = next_adjacent

    def get_next_adjacent(self):
        return self.next_adjacent


class GraphNode:  # node of graph which has elements:index,adjacent_node(link list)
    def __init__(self, index=-1, adjacent_node=None):
        self.index = index
        self.adjacent_node = adjacent_node

    def set_index(self, index):
        self.index = index

    def add_adjacent_node(self, adjacent_node):
        tmp_node = self.adjacent_node
        if tmp_node == None:  # if ths node don't have adjacent node
            self.adjacent_node = adjacent_node
        else:
            while tmp_node.next_adjacent != None:
                tmp_node = tmp_node.next_adjacent
            tmp_node.next_adjacent = adjacent_node

    def get_first_adjacent_nodes(self):
        return self.adjacent_node

def minpath(points_shortest_array, index, graph):  # the shortest path of node of index
    v = []  # the points that have determined the distance
    dist = [float('Inf') for i in graph]
    min_v = index
    dist[index] = 0
    while (len(v) < len(dist)):
        v.append(min_v)
        tmp_adjacent = graph[min_v].adjacent_node  # get the adjacent node of point of min_v
        while tmp_adjacent != None:
            if dist[min_v] + tmp_adjacent.distance < dist[tmp_adjacent.index]:
                dist[tmp_adjacent.index] = dist[min_v] + tmp_adjacent.distance
            tmp_adjacent = tmp_adjacent.next_adjacent
        min_dist = float('Inf')
        for i in range(len(dist)):
            if i in v:
                continue
            if (dist[i] < min_dist):
                min_v = i
                min_dist = dist[i]
    for i in range(len(dist)):
        points_shortest_array[index, i] = dist[i]

def dist_of_points(i, j):  # distance of two points
    return round(math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2), 2)

def product_sort_edges(points):
    def cmp(x, y):
        if x['distance'] - y['distance'] <= 0:
            return -1
        else:
            return 1
    sort_edges_file = open(os.path.join(os.getcwd(),'datas', 'sort_edges.txt'), 'w')
    sorted_edges = []
    num_of_points = len(points)  # number of points
    for i in range(num_of_points):
        j = i
        while j < num_of_points:
            sorted_edges.append({'pointA': i, 'pointB': j, 'distance': dist_of_points(points[i], points[j])})
            j = j + 1
    sorted_edges.sort(cmp)
    sort_edges_file.write(str(sorted_edges))
    sort_edges_file.close()
    return sorted_edges

def productMappingMatrix(width,height,width_segments,height_segments,epsilon,delta):
    #product points
    segmentWidth = round(float(width)/width_segments,2) #the length of each split segments in x direction
    segmentHeight = round(float(height)/height_segments,2) #the length of each split segments in y direction
    x_array=[]
    y_array=[]
    for i in range(0,height_segments):
        x_array.append(i*segmentHeight+segmentHeight/2)
    for j in range(0,width_segments):
        y_array.append(j*segmentWidth+segmentWidth/2)
    position_set=[] # store all points
    for i in range(0,height_segments):
        for j in range(0,width_segments):
            position_set.append([x_array[i],y_array[j]])
    #product delta spanner graph
    sort_edges = product_sort_edges(position_set) #product sorted edges in a file
    num_of_points = len(position_set)  # number of points
    delta_spanner_edges = np.zeros((num_of_points, num_of_points))
    delta_spanner_edges[delta_spanner_edges == 0] = float('Inf')  # initialize all path to -1 which equal to infinity
    points_shortest_array = np.zeros((num_of_points, num_of_points))
    points_shortest_array[points_shortest_array == 0] = float('Inf')  # initialize all path to -1 which equal to infinity
    graph = []  # adjacent table that store structure of points
    for index in range(num_of_points):
        tmp_point = GraphNode(index)
        graph.append(tmp_point)
    for i in range(len(graph)):
        minpath(points_shortest_array, i, graph)
    for i in sort_edges:
        if points_shortest_array[i['pointA'], i['pointB']] > i['distance'] * delta:
            tmp_adj_nodeA = AdjacentNode(i['pointB'], i['distance'])
            tmp_adj_nodeB = AdjacentNode(i['pointA'], i['distance'])
            graph[i['pointA']].add_adjacent_node(tmp_adj_nodeA)
            graph[i['pointB']].add_adjacent_node(tmp_adj_nodeB)
            delta_spanner_edges[i['pointA'], i['pointB']] = 1
            delta_spanner_edges[i['pointB'], i['pointA']] = 1
        for j in range(len(graph)):
            minpath(points_shortest_array, j, graph)
    np.save(os.path.join(os.getcwd(), 'datas', 'delta_spanner.npy'), delta_spanner_edges)
    #product mapping matrix
    numbers_of_various = num_of_points*num_of_points
    c = [0] * numbers_of_various
    ratio = math.pow(math.e, epsilon / delta)
    for i in range(num_of_points):
        for j in range(num_of_points):
            c[i * num_of_points + j] = dist_of_points(position_set[i], position_set[j])
    a_ub = []
    b_ub = []
    a_eq = []
    b_eq = []
    r = []
    # product the a_ub and b_ub
    for i in range(num_of_points):
        for j in range(num_of_points):
            if delta_spanner_edges[i, j] == 1:
                for k in range(num_of_points):
                    tmp_a = [0] * numbers_of_various
                    tmp_a[i * num_of_points + k] = 1
                    tmp_a[j * num_of_points + k] = -math.pow(ratio, dist_of_points(position_set[i], position_set[j]))
                    a_ub.append(tmp_a)
                    b_ub = b_ub + [0]
    # product the a_eq and b_eq
    for i in range(num_of_points):
        tmp_a = []
        for j in range(num_of_points):
            if i == j:
                tmp_a = tmp_a + [1] * num_of_points
            else:
                tmp_a = tmp_a + [0] * num_of_points
        a_eq.append(tmp_a)
        b_eq = b_eq + [1]
    for i in range(numbers_of_various):
        r.append((0, 1))
    len_a_ub = len(a_ub)
    np_a_ub = np.zeros((len_a_ub, numbers_of_various))
    for i in range(len_a_ub):
        for j in range(numbers_of_various):
            np_a_ub[i, j] = a_ub[i][j]
    len_a_eq = len(a_eq)
    np_a_eq = np.zeros((len_a_eq, numbers_of_various))
    for i in range(len_a_eq):
        for j in range(numbers_of_various):
            np_a_eq[i, j] = a_eq[i][j]
    res = linprog(c, np_a_ub, b_ub, np_a_eq, b_eq, bounds=tuple(r),method='interior-point',options={'maxiter':500})
    result = np.zeros((num_of_points, num_of_points))
    linpro_file = open(os.path.join(os.getcwd(), 'datas', 'linprog' + str(epsilon) + '.txt'), 'w')
    def fuzhi2result(result, result_index, linprog_result, lingpro_index):
        for i in range(num_of_points):
            result[result_index, i] = linprog_result[lingpro_index * num_of_points + i]
    linprog_result = res.x.tolist()
    print linprog_result
    linprog_index = -1
    for i in position_set:
        linprog_index += 1
        result_index = -1
        for j in position_set:
            result_index += 1
            if i == j:
                fuzhi2result(result, result_index, linprog_result, linprog_index)
    result_buffer = []
    for i in range(num_of_points):
        result_buffer_tmp = [0] * num_of_points
        for j in range(num_of_points):
            if (result[i, j] <= 1e-5):
                result_buffer_tmp[j] = 0
            else:
                result_buffer_tmp[j] = round(result[i, j], 5)
        result_buffer.append(result_buffer_tmp)
    linpro_file.write(str(result_buffer))
    linpro_file.close()

if __name__ == '__main__':
    epsilon=[x*0.1 for x in range(1,21)]
    for i in epsilon:
    	productMappingMatrix(5,5,5,5,i,1.5)
