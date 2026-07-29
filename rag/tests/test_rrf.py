"""Reciprocal Rank Fusion (Harte Regel 7): Platzierung zählt, nie Scores."""

from library_core.retrieve import rrf


def test_doppeltreffer_schlaegt_einzeltreffer():
    dense = [1, 2, 3]
    sparse = [2, 4]
    fused = rrf([dense, sparse], k=60)
    assert fused[0] == 2                      # in beiden Listen -> vorn
    assert set(fused) == {1, 2, 3, 4}         # ALLE Kandidaten bleiben


def test_formel_exakt():
    # score(d) = Σ 1/(k + rank), rank ist 1-basiert
    fused = rrf([[7], [7], [9]], k=60)
    assert fused == [7, 9]                    # 2/61 > 1/61


def test_reihenfolge_innerhalb_einer_liste_bleibt():
    assert rrf([[5, 6, 7]], k=60) == [5, 6, 7]


def test_leere_listen():
    assert rrf([]) == []
    assert rrf([[], []]) == []


def test_deterministisch_bei_gleichstand():
    a = rrf([[1], [2]], k=60)
    b = rrf([[2], [1]], k=60)
    assert a == b == [1, 2]                   # Tie-Break über id, stabil
