import random
from cbr_lab.simplicial import SimplicialComplex3D
from cbr_lab.simplicial_topology import simplicial_manifold_report


def test_s3_seed_has_expected_topology():
    c = SimplicialComplex3D.s3_boundary_seed()
    r = simplicial_manifold_report(c)
    assert r["face_closed_fraction"] == 1.0
    assert r["s2_pass_fraction"] == 1.0
    assert r["global_betti"] == [1,0,0,1]


def test_14_preserves_s3_manifold_evidence():
    c = SimplicialComplex3D.s3_boundary_seed()
    assert c.pachner_14(random.Random(1))
    r = simplicial_manifold_report(c)
    assert r["face_closed_fraction"] == 1.0
    assert r["s2_pass_fraction"] == 1.0
    assert r["global_betti"] == [1,0,0,1]


def test_defect_can_break_closedness():
    c = SimplicialComplex3D.s3_boundary_seed()
    c.remove_tetra(next(iter(c.tetrahedra)))
    r = simplicial_manifold_report(c)
    assert r["face_closed_fraction"] < 1.0
