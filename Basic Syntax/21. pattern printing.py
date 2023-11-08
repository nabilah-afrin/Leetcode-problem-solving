#pattern printing
n = int(input())
def star_pattern(n):
    for i in range (1,n+1):
      print("*" * i)

def reverse_star_pattern(n):
   for i in range(n, 0, -1):
     print( "*" * i)
   
def flipped_star_pattern(n):
   for i in range(1,n+1):
      print(" " * (n-i) + "*" * i)
""""in order to do it with while we have to also define i =0
    while i=<n:
        print()"""

def pyramid(n):
    for i in range(n):
       print(" " * (n - i - 1) + "*" * (2 * i + 1))

star_pattern(n)
reverse_star_pattern(n)
flipped_star_pattern(n)
pyramid(n)
