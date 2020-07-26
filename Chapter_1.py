import time

def fib(n):
    a,b = 0.0,1.0
    for i in range(n):
        a,b = a + b,a
    return a

if __name__ == '__main__':
    start_time = time.clock()
    a = fib(50)
    end_time = time.clock()
    run_time = end_time - start_time
    print(a,run_time)