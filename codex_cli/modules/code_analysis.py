# code_analysis.py
import ast

class CodeAnalyzer:
    def analyze(self, code: str) -> dict:
        try:
            parsed = ast.parse(code)
            functions = [node.name for node in ast.walk(parsed) if isinstance(node, ast.FunctionDef)]
            classes = [node.name for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)]
            return {"functions": functions, "classes": classes}
        except Exception as e:
            return {"error": str(e)}
