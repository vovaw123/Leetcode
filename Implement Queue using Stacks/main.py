class MyQueue(object):

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
        if not self.out:
            while len(self.inp) != 0:
                self.out.append((self.inp.pop()))
        return self.out.pop()


    def peek(self):
        """
        :rtype: int
        """
        if not self.out:
            while len(self.inp) != 0:
                self.out.append((self.inp.pop()))
        return self.out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # while len(self.inp) != 0:
        #     self.inp.pop()
        # while len(self.out) != 0:
        #     self.out.pop()
        # return self.inp, self.out
        if len(self.inp) == 0 and len(self.out) == 0:
            return True
        return False