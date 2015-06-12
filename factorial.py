# factorial.py
def factorial(n):
    if n<=1:
      return 1
    f=1
    while n>1:
      f=f*n
      n=n-1
    return f

fact = factorial(52)
perm = fact / (factorial(52 - 5) * factorial(5))

print ''
print 'How many ways can you lay out a deck of cards in a line?'
print fact
print ''
print 'How many five card hands from a deck of 52 cards?'
print perm
print ''