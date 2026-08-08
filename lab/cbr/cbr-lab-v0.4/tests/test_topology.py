import random
import networkx as nx
from cbr_lab.topology import assess_vertex_link, gf2_rank


def test_tetrahedral_boundary_link_passes():
    # Build a cone over the octahedron surface. The apex link is the octahedron graph,
    # whose flag complex is S^2 (8 triangular faces, no K4s).
    h = nx.octahedral_graph()
    g = nx.Graph(h)
    apex = 99
    g.add_node(apex)
    for v in h.nodes:
        g.add_edge(apex, v)
    report = assess_vertex_link(g, apex)
    assert report["passed_s2"]
    assert report["beta0"] == 1
    assert report["beta1"] == 0
    assert report["beta2"] == 1
    assert report["chi"] == 2


def test_complete_link_fails_as_filled_high_dimensional_simplex():
    g = nx.complete_graph(6)
    report = assess_vertex_link(g, 0)
    assert not report["passed_s2"]
    assert report["T3"] > 0
