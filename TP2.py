# Graph Using Adjacency List
from sys import stdin
#import time as t

'''
Author       : Arya Fakhruddin Chandra
NPM          : 2006607526
Collaborator : YouTube Videos, 
'''
class Edge:
    def __init__ (self, road, origin, destination, length = 0):
        self.road = road
        self.origin = origin
        self.destination = destination
        self.length = length

class Vertex:
    def __init__(self, city):
        self.city = city

class Graph:
    def __init__(self, vertex):
        self.adj_list = {vertex: [] for vertex in
                         range(vertex)}  # General, structure {Origin : [Type, Destinantion, Weight]}
        self.adj_list0 = {vertex: [] for vertex in range(vertex)}
        self.adj_list1 = {vertex: [] for vertex in range(vertex)}
        self.adj_list01 = {vertex: [] for vertex in range(vertex)}
        # Create Vertex

    def add_edge(self, tipe, origin, destination, weight=0):
        self.adj_list[origin].append([tipe, destination, weight])

        if tipe == 0:
            self.adj_list0[origin].append([destination, weight])
            self.adj_list0[destination].append([origin, weight])

            self.adj_list01[origin].append([tipe, destination, weight])
            self.adj_list01[destination].append([tipe, origin, weight])

            self.adj_list[destination].append([tipe, origin, weight])

        elif tipe == 1:
            self.adj_list1[origin].append([destination, weight])
            self.adj_list1[destination].append([origin, weight])

            self.adj_list01[origin].append([tipe, destination, weight])
            self.adj_list01[destination].append([tipe, origin, weight])

            self.adj_list[destination].append([tipe, origin, weight])

        # elif tipe == 2:
        # self.adj_list[destination].append([tipe, origin, weight])

    def delete_edge(self, tipe, origin, destination):
        temp_origin_list = self.adj_list[origin]
        temp_destination_list = self.adj_list[destination]
        if tipe == 0:
            temp_origin_list0 = self.adj_list0[origin]
            temp_destination_list0 = self.adj_list0[destination]
            temp_destination_list01 = self.adj_list01[destination]
            temp_origin_list01 = self.adj_list01[origin]
            # tipe, deswtinasi, length
            # if x[0] == road and x[1] == dest:
            #
            for x in temp_origin_list0:
                if x[0] == destination:
                    self.adj_list0[origin].remove(x)
                    break

            for y in temp_destination_list0:
                if y[0] == origin:
                    self.adj_list0[destination].remove(y)
                    break

            for z in temp_origin_list:
                if z[0] == 0 and z[1] == destination:
                    self.adj_list[origin].remove(z)
                    break

            for zz in temp_destination_list:
                if zz[0] == 0 and zz[1] == origin:
                    self.adj_list[destination].remove(zz)
                    break

            for xx in temp_destination_list01:
                if xx[0] == 0 and xx[1] == origin:
                    self.adj_list01[destination].remove(xx)
                    break

            for yy in temp_origin_list01:
                if yy[0] == 0 and yy[1] == destination:
                    self.adj_list01[origin].remove(yy)

        if tipe == 1:
            temp_origin_list1 = self.adj_list1[origin]
            temp_destination_list1 = self.adj_list1[destination]

            for x in temp_origin_list1:
                if x[0] == destination:
                    self.adj_list1[origin].remove(x)
                    break

            for y in temp_destination_list1:
                if y[0] == origin:
                    self.adj_list1[destination].remove(y)
                    break

            for z in temp_origin_list:
                if z[0] == 1 and z[1] == destination:
                    self.adj_list[origin].remove(z)
                    break

            for zz in temp_destination_list:
                if zz[0] == 1 and zz[1] == origin:
                    self.adj_list[destination].remove(zz)
                    break

        if tipe == 2:
            for y in temp_origin_list:
                if y[0] == 2 and y[1] == destination:
                    self.adj_list[origin].remove(y)
                    break

    def bfs(self, origin, destination):
        visited = []
        queue = []
        graph = self.adj_list.copy()
        visited.append(origin)
        queue.append(origin)
        lanjut = True

        while queue:
            s = queue.pop(0)

            for x in graph[s]:
                if x[1] not in visited:
                    visited.append(x[1])
                    queue.append(x[1])
                    if x[1] == destination:
                        print('1')
                        lanjut = False
                        break

            if lanjut == True:
                print('0')
                break







    def dijkstra0(self, origin, destination):
        # print('start',origin,destination)
        shortest_distance = {}  # records the length to reach the target vertex
        road_predecessor = {}  # records the road before current vertex
        vertex_unseen = self.adj_list0.copy()
        infinity = 99999999999999
        road = []

        for vertex in vertex_unseen:
            shortest_distance[vertex] = infinity
        shortest_distance[origin] = 0

        while vertex_unseen:

            min_distance_vertex = None

            for vertex in vertex_unseen:

                if min_distance_vertex is None:
                    min_distance_vertex = vertex

                elif shortest_distance[vertex] < shortest_distance[min_distance_vertex]:
                    min_distance_vertex = vertex

            road_option = self.adj_list0[min_distance_vertex]


            for destinasi, panjang in road_option:

                if panjang + shortest_distance[min_distance_vertex] < shortest_distance[destinasi]:
                    shortest_distance[destinasi] = panjang + shortest_distance[min_distance_vertex]

                    road_predecessor[destinasi] = min_distance_vertex

            vertex_unseen.pop(min_distance_vertex)

        currentVertex = destination
        while currentVertex != origin:
            try:
                road.insert(0, currentVertex)
                currentVertex = road_predecessor[currentVertex]

            except KeyError:
                print('-1')
                break

        road.insert(0, origin)
        if shortest_distance[destination] != infinity:
            print(str(shortest_distance[destination]))

        # def dijkstra1(self, origin, destination):
        shortest_distance = {}  # records the length to reach the target vertex
        road_predecessor = {}  # records the road before current vertex
        vertex_unseen = self.adj_list01.copy()
        infinity = 99999999999999
        road = []

    def return_graph(self):
        return self.adj_list

    def return_graph0(self):
        return self.adj_list0

    def return_graph1(self):
        return self.adj_list1

    def return_graph2(self):
        return self.adj_list01

# mulai = t.time()
inPut = stdin.readline().split()
graph = Graph(int(inPut[0]))

for i in range(int(inPut[1])):
    QUERY = stdin.readline().split()
    if QUERY[0] == 'INSERT':
        if QUERY[1] == '0':
            graph.add_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]), int(QUERY[4]))

        elif QUERY[1] == '1':
            graph.add_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]))

        elif QUERY[1] == '2':
            graph.add_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]))

    if QUERY[0] == 'DELETE':
        graph.delete_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]))

    if QUERY[0] == 'SHORTEST_PATH':
        if QUERY[1] == '0':
            graph.dijkstra0(int(QUERY[2]), int(QUERY[3]))

    if QUERY[0] == 'IS_CONNECTED':
        graph.bfs(int(QUERY[1]), int(QUERY[2]))
print('general')
grp = graph.return_graph()
print(grp)
print('-' * 20)
'''stop = t.time()
print(stop-mulai)


print('Type 0')
grp0 = graph.return_graph0()
print(grp0)
print('-' * 20)

print('Type 1')
grp1 = graph.return_graph1()
print(grp1)
print('-' * 20)

print('Type 01')
grp2 = graph.return_graph2()
print(grp2)
print('-' * 20)'''

'''print('General')

'''

###
'''
8 
9
0 1 20
0 6 123
1 3 4
1 2 73
3 7 59
3 5 37
2 4 30
2 5 30
6 7 42


7 6
INSERT 0 1 2 3
INSERT 0 1 3 6
INSERT 0 2 3 1
INSERT 0 3 4 20
INSERT 0 5 6 11
DELETE 0 1 2

General
{0: [], 1: [[0, 3, 6]], 2: [[0, 3, 1]], 3: [[0, 1, 6], [0, 2, 1], [0, 4, 20]], 4: [[0, 3, 20]], 5: [[0, 6, 11]], 6: [[0, 5, 11]]}
--------------------
Type 0
{0: [], 1: [[3, 6]], 2: [[3, 1]], 3: [[1, 6], [2, 1], [4, 20]], 4: [[3, 20]], 5: [[6, 11]], 6: [[5, 11]]}
--------------------
Type 1
{0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
--------------------
Type 2
{0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

7 6
INSERT 0 1 2 3
INSERT 0 1 3 6
INSERT 0 2 3 1
INSERT 0 3 4 20
INSERT 0 5 6 11


7 5
INSERT 0 1 2 3
INSERT 0 1 3 6
INSERT 0 2 3 1
INSERT 0 3 4 20
INSERT 0 5 6 11

7 8
INSERT 0 1 2 3
INSERT 0 1 3 6
INSERT 0 2 3 1
INSERT 0 3 4 20
INSERT 0 5 6 11
SHORTEST_PATH 0 1 2
SHORTEST_PATH 0 1 3
SHORTEST_PATH 0 4 1


7 9
INSERT 0 1 2 3
INSERT 0 1 3 6
INSERT 0 2 3 1
INSERT 0 3 4 20
INSERT 0 4 5 1234
INSERT 0 5 6 11
INSERT 1 4 5
INSERT 1 6 3
DELETE 1 4 5


7 8
INSERT 0 1 2 3
INSERT 0 2 3 4
INSERT 0 3 4 5
INSERT 0 4 5 7
INSERT 0 5 6 2
INSERT 1 1 6
SHORTEST_PATH 0 3 4
SHORTEST_PATH 0 1 6

7 6
INSERT 0 1 2 3
INSERT 0 1 3 6
INSERT 0 2 3 1
INSERT 0 3 4 20
INSERT 0 5 6 11
IS_CONNECTED 4 2


7 8
INSERT 0 1 2 3
INSERT 0 1 3 6
INSERT 0 2 3 1
INSERT 0 3 4 20
INSERT 0 5 6 11
IS_CONNECTED 4 2
IS_CONNECTED 1 5
IS_CONNECTED 0 6

'''
###
