# Class for Prim's
class Vertex:
    def __init__(self,vertex,key = float('inf'),parent = None):
        self.vertex = vertex
        self.key = key
        self.parent = parent
    
    def __str__(self):
        return f"N:{self.vertex}  P:{self.parent}  K:{self.key}"

# Class for Kruskal's
class Node:
    def __init__(self,node,parent = 0,rank = 0):
        self.node = node
        self.parent = parent
        self.rank = rank
    
    def __str__(self):
        return f"N:{self.node}  P:{self.parent}  R:{self.rank}"

# List of Edges in form (u,v,weight)
class EdgeList:
    def __init__(self):
        self.edges = []

    # Add an edge->(u,v) with weight->w as (u,v,w) in the edges list
    def addEdge(self,u,v,w):
        self.edges.append((u,v,w))
    
    # To Sort the edges according to weight -> w in (u,v,w) in the edge list 
    def sortEdges(self):
        for x in range(0,len(self.edges)):
            for y in range(x,len(self.edges)-1):
                if self.edges[x][2] > self.edges[y][2]:
                    self.edges[x],self.edges[y] = self.edges[y],self.edges[x]

    # Overriding __str__ method to return the Edge List 
    def __str__(self):
        s = "\n" + "EDGE LIST\n"
        s += "-"*75 +"\n"
        for edge in self.edges:
            s += str(edge) + '\t'
            if (self.edges.index(edge)+1) % 5 == 0:
                s += "\n\n"
        s += "\n" + "-"*75 +"\n"
        return s

# Graph Class 
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.G = []
        self.E = EdgeList()
        self.V = [x+1 for x in range(self.nodes)]
        for x in range(self.nodes):
            self.G.append([float('inf') for x in range(self.nodes)])
            self.G[x][x] = 0

    # Add an Edge(u,v) that has weight => w in the Graph => G(V,E)
    def addEdge(self,u,v,w):
        if u <= self.nodes and v <= self.nodes:
            self.G[u-1][v-1] = w
            self.G[v-1][u-1] = w
            self.E.addEdge(u,v,w)
            self.E.sortEdges()
        else:
            print("Not a Valid Edge")
        
    # To Get the Adjacent Vertices to the vertex 'u'
    def adjacentVertices(self,u):
        adj = []
        for x in range(self.nodes):
            if self.G[u-1][x] != float('inf') and self.G[u-1][x] != 0:
                adj.append(x+1)   
        
        return adj

    # To Get the weight of a Edge (u,v)
    def weight(self,u,v):
        return self.G[u-1][v-1]

    # Overriding __str__ method to return the Adjacency Matrix 
    def __str__(self):
        s = "\n" +"ADJACENCY MATRIX\n"
        s += "-"*75 +"\n\n"
        s += "\t"
        for x in range(self.nodes):
            s += str(x+1) + "\t"
        s += "\n\n"
        for x in range(self.nodes):
            s += str(x+1) + "\t"
            for y in range(self.nodes):
                s += str((self.G[x][y])) + "\t"
            s += "\n\n"
        s += "-"*75 +"\n"
        return s

from helpers import *

# Helper Functions for Q (a simple Priority Queue)
# To Extract the Minimum from the Queue
def extractMin(Q):
    if Q == []:
        return None
    minimum = Vertex(0)
    for V in Q:
        if V.key < minimum.key:
            minimum = V
    return minimum

# To Check whether a vertex 'v' has a Vertex-Object in Q
def belongs(Q,v):
    for vertex in Q:
        if vertex.vertex == v:
            return True
    return False

# To Get the Vertex Object associated with vertex 'v'
def getVertex(Q,v): 
    for vertex in Q:
        if vertex.vertex == v:
            return vertex
    return None


# Prim's Algortihm that returns the Edges of the Minimum Spanning Tree
def prim(G):
    MST = []
    
    # Creating a Priority Queue
    Q = []
    for V in G.V:
        Q.append(Vertex(V))

    # Setting the First Vertex to Source
    Q[0].key = 0
    while Q != [] :
        # Gettng the Vertex in Q with the Minimum Key Value 
        u = extractMin(Q) 
        
        # Finding all the adjacent vertices of the vertex 'u'
        neighbours = G.adjacentVertices(u.vertex)
        
        # Findig the vertex with the least weight local to 'u' using Greedy Strategy
        for v in neighbours:
            _v = getVertex(Q,v)
            if _v is not None:
                if belongs(Q,v) and (_v.key > G.weight(u.vertex,v)):
                    _v.parent = u.vertex
                    _v.key = G.weight(u.vertex,v)
        Q.remove(u)
        # Getting the edge with the least weight that is not yet been selected
        selectedEdge = extractMin(Q)
        if selectedEdge is not None:
            MST.append((selectedEdge.parent,selectedEdge.vertex,selectedEdge.key))
    
    S = "\n" + "EDGES IN THE MST - (u, v, weight)" + "\n" + "-"*75 + "\n"
    for edge in MST:
        S += str(edge) + "\t"
        if (MST.index(edge)+1) % 5 == 0:
            S += "\n\n"
    S += "\n" + "-"*75
    return S

         
                
def main():
    # creating the graph Object 
    graph = Graph(7)

    # adding edges in the Graph using addEdge() method
    graph.addEdge(1,2,28)
    graph.addEdge(2,3,16)
    graph.addEdge(3,4,12)
    graph.addEdge(4,5,22)
    graph.addEdge(5,6,25)
    graph.addEdge(5,7,24)
    graph.addEdge(6,1,10)
    graph.addEdge(7,2,10)
    graph.addEdge(7,4,18)
    
    # displaying the Adjacency Matrix
    print(graph)   

    # get the MST
    print(prim(graph))

main()