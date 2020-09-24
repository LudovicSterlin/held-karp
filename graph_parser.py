"""A parser that transform data in tspXX.txt file into nx.Graph for TSP problem"""

import sys
from math import sqrt

import networkx as nx


class Point:
    def __init__(self, tup):
        self.x = tup[0]
        self.y = tup[1]

    def __repr__(self):
        return f"Point({self.x:.1f},{self.y:.1f})"

def distance(a, b):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2)

def file_to_points(filename):
    nb_node = 0
    points = []

    with open(filename) as data_file:
        nb = 0
        # first line is total number of vertices in file
        nb_node = int(data_file.readline())
        # print(f"expected number of vertices : {nb_node}")

        for line in data_file:
            points.append(Point(tuple(float(x) for x in line.split())))
            # print(f"reading point {nb}: {points[nb]}")
            nb = nb + 1
        # print(f"\nnumber of vertices found: {nb} \n")

        if nb_node != nb:
            AssertionError("Number of vertices found is different from expected")
        
        return points

def file_to_graph(filename):
    """"Read and parse a .txt file and return a nx.Graph generated from the data

    Args:
        filename (str): The path to the .txt file containing the data on the cities

    Returns:
        (nx.Graph, Points[]): The graph generated from the .txt file, The list of points found in the .txt file
    """
    print(f"\nExtracting graph from {filename} ...")
    points = file_to_points(filename)
    print(f"Found: {len(points)} points")
    print(f"Points: \n{points}\n")

    # Create graph
    g = nx.Graph()

    # Compute and add all the edges
    n = len(points)
    for i in range(n):
        for j in range(1,n):
            weight = distance(points[i], points[j])
            g.add_edge(i,j, weight=weight)

    # return g
    return (g, points)
