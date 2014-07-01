from Queue import Queue as Q


class NodeNotInGraphError(Exception):
    pass


class EdgeNotInGraphError(Exception):
    pass


class Node(object):
    """A simple node class for use with the Graph class"""
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __eq__(self, other):
        return self is other

    def __str__(self):
        return "[{}]".format(self.value)


class Edge(object):
    """A simple edge class for use with the Graph class"""
    def __init__(self, n1, n2, w=1):
        self.n1 = n1
        self.n2 = n2
        self.weight = w

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
    """An object-oriented adjacency list-style implementation of a graph"""
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

    def add_edge(self, n1, n2, weight=1):
        # first check to see if edge already exists. If it does, do nothing.
        if self._get_edge(n1, n2) is not None:
            return
        new_edge = Edge(n1, n2, weight)
        self.edge_list.append(new_edge)
        n1.edges.append(new_edge)
        n2.edges.append(new_edge)

    def del_node(self, n):
        # first, determine if n is in the graph. If it is, remove it.
        try:
            self.node_list.remove(n)
        except ValueError:
            # n isn't in graph, so raise an error
            raise NodeNotInGraphError

        # next, find n's neighbors and remove affected edges for them
        [edge.getNeighbor(n).edges.remove(edge) for edge in n.edges]

        # then, remove the edges from the graph's edge list
        [self.edge_list.remove(edge) for edge in n.edges]

        # lastly, remove the affected edges from the node being removed
        [n.edges.remove(edge) for edge in n.edges]

    def del_edge(self, n1, n2):
        # get the edge object for this edge
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
        if (not self.has_node(n1)) or (not self.has_node(n2)):
            raise NodeNotInGraphError
        return self._get_edge(n1, n2) is not None

    def _depth_first_traversal(self, node, traversed=[]):
        node.marked = True
        # traversed.append(node)
        traversed = traversed + [node]
        for edge in node.edges:
            if not hasattr(edge.getNeighbor(node), 'marked'):
                traversed = self._depth_first_traversal(
                    edge.getNeighbor(node),
                    traversed)
        return traversed

    def depth_first_traversal(self, node, traversed=[]):
        traversed = self._depth_first_traversal(node, traversed)
        # this is the first recursive call, so clean up
        for n in self.node_list:
            if hasattr(n, 'marked'):
                del n.marked
        return traversed

    def breadth_first_traversal(self, node):
        q = Q()
        q.put(node)
        node.bmarked = True
        traversed = [node]
        while not q.empty():
            t = q.get()
            for n in self.neighbors(t):
                if not hasattr(n, 'bmarked'):
                    q.put(n)
                    n.bmarked = True
                    traversed.append(n)
        for n in self.node_list:
            if hasattr(n, 'bmarked'):
                del n.bmarked
        return traversed

    def _min_dist(self, q, distance):
        min_node = q[0]
        for node in q:
            if distance[node] < distance[min_node]:
                min_node = node
        return min_node

    def shortest_path_dijkstra1(self, s, d):
        """Reference implementation"""
        distance, previous, q = {}, {}, []
        distance[s] = 0
        for node in self.node_list:
            if node is not s:
                distance[node] = float("inf")
                previous[node] = None
            q.append(node)

        while q:
            current_node = self._min_dist(q, distance)
            q.remove(current_node)

            for edge in current_node.edges:
                neighbor = edge.getNeighbor(current_node)
                cost = distance[current_node] + edge.weight
                if cost < distance[neighbor]:
                    distance[neighbor] = cost
                    previous[neighbor] = current_node

        if previous.get(d, None) is None:
            return None  # there is no path to the destination node

        shortest_path = []
        current_node = d
        while current_node in previous:
            shortest_path.append(current_node)
            current_node = previous[current_node]
        shortest_path.append(s)
        return shortest_path, distance[d]


if __name__ == '__main__':

    print "Building a seven item, cyclic graph..."
    print """
                    A  \n
                   /|\ \n
                  B C D\n
                 /|\ / \n
                E F G  \n
    """
    g = Graph()
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')
    n7 = Node('G')

    g.node_list.append(n1)
    g.node_list.append(n2)
    g.node_list.append(n3)
    g.node_list.append(n4)
    g.node_list.append(n5)
    g.node_list.append(n6)
    g.node_list.append(n7)

    eAB = Edge(n1, n2)
    eAC = Edge(n1, n3)
    eAD = Edge(n1, n4)
    eBE = Edge(n2, n5)
    eBF = Edge(n2, n6)
    eBG = Edge(n2, n7)
    g.edge_list.append(eAB)
    g.edge_list.append(eAC)
    g.edge_list.append(eAD)
    g.edge_list.append(eBE)
    g.edge_list.append(eBF)
    g.edge_list.append(eBG)

    n1.edges.append(eAB)
    n1.edges.append(eAC)
    n1.edges.append(eAD)
    n2.edges.append(eAB)
    n2.edges.append(eBE)
    n2.edges.append(eBF)
    n2.edges.append(eBG)
    n3.edges.append(eAC)
    n4.edges.append(eAD)
    n5.edges.append(eBE)
    n6.edges.append(eBF)
    n7.edges.append(eBG)

    # insert the cycle part
    eGD = Edge(n7, n4)
    g.edge_list.append(eGD)
    g.node_list[3].edges.append(eGD)
    g.node_list[6].edges.append(eGD)

    b_traversal = g.breadth_first_traversal(g.node_list[0])
    d_traversal = g.depth_first_traversal(g.node_list[0])

    print "breadth traversal:"
    print [item.value for item in b_traversal]
    print "depth traversal:"
    print [item.value for item in d_traversal]
