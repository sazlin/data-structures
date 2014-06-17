class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2


class Graph(object):
    """A simple graph"""
    def __init__(self):
        self.edge_list = []
        self.node_list = []

    def nodes(self):
        return self.node_list

    def edges(self):
        return self.edge_list

    def add_node(self, n):
        self.node_list.append(n)

    def add_edge(self, n1, n2):
        pass

    def del_node(self, n):
        pass

    def del_edge(self, n1, n2):
        pass

    def had_node(self, n):
        pass

    def neighbors(self, n):
        pass

    def adjacent(self, n1, n2):
        pass
