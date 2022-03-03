class RecordScore():
    def __init__(self, score=0):
        self.score = score

    def __call__(self, score):
        if self.score == 0 or score > self.score:
            self.score = score
        return self.score
