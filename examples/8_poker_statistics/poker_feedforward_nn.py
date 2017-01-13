
from math import exp


def main():
    pass


def sigmoid(z):
    ''' The sigmoid (or logistic) function '''
    return 1.0 / (1.0 + exp(-z))


def dot(K, L):
   ''' The dot product of two lists '''
   if len(K) != len(L):
      return 0.0
   return sum(lst[0] * lst[1] for lst in zip(K, L))


if __name__ == '__main__':
    main()
