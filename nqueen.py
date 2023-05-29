#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N= int(input("Enter value of N: "))

def printsoln(board):
    for i in range(N):
        for j in range(N):
            print("|",board[i][j],end=" ")
        print("|")    

def issafe(board,row,col):
    for i in range(col):
        if board[row][i]=="Q":
            return False
        
    for i, j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]=="Q":
            return False
        
    for i,j in zip(range(row,N,1,range(col,-1,-1))):
        if board[i][j]=="Q":
            return False
        
    return True


def solveNQUtil(board,col):
    if col>=N:
        return True
    
    for i in range(N):
        if issafe(board,i,col):
            board[i][col]="Q"
            
            if solveNQUtil(board,col+1)==True:
                return True
            
            board[i][col]= " "
            
    return False    


def solveNQ():
    board = [[' ']*N for _ in range(N)]
    
    if solNQUtil(board,0)==False:
        print("No soln exists")
        return False
    
    printsoln(board)
    return True

solveNQ()


# In[ ]:




