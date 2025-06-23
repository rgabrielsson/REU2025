import math

def test_cases():
    testset = [9,10]

    combos = []
    for a in range(11):
        for b in range(11):
            for c in range(11):
                if a + b + c in testset:
                    combos.append((a,b,c))
                elif a in testset:
                    combos.append((a,b,c))
                elif b in testset:
                    combos.append((a,b,c))
                elif c in testset:
                    combos.append((a,b,c))
                elif a + b in testset:
                    combos.append((a,b,c))
                elif c + b in testset:
                    combos.append((a,b,c))
                elif a + c in testset:
                    combos.append((a,b,c))


    maxcount = 0
    for combo in combos:
        count = 0
        a = combo[0]
        b = combo[1]
        c = combo[2]

        if a in testset:
            count += 1
        if b in testset:
            count += 1
        if c in testset:
            count += 1
        if a + b in testset:
            count += 1
        if c + b in testset:
            count += 1
        if a + c in testset:
            count += 1
        if a + b +c in testset:
            count += 1
        if count > maxcount:
            maxcount = count
        if count == 3 and a != 1 and a != 1 and a != 1:
            print(combo)
            print(a+b+c)

    print(maxcount)


def find_lowest_k(ving):
    start_charge = 2**(ving-1) * (14-ving)
    charge = 4096
    k=12
    while charge >= 0:
        k=k+1
        charge = ((math.factorial(k)/(math.factorial(ving)*math.factorial(k-ving)))*start_charge + 2**(k-1) * (14-k))/((math.factorial(k)/(math.factorial(ving)*math.factorial(k-ving)))+1)
    print(ving)
    print(k)
    print(charge)
    print("---------")


for i in range(14):
    find_lowest_k(i)