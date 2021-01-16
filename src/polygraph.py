from src.assertion_finder import AssertionFinder
from src.textual_entailment import TextualEntailment


class Polygraph:
    def __init__(self, top_n=10):
        self.top_n = top_n
        self.assertion_finder = AssertionFinder()
        self.hypothesis_tester = TextualEntailment()

    def run(self, captions: dict):
        assertion_scores = self.assertion_finder.parse_captions(captions)
        assertions = sorted(assertion_scores, key=lambda x: x[1], reverse=True)[:self.top_n]
