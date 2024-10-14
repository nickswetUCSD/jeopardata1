import time


def F(n):
    '''Returns a list of the nth fibonacci numbers. When n = 1, returns [0]; When n = 2, returns [0, 1].'''


    memos = {0: 0, 1: 1}
    def fib(n):
        '''Returns a list of the nth fibonacci numbers. When n = 0, returns 0. When n = 1, returns 1'''

        if not isinstance(n, int):
            return AssertionError("n must be an integer >= 0")

        if n not in memos:
            memos[n] = fib(n - 1) + fib(n - 2)
        return memos[n]

    run = fib(n)
    out = list(memos.values())[:-1]
    return out