class NodeNotInGraphError(Exception):
    pass


class EdgeNotInGraphError(Exception):
    pass


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __eq__(self, other):
        return self is other


class Edge(object):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __eq__(self, other):
        return self is other

    def getNeighbor(self, n):
        if self.n1 == n:
            return self.n2
        elif self.n2 == n:
            return self.n1
        else:
            raise ValueError(u"Edge does not point to the provided node")


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

    def _get_edge(self, n1, n2):
        for e in self.edge_list:
            if (e.n1 == n1 or e.n1 == n2) and \
               (e.n2 == n1 or e.n2 == n2):
                return e
        return None

    def add_edge(self, n1, n2):
        # first check to see if edge already exists. If it does, do nothing.
        if self._get_edge(n1, n2) is not None:
            return
        new_edge = Edge(n1, n2)
        self.edge_list.append(new_edge)
        n1.edges.append(new_edge)
        n2.edges.append(new_edge)

    def del_node(self, n):
        #first, determine if n is in the graph. If it is, remove it.
        try:
            self.node_list.remove(n)
        except ValueError:
            #n isn't in graph, so raise an error
            raise NodeNotInGraphError

        #next, find n's neighbors and remove affected edges for them
        [edge.getNeighbor(n).edges.remove(edge) for edge in n.edges]

        #then, remove the edges from the graph's edge list
        [self.edge_list.remove(edge) for edge in n.edges]

        #lastly, remove the affected edges from the node being removed
        [n.edges.remove(edge) for edge in n.edges]

    def del_edge(self, n1, n2):
        #get the edge object for this edge
        edge = self._get_edge(n1, n2)
        if edge is None:
            raise EdgeNotInGraphError
        n1.edges.remove(edge)
        n2.edges.remove(edge)
        self.edge_list.remove(edge)

    def has_node(self, n):
        for node in self.node_list:
            if node == n:
                return True
        return False

    def neighbors(self, n):
        if not self.has_node(n):
            raise NodeNotInGraphError
        return [edge.getNeighbor(n) for edge in n.edges]


    def adjacent(self, n1, n2):
        pass