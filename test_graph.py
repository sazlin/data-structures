from graph import Graph
from graph import Node
from graph import Edge
import pytest


@pytest.fixture(scope="function")
def setup_simple_graph():
    g = Graph()
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    g.node_list.append(n1)
    g.node_list.append(n2)
    g.node_list.append(n3)
    eAB = Edge(n1, n2)
    eAC = Edge(n1, n3)
    g.edge_list.append(eAB)
    g.edge_list.append(eAC)

    n1.edges.append(eAB)
    n1.edges.append(eAC)
    n2.edges.append(eAB)
    n3.edges.append(eAC)
    return g


@pytest.fixture(scope="function")
def setup_weighted_graph(setup_simple_graph):
    g = setup_simple_graph
    g.edge_list[0].weight = 2
    g.edge_list[1].weight = 3
    g.add_edge(g.node_list[1], g.node_list[2])
    n4 = Node('D')
    g.add_node(n4)
    g.add_edge(g.node_list[2], n4, 5)
    return g


@pytest.fixture(scope="function")
def setup_7_item_acyclic_graph():
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
    return g


@pytest.fixture(scope="function")
def setup_7_item_cyclic_graph(setup_7_item_acyclic_graph):
    g = Graph()
    g = setup_7_item_acyclic_graph
    n4 = g.node_list[3]  # 'D'
    n7 = g.node_list[6]  # 'G'
    eGD = Edge(n7, n4)
    g.edge_list.append(eGD)
    g.node_list[3].edges.append(eGD)
    g.node_list[6].edges.append(eGD)
    return g


@pytest.fixture(scope="function")
def setup_big_weighted_graph(setup_7_item_cyclic_graph):
    g = setup_7_item_cyclic_graph
    g.edge_list[0].weight = 2
    g.edge_list[1].weight = 1
    g.edge_list[2].weight = 10
    g.edge_list[3].weight = 9
    g.edge_list[4].weight = 1
    g.edge_list[5].weight = 2
    g.edge_list[6].weight = 5


@pytest.fixture(scope="function")
def setup_unconnected_graph():
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
    eAG = Edge(n1, n7)
    g.edge_list.append(eAG)
    g.node_list[0].edges.append(eAG)
    g.node_list[6].edges.append(eAG)
    return g


@pytest.fixture(scope="function")
def setup_acyclic_graph(setup_simple_graph):
    q = setup_simple_graph
    A_node, B_node = q.node_list[0], q.node_list[1]
    new_node = Node('D')
    q.add_node(new_node)
    q.add_edge(B_node, new_node)
    return q


@pytest.fixture(scope="function")
def setup_cyclic_graph(setup_acyclic_graph):
    q = setup_acyclic_graph
    A_node, D_node = q.node_list[0], q.node_list[3]
    q.add_edge(D_node, A_node)
    return q


def test_node_init():
    n = Node(123)
    assert n is not None
    assert n.value == 123


def test_edge_init():
    e = Edge(Node(1), Node(2))
    assert e is not None
    assert e.n1 is not None
    assert e.n1.value == 1
    assert e.n2 is not None
    assert e.n2.value == 2


def test_graph_init():
    g = Graph()
    assert g is not None
    assert g.node_list is not None
    assert g.edge_list is not None


def test_graph_nodes(setup_simple_graph):
    g = setup_simple_graph
    nodes = g.nodes()
    assert nodes[0].value == 'A'
    assert nodes[1].value == 'B'
    assert nodes[2].value == 'C'


def test_graph_edges(setup_simple_graph):
    g = setup_simple_graph
    edges = g.edges()
    assert len(edges) == 2
    assert edges[0].n1.value == 'A'
    assert edges[0].n2.value == 'B'
    assert edges[1].n1.value == 'A'
    assert edges[1].n2.value == 'C'


def test_graph_add_edge():
    g = Graph()
    test_node1 = Node('A')
    test_node2 = Node('B')
    g.node_list.append(test_node1)
    g.node_list.append(test_node2)
    assert len(g.edge_list) == 0
    assert len(test_node1.edges) == 0
    assert len(test_node2.edges) == 0
    g.add_edge(test_node1, test_node2)
    g.add_edge(test_node1, test_node2)
    g.add_edge(test_node1, test_node2)
    assert len(g.edge_list) == 1
    assert len(test_node1.edges) == 1
    assert len(test_node2.edges) == 1


def test_graph_del_node(setup_simple_graph):
    q = setup_simple_graph
    assert len(q.edge_list) == 2
    assert len(q.node_list) == 3
    deleted_node = q.node_list[0]
    q.del_node(deleted_node)
    assert len(q.node_list) == 2
    assert len(q.edge_list) == 0  # both edges should have been deleted
    assert len(q.node_list[0].edges) == 0
    assert len(q.node_list[1].edges) == 0


def test_graph_del_edge(setup_simple_graph):
    q = setup_simple_graph
    deleted_edge_n1, deleted_edge_n2 = q.edge_list[0].n1, q.edge_list[0].n2
    assert len(q.node_list) == 3
    assert len(q.edge_list) == 2
    assert len(deleted_edge_n1.edges) == 2
    assert len(deleted_edge_n2.edges) == 1
    q.del_edge(deleted_edge_n1, deleted_edge_n2)
    assert len(q.node_list) == 3
    assert len(q.edge_list) == 1
    assert len(deleted_edge_n1.edges) == 1
    assert len(deleted_edge_n2.edges) == 0


def test_graph_has_node_1():
    q = Graph()
    new_node = Node(74782034)
    assert not q.has_node(new_node)
    q.node_list.append(new_node)
    assert q.has_node(new_node)


def test_graph_has_node_2(setup_simple_graph):
    q = setup_simple_graph
    new_node = Node(9812738921)
    assert not q.has_node(new_node)
    q.node_list.append(new_node)
    assert q.has_node(new_node)


def test_graph_neighbors(setup_simple_graph):
    q = setup_simple_graph
    neighbors = q.neighbors(q.node_list[0])
    assert q.node_list[1] in neighbors
    assert q.node_list[2] in neighbors
    assert q.node_list[0] not in neighbors


def test_graph_adjacent(setup_simple_graph):
    q = setup_simple_graph
    new_node = Node(82390832)
    q.node_list.append(new_node)
    assert q.adjacent(q.node_list[0], q.node_list[1])
    assert not q.adjacent(q.node_list[0], new_node)


def test_depth_first_traversal_acyclic(setup_acyclic_graph):
    q = setup_acyclic_graph
    traversed = q.depth_first_traversal(q.node_list[0])
    print [str(i) for i in traversed]
    assert traversed[0] == q.node_list[0]  # A
    assert traversed[1] == q.node_list[1]  # B
    assert traversed[2] == q.node_list[3]  # D
    assert traversed[3] == q.node_list[2]  # C


def test_depth_first_traversal_cyclic(setup_cyclic_graph):
    q = setup_cyclic_graph
    traversed = q.depth_first_traversal(q.node_list[0])
    print [str(i) for i in traversed]
    assert traversed[0] == q.node_list[0]  # A
    assert traversed[1] == q.node_list[1]  # B
    assert traversed[2] == q.node_list[3]  # D
    assert traversed[3] == q.node_list[2]  # C


def test_depth_first_traversal_multiple_runs(setup_cyclic_graph):
    q = setup_cyclic_graph
    traversed1 = q.depth_first_traversal(q.node_list[0])
    traversed2 = q.depth_first_traversal(q.node_list[0])
    traversed3 = q.depth_first_traversal(q.node_list[0])
    traversed4 = q.depth_first_traversal(q.node_list[0])
    assert len(traversed2) == len(traversed1)
    assert len(traversed3) == len(traversed1)
    assert len(traversed4) == len(traversed1)
    for i in range(len(traversed1)):
        assert traversed2[i] == traversed1[i]
        assert traversed3[i] == traversed1[i]
        assert traversed4[i] == traversed1[i]

def test_breadth_first_traversal_acyclic(setup_7_item_acyclic_graph):
    g = setup_7_item_acyclic_graph
    traversed = g.breadth_first_traversal(g.node_list[0])
    print "acyclic graph, breadth first"
    print [item.value for item in traversed]
    assert traversed[0] == g.node_list[0]  # 'A'
    assert traversed[1] == g.node_list[1]  # 'B'
    assert traversed[2] == g.node_list[2]  # 'C'
    assert traversed[3] == g.node_list[3]  # 'D'
    assert traversed[4] == g.node_list[4]  # 'E'
    assert traversed[5] == g.node_list[5]  # 'F'
    assert traversed[6] == g.node_list[6]  # 'G'


def test_breadth_first_traversal_cyclic(setup_7_item_cyclic_graph):
    g = setup_7_item_cyclic_graph
    traversed = g.breadth_first_traversal(g.node_list[0])
    print "cyclic graph, breadth_first"
    print [item.value for item in traversed]
    assert traversed[0] == g.node_list[0]  # 'A'
    assert traversed[1] == g.node_list[1]  # 'B'
    assert traversed[2] == g.node_list[2]  # 'C'
    assert traversed[3] == g.node_list[3]  # 'D'
    assert traversed[4] == g.node_list[4]  # 'E'
    assert traversed[5] == g.node_list[5]  # 'F'
    assert traversed[6] == g.node_list[6]  # 'G'


def test_breadth_first_unconnected_graph(setup_unconnected_graph):
    g = setup_unconnected_graph
    traversed = g.breadth_first_traversal(g.node_list[0])
    print "unconnected graph, breadth first (only A and G connected)"
    print [item.value for item in traversed]
    assert len(traversed) == 2
    assert traversed[0] == g.node_list[0]  # 'A'
    assert traversed[1] == g.node_list[6]  # 'G'


def test_weighted_edges(setup_weighted_graph):
    g = setup_weighted_graph
    assert g.edge_list[0].weight == 2
    assert g.edge_list[1].weight == 3
    assert g.edge_list[2].weight == 1


def test_shortest_path_dijkstra_1(setup_big_weighted_graph):
    g = setup_big_weighted_graph
    node_A, node_D = g.node_list[0], g.node_list[3]

    path, cost = g.shortest_path_dijkstra1(node_A, node_D)
    assert path.pop().value == 'A'
    assert path.pop().value == 'B'
    assert path.pop().value == 'G'
    assert path.pop().value == 'D'
    assert cost == 9
    with pytest.raises(IndexError):
        path.pop()

