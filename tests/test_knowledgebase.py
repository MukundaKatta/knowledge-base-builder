"""Tests for KnowledgeBase."""
import pytest
from src.knowledgebase import KnowledgeBase

def test_init():
    obj = KnowledgeBase()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = KnowledgeBase()
    result = obj.ingest_document(input="test")
    assert result["processed"] is True
    assert result["operation"] == "ingest_document"

def test_multiple_ops():
    obj = KnowledgeBase()
    for m in ['ingest_document', 'chunk_text', 'generate_embeddings']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = KnowledgeBase()
    r1 = obj.ingest_document(key="same")
    r2 = obj.ingest_document(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = KnowledgeBase()
    obj.ingest_document()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = KnowledgeBase()
    obj.ingest_document(x=1)
    obj.chunk_text(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
