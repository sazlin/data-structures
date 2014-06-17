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
    eBC = Edge(n2, n3)
    eAC = Edge(n1, n3)
    g.edge_list.append(eAB)
    g.edge_list.append(eBC)
    g.edge_list.append(eAC)

    n1.edges.append(eAB)
    n1.edges.append(eAC)
    n2.edges.append(eAB)
    n2.edges.append(eBC)
    n3.edges.append(eAC)
    n3.edges.append(eBC)
    return g


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
    assert len(edges) == 3
    assert edges[0].n1.value == 'A'
    assert edges[0].n2.value == 'B'
    assert edges[1].n1.value == 'B'
    assert edges[1].n2.value == 'C'
    assert edges[2].n1.value == 'A'
    assert edges[2].n2.value == 'C'


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
    assert len(q.edge_list) == 3
    assert len(q.node_list) == 3
    deleted_node = q.node_list[0]
    q.del_node(deleted_node)
    assert len(q.node_list) == 2
    assert len(q.edge_list) == 1  # 2 edges should have been deleted
    assert len(q.node_list[0].edges) == 1
    assert len(q.node_list[1].edges) == 1


def test_graph_del_edge(setup_simple_graph):
    q = setup_simple_graph
    deleted_edge_n1, deleted_edge_n2 = q.edge_list[0].n1, q.edge_list[0].n2
    assert len(q.node_list) == 3
    assert len(q.edge_list) == 3
    assert len(deleted_edge_n1.edges) == 2
    assert len(deleted_edge_n2.edges) == 2
    q.del_edge(deleted_edge_n1, deleted_edge_n2)
    assert len(q.node_list) == 3
    assert len(q.edge_list) == 2
    assert len(deleted_edge_n1.edges) == 1
    assert len(deleted_edge_n2.edges) == 1
