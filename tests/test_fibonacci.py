from fibonacci import fib

def test_fibonaci():
    for n, v in enumerate([0,1,1,2,3,5]):
        assert fib(n)==v