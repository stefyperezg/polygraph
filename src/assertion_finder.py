import stanfordnlp
from src.definitions import ROOT_PATH


class AssertionFinder:
    def __init__(self):
        self.nlp = stanfordnlp.Pipeline(processors='tokenize', lang="en")

    def assertion_likelihood(self, sentence: str) -> float:
        return 0.5

    def parse_captions(self, captions: dict) -> dict:
        full_text = " ".join(captions.values())
        doc = self.nlp(full_text)
        return {k: self.assertion_likelihood(v) for k, v in captions.items()}
