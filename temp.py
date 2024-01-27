import pickle
from get_network import create_graph

state_file = open('serialized/obj_1.pkl', 'rb')
nw_state = pickle.load(state_file)

nw_state.show_network()