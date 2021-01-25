Write an algorithm which computes the number of trailing zeros in a factorial

## Brute force
Calculate the factorial
Count the zeros

5! = 5 x 4 x 3 x 2 x 1
n! = n x (n-1) x n 1 x… 3 x 2 x 1
```python
def factorial(n):
   	if n < 1:
   		rise ArithmeticError()
   	if n == 1:
   		return 1
   	else:
   		return n * factorial(n-1)
   
def count_trailing_zeros(n):
   	return len(str(n)) - len( str(n).rstrip(‘0’) )
```



## Getting a bit more clever

Is there something clever I can do to get only the number zeros? Somehow count how many times we multiply by ten?

