class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}

    def push(self, val):
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

    def pop(self):
        # max_f = max(self.group.keys())
        # val = self.group[max_f].pop()
        # self.freq[val] -= 1
        # if not self.group[max_f]:
        #     self.group[max_f] = []

        # return val
        max_f = None
        for i in self.group:
            if self.group[i]:
                if max_f is None or i > max_f:
                    max_f = i
        val = self.group[max_f].pop()
        self.freq[val] -= 1
        return val