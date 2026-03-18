"""Tests for KnowledgeBaseBuilder."""
from src.core import KnowledgeBaseBuilder
def test_init(): assert KnowledgeBaseBuilder().get_stats()["ops"] == 0
def test_op(): c = KnowledgeBaseBuilder(); c.generate(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = KnowledgeBaseBuilder(); [c.generate() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = KnowledgeBaseBuilder(); c.generate(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = KnowledgeBaseBuilder(); r = c.generate(); assert r["service"] == "knowledge-base-builder"
