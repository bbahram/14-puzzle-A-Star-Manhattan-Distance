from copy import deepcopy


class Node: # node class
    graf=[]
    parent=None
    h2=0




def GrafSearch(): #the main function to search the nodes and check them
    mainInit=None
    i=0
    while True:
        if frontier==[]:
            break
        
        i=AStar()
        mainInit=frontier[i]
        tempGraf=mainInit.graf

        del frontier[i]
        
        if tempGraf==goal:
            break
        explored.append(tempGraf)
        
        AddToFrontier(mainInit)
    

    moves=0
    while mainInit.parent!=None:
        for i in range(4):
            print(mainInit.graf[i][:])
        print(mainInit.h2)
        print("--------------------------------------------------------------")
        mainInit=mainInit.parent
        moves=moves+1
    print("first base:")
    for i in range(4):
            print(mainInit.graf[i][:])
    
    print("explored: " , len(explored))
    print("frontier: " , len(frontier))
    print("Moves: ", moves)


def AddToFrontier(node): #creates new matrises and put them in frontier
    tempGrid=node.graf
    location=FindSpace(tempGrid)
    k=0
    while k<len(location):
        i= -1
        while i<2:
            j=-1
            tempi=i+location[k][0]
            while j<2:
                tempj=j+location[k][1]
                if ((j!=0 or i!=0) and (tempi>=0 and tempi<len(tempGrid)) 
                    and (tempj>=0 and tempj<len(tempGrid)) 
                    and (tempGrid[tempi][tempj]!=0) and (i+j==-1 or i+j==1)):
                    newGrid=deepcopy(tempGrid)
                    newGrid[location[k][0]][location[k][1]], newGrid[tempi][tempj]= newGrid[tempi][tempj], newGrid[location[k][0]][location[k][1]]

                    checker= newGrid in explored
                    
                    if checker==False:
                        for search in frontier:
                            if(search.graf==newGrid):
                                checker=True
                                break   

                    if(checker==False):
                        newNode=Node()
                        newNode.parent=node
                        newNode.graf=newGrid
                        newNode.h2=CalculateManhattanDistance(newGrid)
                        frontier.append(newNode)
                j=j+1
            i=i+1
        k=k+1






def FindSpace(graf): # finds the two empty spaces in matrix
    x=[]
    for i in range(4):
        for j in range(4):
            if(graf[i][j]==0):
                x.append([i, j])
                if(len(x)==2):
                    return x

def Find(n):
    global goal
    x=[]
    for i in range(4):
        for j in range(4):
            if(n==goal[i][j]):
                x.append(i)
                x.append(j)
                return x

def CalculateManhattanDistance(matrix):
    global goal
    H=[]
    sum=0
    for i in range(4):
        for j in range(4):
            temp=matrix[i][j]
            temp=Find(temp)
            sum=sum+abs(i-temp[0])+abs(j-temp[1])
    return sum



    return sum

def AStar():
    global frontier
    min=100
    mini=0
    i=0
    while i < len(frontier):
        if(frontier[i].h2 < min):
            min=frontier[i].h2
            mini=i
        i=i+1
    return mini



goal=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 0]]

intitial =[[0, 0, 3, 2], [1, 5, 10, 4], [9, 6, 8, 7], [13, 14, 11, 12]]

#[[0,1,0,2],[3,4,5,6],[7,8,9,10],[11,12,13,14]]
#[[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 0, 10], [11, 12, 13, 14]]

frontier=[]
explored=[]

init=Node()
init.graf=intitial
init.h2=CalculateManhattanDistance(init.graf)
frontier.append(init)
GrafSearch()
