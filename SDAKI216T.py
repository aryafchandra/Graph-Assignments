# Graph Using Adjacency List
from sys import stdin
from collections import deque
import heapq

'''
Author       : Arya Fakhruddin Chandra
NPM          : 2006607526
Collaborator : YouTube Videos, Anastasia Audi 
'''


class Graph:
    def __init__(self, vertex):
        self.adj_list = {vertex: [] for vertex in
                         range(vertex)}  # General, structure {Origin : [Type, Destinantion, Weight]}
        self.adj_list0 = {vertex: [] for vertex in range(vertex)}
        self.adj_list1 = {vertex: [] for vertex in range(vertex)}
        self.adj_list2 = {vertex: [] for vertex in range(vertex)}
        # Create Vertex

    def add_edge(self, tipe, origin, destination, weight=0):
        self.adj_list[origin].append([tipe, destination, weight])

        if tipe == 0:
            self.adj_list0[origin].append([destination, weight])
            self.adj_list0[destination].append([origin, weight])

            self.adj_list[destination].append([tipe, origin, weight])

        elif tipe == 1:
            self.adj_list1[origin].append([destination, weight])
            self.adj_list1[destination].append([origin, weight])

            self.adj_list[destination].append([tipe, origin, weight])

        elif tipe == 2:
            self.adj_list2[origin].append([destination])

    def delete_edge(self, tipe, origin, destination):
        temp_origin_list = self.adj_list[origin]
        temp_destination_list = self.adj_list[destination]
        if tipe == 0:
            temp_origin_list0 = self.adj_list0[origin]
            temp_destination_list0 = self.adj_list0[destination]
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
            temp_adjlis2 = self.adj_list2
            for aa in temp_adjlis2:
                if aa[0] == destination:
                    self.adj_list2[origin].remove(aa)
                    break

            for y in temp_origin_list:
                if y[0] == 2 and y[1] == destination:
                    self.adj_list[origin].remove(y)
                    break

    def is_connected(self, origin, destination):
        visited = []
        queue = []
        graph = self.adj_list
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
                        print(1)
                        lanjut = False
                        break

        if lanjut == True:
            print(0)

    def min_path(self, origin, destination):
        graph = self.adj_list0
        distance = {origin: 0}
        queue = deque([origin])

        while queue:
            u = queue.popleft()
            d = distance[u] + 1
            for i in graph[u]:
                if i[0] not in distance:
                    if i[0] == destination:
                        return d
                    distance[i[0]] = d
                    queue.append(i[0])
        return -1

    def count_city(self, origin, distance):
        shortest_distance = {}  # records the length to reach the target vertex
        road_predecessor = {}  # records the road before current vertex
        vertex_unseen = self.adj_list0.copy()
        infinity = 99999999999999

        totalcity = 0
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
        for x in shortest_distance:
            if shortest_distance[x] <= distance:
                totalcity += 1
        return totalcity

    def count_connected(self):
        visited = []
        queue = []
        count = []
        graph = self.adj_list0

        for i in range(len(graph)):
            if i in visited:
                continue
            else:
                visited.append(i)
            count.append(i)
            queue.append(i)

            while queue:
                s = queue.pop(0)

                for x in graph[s]:
                    if x[0] not in visited:
                        visited.append(x[0])
                        queue.append(x[0])

        return len(count)

    def dijkstra0(self, origin, destination):
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

            road_option = self.adj_list0[min_distance_vertex].copy()

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
                return -1

        road.insert(0, origin)
        if shortest_distance[destination] != infinity:
            return shortest_distance[destination]

    def simulate_walk(self, origin, distance):
        graph = self.adj_list2
        now = origin
        walk = 0
        visited = []
        visited.append(origin)
        lanjut = True

        while lanjut:
            for i in graph[now]:
                if walk != distance:
                    walk += 1
                    visited.append(i[0])
                    if i[0] == origin:
                        return visited[distance % (len(visited) - 1)]
                now = i[0]
            if len(i) == 0:
                return now

    def return_graph(self):
        return self.adj_list

    def return_graph0(self):
        return self.adj_list0

    def return_graph1(self):
        return self.adj_list1

    def return_graph2(self):
        return self.adj_list2


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
            print(graph.dijkstra0(int(QUERY[2]), int(QUERY[3])))
        if QUERY[1] == '1':
            print('belum [DJIKSTRA1]')
    if QUERY[0] == 'IS_CONNECTED':
        graph.is_connected(int(QUERY[1]), int(QUERY[2]))
    if QUERY[0] == 'MIN_PATH':
        print(graph.min_path(int(QUERY[1]), int(QUERY[2])))
    if QUERY[0] == 'COUNT_CITY':
        print(graph.count_city(int(QUERY[1]), int(QUERY[2])))
    if QUERY[0] == 'COUNT_CONNECTED':
        print(graph.count_connected())
    if QUERY[0] == 'SIMULATE_WALK':
        print(graph.simulate_walk(int(QUERY[1]), int(QUERY[2])))
