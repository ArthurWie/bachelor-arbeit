"""Smoke: alle Module ohne GPU/Docling importierbar; MCP-Server registriert
alle Werkzeuge (Modelle werden erst beim ersten Encode geladen)."""

import importlib


def test_kernmodule_importierbar_ohne_torch_und_docling():
    for mod in ("library_core.config", "library_core.db", "library_core.cite",
                "library_core.parse", "library_core.chunk",
                "library_core.retrieve", "library_core.corpus"):
        importlib.import_module(mod)


def test_mcp_server_registriert_alle_werkzeuge():
    server = importlib.import_module("retrieval_mcp.__main__")
    names = {t.name for t in server.mcp._tool_manager.list_tools()}
    expected = {
        "search_library", "search_library_multi", "find_relevant_documents",
        "read_full_document", "get_chunk_context", "list_documents",
        "verify_citations",
    }
    assert expected <= names
