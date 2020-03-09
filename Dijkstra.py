from sys import maxsize as infinit

initial=[
    [0,7,4,6,1],
    [infinit,0,infinit,infinit,infinit],
    [infinit,2,0,5,infinit],
    [infinit,3,infinit,0,infinit],
    [infinit,infinit,infinit,1,0]
]

def find_origins(origin,visited=[]):
    indexes=list()
    for x in visited:
        if x==origin:
            indexes.append(x)

    return indexes


def map(origin,verticles,distination,visited=[],pathOrder=[]):
    if distination not in pathOrder:
        return ValueError('There is no path to the Distination...')
    else:
        indexes=find_origins(origin,visited)
        finalPath=None
        for index in indexes:
            i=index
            path = [index,]
            found = None
            global again
            again=True
            while again:
                valueTemp=pathOrder[i]
                if valueTemp==distination:
                    path.append(valueTemp)
                    again=False
                    found=True
                    break
                else:
                    indexTemp2=visited.index(valueTemp)
                    i=indexTemp2
                    path.append(visited[i])

            if found:
                finalPath=path
                break

        return finalPath

def djkstar(verticles,weights,origin,destination):

    visitedVerticles=[0 for i in range(verticles)]  #The virticle that have been saw
    lengthOfVerticles=[0 for i in range(verticles)]  #Minimum destanse of each verticle from start node
    Finall=[]
    pathOrder=[]
    for i in range(verticles):
        if i != origin:
            visitedVerticles[i]=origin
            lengthOfVerticles[i]=weights[origin][i]
    for i in range(verticles-1):
        min=infinit
        for j in range(verticles):
            if j!= origin:
                if 0<=lengthOfVerticles[j] and lengthOfVerticles[j]<min:
                    min=lengthOfVerticles[j]
                    nearVerticle=j
        e=visitedVerticles[nearVerticle]
        Finall.append((e,nearVerticle))
        pathOrder.append(nearVerticle)
        for j in range(verticles):
            if j != origin:
                if lengthOfVerticles[nearVerticle]+weights[nearVerticle][j]<lengthOfVerticles[j]:
                    lengthOfVerticles[j]=lengthOfVerticles[nearVerticle]+weights[nearVerticle][j]
                    visitedVerticles[j]=nearVerticle
        lengthOfVerticles[nearVerticle]=-1


    return Finall








