"""CLI for knowledge-base-builder."""
import sys, json, argparse
from .core import KnowledgeBaseBuilder

def main():
    parser = argparse.ArgumentParser(description="Build searchable knowledge bases from documents with AI-powered organization")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = KnowledgeBaseBuilder()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.generate(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"knowledge-base-builder v0.1.0 — Build searchable knowledge bases from documents with AI-powered organization")

if __name__ == "__main__":
    main()
