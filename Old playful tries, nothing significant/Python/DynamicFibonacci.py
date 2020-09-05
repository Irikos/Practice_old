
#solving the fibonacci sequence using dynamic programming
fibonacciDict = {}
def DynamicFibonacci(n):
    if n <= 2:
        f = 1
    else:
        f = DynamicFibonacci(n - 1) + DynamicFibonacci(n - 2)
    fibonacciDict[n] = f
    return f

# print DynamicFibonacci(13)
# print fibonacciDict

# same thing, no recursions. I can save memory by always keeping only the last 2 terms in the dictionary, while deleting the rest.
bopttomUpFibonacciDict = {}
def BottomUpDynamicFibonacci(n):
    for k in range(1,n+1):
        if k <= 2:
            f = 1
        else:
            f = bopttomUpFibonacciDict[k-1] + bopttomUpFibonacciDict[k-2]
        bopttomUpFibonacciDict[k] = f
    return f

print BottomUpDynamicFibonacci(13)
print bopttomUpFibonacciDict
