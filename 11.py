
import warnings
warnings.filterwarnings('ignore')
import networkx as nx
import matplotlib.pyplot as plt

class edge():
    def __init__(self, s: str, t: str, weight:float):
        self.s = s
        self.t = t
        self.weight = weight
    def __str__(self):
        return "{} -({})-> {}".format(self.s,self.weight,self.t)
    def __lt__(self, other):
    
        return self.weight < other.weight
class node():
    def __init__(self, name: str):
        """
        - node has a name (str)
        - DIFFERENTLY neighbors is the list of edge objects
        """
        self.name = name
        self.neighbors = [] # list of edge objects !!
    def neighbors_name(self) -> list:
        """
        info about neighbors names (returns list of strings)
        """
        return [(e.s, e.t, e.weight) for e in self.neighbors]

class weightedGraph():
    def __init__(self, elist: list):
        """
        self.nodes is a dictionary
        key : node name
        value : node object
        """
        self.elist = elist
        self.node_names = list(set([s for s, t, w in elist] + [t for s,t,w
        in elist]))
        self.nodes = {s:node(s) for s in self.node_names}
        self.create_graph()
    def add_edge(self, e:edge):
        """undirected Edge"""
        self.nodes[e.s].neighbors.append(e)
        self.nodes[e.t].neighbors.append(e)
    def create_graph(self):
        for s,t,w in self.elist:
            e = edge(s,t,w)
            self.add_edge(e)
    def info(self) -> dict:
        return {s:node_s.neighbors_name() for s,node_s in self.nodes.items()}
    def draw(self, color = 'orange'):
        """
        Usage of networkx for visualisation
        """
        G = nx.Graph()
        G.add_weighted_edges_from(self.elist)
        plt.figure(figsize=(10,5))
        pos = nx.spring_layout(G) # positions for all nodes
        nx.draw(G, pos, node_size=2000, node_color=color, font_size=40, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, font_size=20, edge_labels =
        nx.get_edge_attributes(G,'weight'))
        
        
from heapq import *

class LazyPrimMST():
    def __init__(self, G:weightedGraph):
        self.G = G
        self.marked = {node_name: False for node_name in self.G.node_names
        } # MST vertices
        self.mst = [] # MST edges
        self.pq = [] # Priority Queue of edges
        self.visit(self.G.node_names[0])
        while self.pq:
            weight, e = heappop(self.pq)
            if self.marked[e.s] and self.marked[e.t]: continue
            self.mst.append(e)
            if not self.marked[e.s]: self.visit(e.s)
            if not self.marked[e.t]: self.visit(e.t)
    def visit(self, v: str):
        self.marked[v] = True
        for e in self.G.nodes[v].neighbors:
            s, t, weight = e.s, e.t, e.weight
            if not self.marked[s]: heappush(self.pq, (weight, e))
            if not self.marked[t]: heappush(self.pq, (weight, e))
    def display(self):
        return [(e.s, e.t, e.weight) for e in self.mst]    


"""QUESTION 0"""

elist = [('A', 'B', 5), ('A', 'H', 37), ('A', 'E', 25), ('A', 'G', 36), ('A', 'C', 3), ('H', 'G', 8),('C', 'D', 11), ('C', 'B', 2), ('D', 'F', 5),('D', 'E', 4),('E', 'F', 5)]
G = weightedGraph(elist)
G.draw() 


"""QUESTION 1"""

MST = LazyPrimMST(G)
print(MST.display())   

"""QUESTION 2"""

MST.mst.sort()
print(MST.display())
MST.mst.remove(MST.mst[-1])
print(MST.display())
MST.mst.remove(MST.mst[-1])
print(MST.display())

"""QUESTION 3"""


class KClusting:
    def __init__ (self,numberOfCluster,MST:LazyPrimMST):
        MST.mst.sort()
        for i in range (numberOfCluster - 1):
            MST.mst.remove(MST.mst[-1])
        print(MST.display())
k = KClusting(2,MST)
[('C', 'B', 2),('A', 'C', 3),('D', 'E', 4),('E', 'F', 5)]

"""QUESTION 4"""

class EagerPrimMST():
    pass


"""QUESTION 5"""

class KClustingEager:
    def __init__ (self,numberOfCluster,MST:EagerPrimMST):
        MST.mst.sort()
        for i in range (numberOfCluster - 1):
            MST.mst.remove(MST.mst[-1]) 
            
        print(MST.display())    
                 
            