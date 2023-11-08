#fibonacci
def fibonacci(n):
    a,b = 0,1
    series = []
    while a<n:
        series.append(a)
        a, b = b, a+b
    print(series)

fibonacci(4)
