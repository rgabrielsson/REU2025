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
        if count == 3 and a != 1 and b != 1 and c != 1:
            print(combo)
            print(a+b+c)

    #print(maxcount)


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


#test_cases()



def calc_charge(val):
    charge = 2**(val-1) * (14-val)
    if charge < 0:
        charge = charge / math.comb(val,3)
    return charge

def test_2():
    families = []
    for a in range(11):
        for b in range(11):
            for c in range(11):
                families.append((a,b,c))           
    
    worst_charge = 0
    worst_families = []
    pairings = []
    for family in families:
        a = family[0]
        b = family[1]
        c = family[2]
        c3 = calc_charge(3)
        ca = calc_charge(a+3)
        cb = calc_charge(b+3)
        cc = calc_charge(c+3)
        cab = calc_charge(a+b+3)
        cac = calc_charge(a+c+3)
        ccb = calc_charge(b+c+3)
        cabc = calc_charge(a+b+c+3)
        charges = [c3,ca,cb,cc,cab,cac,ccb,cabc]
        total = sum(charges) / len(charges)
        if total >= worst_charge:
            worst_charge = total
        pairings.append((total,(a,b,c)))
    for pairing in pairings:
        if pairing[0] == worst_charge:
            worst_families.append(pairing[1])    
    print(worst_charge)
    print(worst_families)


test_2()