class MyStack(object):

    def __init__(self):
        self.inp = []
        self.out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inp.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.inp) > 1:
            self.out.append(self.inp.pop(0))
        que_pop = self.inp.pop(0)
        self.inp, self.out = self.out, []
        return que_pop
        

    def top(self):
        """
        :rtype: int
        """
        while len(self.inp) > 1:
            self.out.append(self.inp.pop(0))
        que_top = self.inp.pop(0)
        self.out.append(que_top)
        self.inp, self.out = self.out, []
        return que_top
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.inp) == 0 and len(self.out) == 0:
            return True
        return False