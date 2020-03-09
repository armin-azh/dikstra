import networkx as nx
import numpy as np

MAXIMUM_TIME=100
NUMBER_OF_STATIONS=107


class Station:
    def __init__(self,name,delay,id):
        self.name=name
        self.delay=delay
        self.id=id
    def __str__(self):
        return 'name {}'.format(self.name)

def station(file_path):
    try:
        f=open(file_path,'r')
        line=f.readline()
        stations=dict()
        while line:
            temp = line.split()
            stations[temp[1]]=Station(temp[0],temp[2],temp[1])
            line=f.readline()

        return stations
    finally:
        f.close()


def adjusment_matrix():
    graph=nx.Graph()
    line1=station('substations/line1.txt')
    keys1=line1.keys()
    ls=list()
    for item in keys1:
        ls.append(item)
    for item in zip(ls[:len(ls)-2],ls[1:]):
        graph.add_edge(int(item[0]),int(item[1]),weight=line1[item[0]].delay)

    line2=station('substations/line2.txt')
    keys2=line2.keys()
    ls=list()
    for item in keys2:
        ls.append(item)
    for item in zip(ls[:len(ls)-2],ls[1:]):
        graph.add_edge(int(item[0]), int(item[1]), weight=line2[item[0]].delay)


    line3=station('substations/line3.txt')
    keys3=line3.keys()
    ls=list()
    for item in keys3:
        ls.append(item)
    for item in zip(ls[:len(ls)-2],ls[1:]):
        graph.add_edge(int(item[0]), int(item[1]), weight=line3[item[0]].delay)

    line4=station('substations/line4.txt')
    keys4=line4.keys()
    ls=list()
    for item in keys4:
        ls.append(item)
    for item in zip(ls[:len(ls)-2],ls[1:]):
        graph.add_edge(int(item[0]), int(item[1]), weight=line4[item[0]].delay)

    line5=station('substations/line5.txt')
    keys5=line5.keys()
    ls=list()
    for item in keys5:
        ls.append(item)
    for item in zip(ls[:len(ls)-2],ls[1:]):
        graph.add_edge(int(item[0]), int(item[1]), weight=line5[item[0]].delay)

    line6=station('substations/line6.txt')
    keys6=line6.keys()
    ls=list()
    for item in keys6:
        ls.append(item)
    for item in zip(ls[:len(ls)-2],ls[1:]):
        graph.add_edge(int(item[0]), int(item[1]), weight=line6[item[0]].delay)

    line7=station('substations/line7.txt')
    keys7=line7.keys()
    ls=list()
    for item in keys7:
        ls.append(item)
    for item in zip(ls[:len(ls)-2],ls[1:]):
        graph.add_edge(int(item[0]), int(item[1]), weight=line7[item[0]].delay)

    adjMatrix=np.zeros((NUMBER_OF_STATIONS,NUMBER_OF_STATIONS))
    for i in range(NUMBER_OF_STATIONS):
        for j in range(NUMBER_OF_STATIONS):
            if i == j :
                adjMatrix[i][j] = 0
            else:
                adjMatrix[i][j]=MAXIMUM_TIME

    for item in graph.edges.data():
        adjMatrix[item[0]][item[1]]=item[2]['weight']
        adjMatrix[item[1]][item[0]] = item[2]['weight']

    return adjMatrix


def get_station_names():
    line1 = station('substations/line1.txt'),
    line2 = station('substations/line2.txt'),
    line3 = station('substations/line3.txt'),
    line4 = station('substations/line4.txt'),
    line5 = station('substations/line5.txt'),
    line6 = station('substations/line6.txt'),
    line7 = station('substations/line7.txt'),
    lines=[line1,line2,line3,line4,line5,line6,line7]
    stations=dict()
    for line in lines:
        keys=line[0].keys()
        for key in keys:
            stations[key]=line[0][key].name

    print(stations)

