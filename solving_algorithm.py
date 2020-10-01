from collections import defaultdict
import heapq
import time
import networkx as nx

def mst_weight(tree, originGraph):
    weight = 0
    for origin in tree:
        for target in tree[origin]:
            weight = weight + originGraph[origin][target]
    return weight

def prim(graph):
    starting_vertex = list(graph)[0]
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

def complete_prim_algorithm(listaDeAdjacencia):
    mst = prim(listaDeAdjacencia)
    return mst_weight(mst, listaDeAdjacencia)

def create_nx_graph(nodes_list):
	Graph = nx.Graph()
	for node in nodes_list:
		Graph.add_edge(node[0], node[1], weight=node[2])
	return Graph
		
def mst_prim_visualization(graph):
	mst = nx.minimum_spanning_tree(graph, algorithm='prim')
	return mst