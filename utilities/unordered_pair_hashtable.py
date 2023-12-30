class UnorderedPairHashtable:
    def __init__(self):
        self.table = {}

    def add(self, el_1, el_2, value):
        if el_1 < el_2:
            self.table[(el_1, el_2)] = value
        else:
            self.table[(el_2, el_1)] = value

    def get(self, el_1, el_2):
        if el_1 < el_2:
            return self.table[(el_1, el_2)]
        else:
            return self.table[(el_2, el_1)]
