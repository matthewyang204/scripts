import math

# Useless calc1 - see computeExpected for proper computation
def calc1():
    amounts = [0, 50000, 100000, 150000, 200000, 250000]
    probabilities = [0.65, 0.23, 0.08, 0.02, 0.01, 0.01]

    added = 0
    for i in range(len(amounts)):
        amount = amounts[i-1]
        probability = probabilities[i-1]
        added = added + (amount * probability)

    print(added)

def computeExpected(amounts, probabilities):
    if len(amounts) != len(probabilities):
        print("ERROR: Cannot compute unequal lengthed amounts against probabilities")
        raise ValueError("Lengths of lists must match")
    
    added = 0
    for i in range(len(amounts)):
        amount = amounts[i]
        probability = probabilities[i]
        added = added + (amount * probability)

    return added

def calc2():
    amounts = [8, 6, 4, 2, 0, -2]
    probability = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]

    centsPerDozen = computeExpected(amounts, probability)
    totalCents = (14000 + 4000) * centsPerDozen
    totalDollars = totalCents / 100
    print(totalDollars)

def calc3():
    amounts = [0, 20000, 40000, 60000, 80000, 100000]
    probability = [0.70, 0.19, 0.07, 0.02, 0.01, 0.01]

    added = computeExpected(amounts, probability)
    print(added)

def calc4():
    amounts = [250000, -75000]
    probabilities = [3/4, 1/4]

    added = computeExpected(amounts, probabilities)
    print(added)

def calc5():
    amounts1 = [100, -15]
    probabilities1 = [0.2, 0.8]
    expected1 = computeExpected(amounts1, probabilities1)

    amounts2 = [150, -27]
    probabilities2 = [0.1, 0.9]
    expected2 = computeExpected(amounts2, probabilities2)

    diff = expected2 - expected1

    print(expected1)
    print(expected2)
    print(diff)

def calc6():
    amounts = [-100000, 1]
    probabilities = [22/10000000, 9999978/10000000]

    print(computeExpected(amounts, probabilities))

def calc7():
    amounts = [-140, 45000-140]
    probabilities = [599/600, 1/600]

    print(computeExpected(amounts, probabilities))

def calc8():
    value = 36000
    unitPrice = 140
    n = 600
    soldFor = unitPrice * n
    
    amounts = [-unitPrice, value-unitPrice]
    probabilities = [599/600, 1/600]

    print(computeExpected(amounts, probabilities))
    print(soldFor - value)
    print(soldFor)

def calc9():
    amounts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probabilities = []
    for i in range(len(amounts)):
        probabilities.append(1/len(amounts))

    add = 0
    total = 0
    for i in range(20):
        add = computeExpected(amounts, probabilities)
        total += add
    print(total)

def binomialProb(r, n, p):
    comb = math.comb(n, r)
    finalResult = comb * (p**r) * ((1-p)**(n-r))
    return finalResult

def calc10():
    p = 1/4
    n = 5
    r = 2

    print(binomialProb(r, n, p))

def calc10_1():
    p = 1/4
    n = 5
    r = 2

    inc = 0
    totalProb = 0
    for i in range(4):
        inc = binomialProb(r, n, p)
        totalProb += inc
        r += 1
    print(totalProb)

def calc11():
    p = 0.18
    n = 8
    r = 2

    inc = 0
    totalProb = 0
    for i in range(2):
        inc = binomialProb(r, n, p)
        totalProb += inc
        r -= 1
    print(totalProb)

def calc12():
    p = 0.2
    n = 6
    r = 4

    inc = 0
    totalProb = 0
    for i in range(3):
        inc = binomialProb(r, n, p)
        totalProb += inc
        r += 1
    print(totalProb)

if __name__ == '__main__':
    calc12()

