from Dijkstar.Dijkstra import djkstar
from Dijkstar.utils import adjusment_matrix,NUMBER_OF_STATIONS


weightMatrix=adjusment_matrix() # Giving the Stations adjasment matrix

if __name__ == '__main__':
    print(djkstar(NUMBER_OF_STATIONS,adjusment_matrix(),0,75))