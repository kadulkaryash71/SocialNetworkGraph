import networkx as nx
import matplotlib.pyplot as plt

def create_graph(network_dict):
    G = nx.DiGraph()

    for user in network_dict.keys():
        G.add_node(user)
        for friend in network_dict[user]:
            G.add_node(friend)
            G.add_edge(user, friend)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=10000, font_weight='bold')
    plt.show()

    return True
