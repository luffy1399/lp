#!/usr/bin/env python
# coding: utf-8

# In[4]:


graph={
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []     
}

visited =set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            

print("DFS :")
dfs(visited,graph,'5')
            


# In[6]:


graph={
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []     
}


visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m)
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                

print("BFS :")
bfs(visited,graph,'5')


# In[ ]:




