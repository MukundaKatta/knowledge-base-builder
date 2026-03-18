"""Integration tests for KnowledgeBaseBuilder."""
from src.core import KnowledgeBaseBuilder

class TestKnowledgeBaseBuilder:
    def setup_method(self):
        self.c = KnowledgeBaseBuilder()
    def test_10_ops(self):
        for i in range(10): self.c.generate(i=i)
        assert self.c.get_stats()["ops"] == 10
    def test_service_name(self):
        assert self.c.generate()["service"] == "knowledge-base-builder"
    def test_different_inputs(self):
        self.c.generate(type="a"); self.c.generate(type="b")
        assert self.c.get_stats()["ops"] == 2
    def test_config(self):
        c = KnowledgeBaseBuilder(config={"debug": True})
        assert c.config["debug"] is True
    def test_empty_call(self):
        assert self.c.generate()["ok"] is True
    def test_large_batch(self):
        for _ in range(100): self.c.generate()
        assert self.c.get_stats()["ops"] == 100
