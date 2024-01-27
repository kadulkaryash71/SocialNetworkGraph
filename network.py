from get_network import create_graph
import pickle

class Network:
    # all nodes are objects of class Person

    def __init__(self, nwname):
        self.name = nwname
        self.nw = {}

    def add_node(self, from_node, to_node):
        try:
            if from_node not in self.nw.keys():
                self.nw[from_node] = [to_node]
            else:
                self.nw[from_node].append(to_node)
            
            if to_node not in self.nw.keys():
                self.nw[to_node] = [from_node]
            else:
                self.nw[to_node].append(from_node)
            
            self.save_network()
            return True
        
        except Exception as e:
            print("Something went wrong while adding an edge", e)
            return False

    def remove_node(self, node1, node2):
        try:
            self.nw[node1].remove(node2)
            self.nw[node2].remove(node1)

            self.save_network()
            return True
        
        except Exception as e:
            print("Something went wrong while adding an edge", e)
            return False

    def show_network(self):
        create_graph(self.nw)

    def save_network(self):
        f = open(f'serialized/{self.name}.pkl', 'wb')
        pickle.dump(self, f)
        f.close()

        return True

    def __str__(self):
        # print(self.nw)
        # change the return statement to display the whole graph in a matrix/dictionary format
        return str(self.nw)
        # return f"Congratulations! You are in the {self.name} social network."