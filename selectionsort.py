#!/usr/bin/env python
# coding: utf-8

# In[1]:


def selection_sort(arr,size):
    
    for ind in range(size-1):
        min=ind
        for j in range(ind+1,size):
            if arr[j]<arr[min]:
                min=j
            
        (arr[ind],arr[min]) = (arr[min],arr[ind])    



arr=[-5,-1,4,-30,30,20,1,1,5]
size=len(arr)

print("before sort : ",arr )
selection_sort(arr,size)

print("after sort : ",arr)


# In[ ]:




