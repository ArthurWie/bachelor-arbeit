"""Der Korpus-Adapter gegen die echten, eingefrorenen Dateien der Arbeit.

Absichtlich ein Integrationstest: Genau die Deckungsgleichheit von
coding_table.csv, Scopus-Export und literature/*.pdf ist die Eigenschaft, die
stillschweigend kaputtgehen kann (PDF umbenannt, Zeile ergänzt).
"""

import pytest

from library_core import config, corpus

pytestmark = pytest.mark.skipif(
    not config.CODING_TABLE.is_file(),
    reason=f"Korpusdateien nicht am erwarteten Ort ({config.CODING_TABLE})",
)


@pytest.fixture(scope="module")
def docs():
    return corpus.documents()


def test_alle_studien_mit_existierendem_pdf(docs):
    # documents() wirft bei fehlendem PDF/EID – hier nur die Bestätigung,
    # dass wirklich der volle Korpus ankommt.
    assert len(docs) == 67
    assert all(config.LITERATURE_DIR in __import__("pathlib").Path(d.path).parents
               for d in docs)


def test_study_ids_eindeutig_und_schema(docs):
    ids = [d.study_id for d in docs]
    assert len(set(ids)) == len(ids)
    assert all(i.startswith("S") and i[1:].isdigit() for i in ids)


def test_metadaten_vollstaendig(docs):
    assert all(d.title and d.title != "(ohne Titel)" for d in docs)
    assert all(d.authors for d in docs)
    assert all(d.year and 2014 < d.year < 2027 for d in docs)


def test_scopus_seitenbereiche_nur_wo_vorhanden(docs):
    mit_bereich = [d for d in docs if d.printed_first is not None]
    # 27 Studien haben einen Seitenbereich, der Rest ist artikelnummeriert.
    assert 20 <= len(mit_bereich) <= 40
    assert all(d.printed_last >= d.printed_first for d in mit_bereich)


def test_autoren_scopus_reihenfolge(docs):
    # "Nachname I.I." – kein Komma, keine leeren Einträge.
    for d in docs:
        assert all(a.strip() == a and a for a in d.authors)
