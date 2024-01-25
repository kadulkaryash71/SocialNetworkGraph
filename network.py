from get_network import create_graph

class Network:
    # all nodes are objects of class Person

    def __init__(self, nwname):
        self.name = nwname
        self.nw = {}

    def add_node(self, from_node, to_node):
        if from_node not in self.nw.keys():
            self.nw[from_node] = [to_node]
        else:
            self.nw[from_node].append(to_node)
        
        if to_node not in self.nw.keys():
            self.nw[to_node] = [from_node]
        else:
            self.nw[to_node].append(from_node)

    def remove_node(self, node1, node2):
        self.nw[node1].remove(node2)
        self.nw[node2].remove(node1)

    def show_network(self):
        create_graph(self.nw)

    def __str__(self):
        # print(self.nw)
        # change the return statement to display the whole graph in a matrix/dictionary format
        return str(self.nw)
        # return f"Congratulations! You are in the {self.name} social network."