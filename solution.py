# # Cactus Labs Python Test
import networkx as nx
import pandas as pd

def find_common_node(data_set_path, node_a, node_b):
    #create graph
    g = nx.read_edgelist(data_set_path,create_using=nx.DiGraph(), nodetype = int)
    print(nx.info(g))
    # Find a least common anscestors
    node_a_branch = nx.ancestors(g, node_a).union({node_a})
    node_b_branch = nx.ancestors(g, node_b).union({node_b})
    common = node_a_branch & node_b_branch
    if len(common) == 0:
        lca = None
    else:
        for c in common:
            lca=(nx.shortest_path_length(g, c), c)
    return(lca[1])
