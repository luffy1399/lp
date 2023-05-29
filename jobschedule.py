#!/usr/bin/env python
# coding: utf-8

# In[4]:


def job_schedule(arr,t):
    size = len(arr)
    
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j][2] < arr[j+1][2]:
                (arr[j],arr[j+1]) = (arr[j+1],arr[j])
                
    
    jobs= [-1]*t
    for i in range(size):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if jobs[j]==-1:
                jobs[j]= arr[i][0]
                break
    
    print(jobs)



arr = [['a', 2, 100],
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

job_schedule(arr,3)


# In[ ]:




