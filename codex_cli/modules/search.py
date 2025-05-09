# search.py
# Searching for keywords in project files

import os

class Searcher:
    def search(self, term: str, directory: str) -> list:
        matches = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    with open(os.path.join(root, file), "r") as f:
                        content = f.read()
                        if term in content:
                            matches.append(os.path.join(root, file))
        return matches
