import os
import networkx as nx
filename = 'WikiData.txt'
G=nx.DiGraph()
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head,tail)

pr=nx.pagerank(G,alpha=0.85)
x = 0


a=sorted(pr.items(), key=lambda x: x[1], reverse=False)
print(a)