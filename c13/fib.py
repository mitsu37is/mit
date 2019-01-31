import time
import pylab

def recursive_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

def memo_fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = memo_fib(n-1, memo) + memo_fib(n-2, memo)
        memo[n] = result
        return result

def repetition_fib(n):
    result = 0
    f0 = 0
    f1 = 1
    for i in range(n):
        result = f0 + f1
        f0 = f1
        f1 = result
    return result

def test_fib():
    recursive_fib_times = []
    for i in range(1, 26):
        start_time = time.perf_counter()
        for j in range(10):
            recursive_fib(i)
        execution_time = time.perf_counter() - start_time
        recursive_fib_times.append(execution_time)

    memo_fib_times = []
    for i in range(1, 26):
        start_time = time.perf_counter()
        for j in range(10):
            memo_fib(i)
        execution_time = time.perf_counter() - start_time
        memo_fib_times.append(execution_time)

    repetition_fib_times = []
    for i in range(1, 26):
        start_time = time.perf_counter()
        for j in range(10):
            repetition_fib(i)
        execution_time = time.perf_counter() - start_time
        repetition_fib_times.append(execution_time)

    pylab.figure(1)
    pylab.style.use('seaborn-darkgrid')
    pylab.plot(range(1, 26), recursive_fib_times, 'o-', label='recursive fib')
    pylab.plot(range(1, 26), memo_fib_times, 'o-', label='memolization fib')
    pylab.plot(range(1, 26), repetition_fib_times, 'o-', label='repetition fib')
    pylab.title('Compare algorithms')
    pylab.xlabel('Fibonacci sequence nth term')
    pylab.ylabel('Runtime (s)')
    pylab.legend(loc='best')
    pylab.savefig('fib/compare-fig')


test_fib()