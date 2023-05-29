#!/usr/bin/env python
# coding: utf-8

# In[13]:


graph=[]
V=5

def add_edge(u,v,w):
    graph.append([u,v,w])
    
def find(parent,i):
    if parent[i] != i:
        parent[i]=find(parent,parent[i])
        
    return parent[i]

def union(parent,rank,x,y):
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1
        

def kruskal():
    result=[]
    rank=[]
    parent=[]
    i=0
    e=0
    
    graph.sort(key=lambda item : item[2])
    
    for node in range(V):
        parent.append(node)
        rank.append(0)
        
    while e<(V-1):
        u,v,w=graph[i]
        i=i+1
        x=find(parent,u)
        y=find(parent,v)
        
        if x!=y:
            e= e+1
            result.append([u,v,w])
            union(parent,rank,x,y)
            
            
    
    min_cost=0
    
    for u,v,w in result:
        min_cost+=w
        
        print(str(u) + "-" + str(v) + " : " + str(w))
        
    print("\nmin_cost = " ,min_cost)
    
    print("\nGraph : ")
    
 
add_edge(0,1,1)
add_edge(0,2,5)
add_edge(0,3,6)
add_edge(1,2,2)
add_edge(1,4,8)
add_edge(2,3,3)
add_edge(2,4,7)
add_edge(3,4,4)


kruskal()
print(graph)


        


# In[ ]:





# In[ ]:





# In[ ]:




