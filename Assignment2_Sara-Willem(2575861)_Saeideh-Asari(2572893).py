#Sara Willems (2575861)
#Saeideh Asari(2572893)

import sys

class Nodes:
    #edge_tuple stores i and j for each node
    def __init__(self, edge_tuple, node_id, parent, children=[]):
        self.edge = edge_tuple
        self.node_id = node_id
        self.parent = parent
        self.children = children


class SuffixTree:

    def __init__(self):
        self.tree = [Nodes((0, 0), 0, None, [])]
        self.text = ''

    def get_new_active_pos(self, active_pos):
        new_active_pose = []
        new_active_pose[0] = active_pos[0]
        new_active_pose[1] = c
        new_active_pose[2] += 1
        return(tuple(new_active_pose))

    def new_node(self, active_pos, i, j):
        for child in self.tree[active_pos[0]].children:
            if (self.text[self.tree[child].edge[0]]) == c:
                break
            else:
                self.tree.append(Nodes())

    def move_down(self, active_pos, c):
        for child in self.tree[active_pos[0]].children:
            if self.text[child[0]] != c:
                return None
            else:
                self.get_new_active_pos(active_pos)

    def use_suffix_link(self, active_pose):
        pass

    def add_suffix_link(self, a, b):
        pass


s = sys.argv[0]
tree = SuffixTree()

active_pos = (0, '', 0)  # (node: index of the node, letter, depth)  #it is a tuple
for i, c in enumerate(s):
    tree.text += c
    visited_nodes = []
    while True:
        new_pos = tree.move_down(active_pos, c)
        if new_pos is None:
            link_target = tree.use_suffix_link(active_pos)
            parent_id = tree.new_node(active_pos, i, None)
            visited_nodes.append(parent_id)
            if link_target is None:
                break
            active_pos = link_target
        else:
            visited_nodes.append(active_pos[0])
            active_pos = new_pos
            break
    for j in range(len(visited_nodes)-1):
        tree.add_suffix_link(visited_nodes[j], visited_nodes[j+1])