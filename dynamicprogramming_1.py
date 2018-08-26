# Demonstration of overlapping subproblems
# of Dynamic programming
# Using fibonacci series to demonstrate

# Top down Approach

def fib(n, lookup):
    # Base Case
    if n == 0 or n == 1:
        lookup[n] = n

    # If the value is not calculated previously then
    # Calculate it
    if lookup[n] is None:
        lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)

    # Return the value corresponding to that value of n
    return lookup[n]
# end of function


# Bottom up approach
def fib_bottomup(n):

    #array declaration
    f = [0]*(n+1)

    #base case assignment
    f[1] = 1

    # Calculating the fibonacci and storing the values
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i -2]
    return f[n]

def main():
    n = 9
    print("Fibonacci number is ", fib_bottomup(n))

if __name__=="__main__":
    main()