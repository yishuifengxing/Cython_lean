import fib
import time
start_time = time.clock()
a = fib.fib(50)
end_time = time.clock()
run_time = end_time - start_time
print(a,run_time)