#!/usr/bin/env python
# coding: utf-8

# In[11]:


import heapq
INF= 9999999


def dijkstra(graph,source):
    Q=set()
    dist={}
    
    for vertex in graph:
        dist[vertex]=INF
        Q.add(vertex)
    dist[source]=0
    
    while Q:
        u = min(Q,key=lambda v:dist[v])
        Q.remove(u)
        
        for v in graph[u]:
            cost_uv=graph[u][v]
            if dist[u] + cost_uv <dist[v]:
                dist[v]=dist[u] + cost_uv
                
    return dist
    
    
graph={
        'A' : {'B':2,'C':4},
        'B' : {'A':2,'C':1,'D':5,'E':10},
        'C' : {'A':4,'B':1,'D':3,'E':5},
        'D' : {'B':5,'C':3,'E':3},
        'E' : {'B':10,'C':5,'D':3}
    }
    
source='A'
    
shortest_dist = dijkstra(graph,source)
    
for node,distance in shortest_dist.items():
    
    print("Dist from " + source + " to " + node + " : " + str(distance))
        
    
   
  
            


# In[ ]:




