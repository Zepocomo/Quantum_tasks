import time

start_time = time.perf_counter() #used perf_counter()  because it's more accurate than time()

N1 = int(1)
N2 = int(3)
N3 = int(10)
def sum(N):
    sum = N * (N + 1) // 2
    return sum

end_time = time.perf_counter()

print('\nsum of ',N1,' is ',sum(N1)," and time of execution is: {:.10f} seconds".format(end_time - start_time))
print('sum of ',N2,' is ',sum(N2)," and time of execution is: {:.10f} seconds".format(end_time - start_time))
print('sum of ',N3,' is ',sum(N3)," and time of execution is: {:.10f} seconds".format(end_time - start_time),'\n')