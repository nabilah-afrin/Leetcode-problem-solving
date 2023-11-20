#fibonacci
def fibonacci(n):
    a,b = 0,1
    series = []
    while a<n:
        series.append(a)
        a, b = b, a+b
    print(series) #will create from 0,1,1

fibonacci(4)

"""in order to buikd from 1,1,2 
a,b = 1,1
for i in range(n):
a,b = b, a+b
return b"""
while n>1: return fib(n-1) + fib(n-2)
