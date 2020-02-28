# APMA 3100-006 S2020 Project 1
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian

class rand16bit:
    x = []
    a = 24693
    c = 3517
    k = 2**15

    ## Initialize with pseudo-random numbers up to n
    def __init__(self, n, x_0 = 1000):
        self.x = [x_0]
        self.grow(n)

    ## Grow array of pseudo-random numbers to size n
    def grow(self, n):
        while (len(self.x) <= n):
            self.x.append( (self.a*self.x[len(self.x) - 1] + self.c) % self.k )

    ## Print array fo pseudo-random numbers
    def print(self):
        for i in range(len(self.x)):
            print("[{:4d}]: {:d}".format(i, self.x[i]))

    ## Get pseudo-random number i
    def getX(self, i):
        self.grow(i)
        return self.x[i]

    ## Get pseudo-random probablity i
    def getU(self, i):
        self.grow(i)
        return self.x[i]/self.k
