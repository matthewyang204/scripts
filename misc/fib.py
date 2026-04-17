def fib(n=20, startA=0, startB=1):
    a, b = startA, startB
    list = []
    list.append(a)
    for i in range(n):
        a, b = b, a + b
        list.append(a)
    return list

def printFib(n=20):
    toPrint = fib(n=n)
    for obj in toPrint:
        print(obj, end=' ')

def main():
    # Example usage of function
    print("Running example to get 20 terms...")
    printFib()

if __name__ == '__main__':
    main()
