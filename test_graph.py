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
    g.edge_list.append(Edge(n1, n2))
    g.edge_list.append(Edge(n2, n3))
    g.edge_list.append(Edge(n1, n3))
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
    pass
