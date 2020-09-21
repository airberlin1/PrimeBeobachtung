import Functions


def nats(n):
    yield n
    yield from nats(n+1)


def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


def create_list(n, sieve_l):
    relist = []
    for intt in range(1, n):
        relist.append([intt, next(sieve_l)])
    return relist


p = sieve(nats(2))
list_with_primes = create_list(10, p)
print(list_with_primes)
functions = []
for i, prime in enumerate(list_with_primes):
    functions.append(Functions.MathematicalFunction("hey" + str(i + 1), "ganzrational", i))
for fun in functions:
    fun.term.show()
clear_matrix = Functions.Matrix(5, 6)
clear_matrix.show()