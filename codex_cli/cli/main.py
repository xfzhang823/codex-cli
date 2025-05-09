# main.py
"""
Main entry point for the Codex CLI application.
"""
import argparse
from codex_cli.modules.code_generation import CodeGenerator
from codex_cli.modules.code_analysis import CodeAnalyzer
from codex_cli.modules.extraction import Extractor
from codex_cli.modules.refactoring import Refactorer
from codex_cli.modules.explanation import Explainer
from codex_cli.modules.testing import TestGenerator
from codex_cli.modules.search import Searcher


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Codex CLI - A command-line interface for AI-assisted code generation and analysis")
    subparsers = parser.add_subparsers(dest="command")

    # Generate Command
    gen_parser = subparsers.add_parser("generate", help="Generate code from a prompt")
    gen_parser.add_argument("prompt", type=str, help="Prompt for code generation")
    gen_parser.add_argument("--max_tokens", type=int, default=150, help="Maximum tokens for generation")

    # Analyze Command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a Python file")
    analyze_parser.add_argument("file", type=str, help="Path to the Python file to analyze")

    # Search Command
    search_parser = subparsers.add_parser("search", help="Search for a keyword in Python files")
    search_parser.add_argument("keyword", type=str, help="Keyword to search")
    search_parser.add_argument("dir", type=str, help="Directory to search in")

    return parser.parse_args()


def main():
    args = parse_cli_args()

    if args.command == "generate":
        generator = CodeGenerator()
        result = generator.generate_code(args.prompt, max_tokens=args.max_tokens)
        print("\nGenerated Code:\n", result)

    elif args.command == "analyze":
        analyzer = CodeAnalyzer()
        with open(args.file, "r") as file:
            code = file.read()
        analysis = analyzer.analyze(code)
        print(f"\nFunctions: {analysis['functions']}\nClasses: {analysis['classes']}")

    elif args.command == "search":
        searcher = Searcher()
        matches = searcher.search(args.keyword, args.dir)
        if matches:
            for match in matches:
                print(f"Found in: {match}")
        else:
            print("No matches found.")

    else:
        print("Unknown command. Use --help for usage information.")


if __name__ == "__main__":
    main()