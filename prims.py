#!/usr/bin/env python
# coding: utf-8

# In[5]:


INF=999999
V=5

G=[[0,1,5,6,0],
   [1,0,2,0,8],
   [5,2,0,3,7],
   [6,0,3,0,4],
   [0,8,7,4,0]]

selected_node = [0] * V
selected_node[0] = True
e=0

while e<(V-1):
    min=INF
    a=0
    b=0
    
    for i in range(V):
        if selected_node[i]:
            for j in range(V):
                if not selected_node[j] and G[i][j]:
                    if min>G[i][j]:
                        min=G[i][j]
                        a=i
                        b=j
    
    
    e+=1
    selected_node[b]=True
    print(str(a) + "-" + str(b) + " : " + str(G[a][b]))
    
                


# In[ ]:




