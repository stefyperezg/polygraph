class AssertionFinder:
    def __init__(self):
        pass

    def assertion_likelihood(self, sentence: str) -> float:
        return 0.5

    def parse_captions(self, captions: dict) -> dict:
        return {k: self.assertion_likelihood(v) for k, v in captions.items()}

