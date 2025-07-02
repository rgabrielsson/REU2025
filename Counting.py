import math
import itertools

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
    start_charge = 2**(ving-1) * (9-ving)
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


#get charge on a given 0-ving based on formula
def calc_charge(val):
    charge = 2**(val-1) * (9-val)
    if charge < 0:
        charge = charge / math.comb(val,3)
    return charge

#get every possible family
def get_families():
    families = []
    for a in range(11):
        for b in range(11):
            for c in range(11):
                if (a,c,b) not in families and (b,c,a) not in families and (b,a,c) not in families and (c,a,b) not in families and (c,b,a) not in families: 
                    families.append((a,b,c))       
    return families         
    

def test2():
    families = get_families()
    worst_charge = 0
    worst_families = []
    pairings = []

    #iterate over families to find the ones with highest charge
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

        #identify highest possible total charge
        if total >= worst_charge:
            worst_charge = total
        pairings.append((total,(a,b,c)))
    
    #find all families that give the worst possible charge
    pairings.sort()
    for pairing in pairings:
        if pairing[0] == worst_charge:
            worst_families.append(pairing[1])
        if pairing[0] > 0.5*worst_charge and pairing[1][0] != 0:
            print(pairing)  

test2()




def triple_one_clans():
    # Generate all combinations
    combinations = list(itertools.product(range(5), repeat=6))
    for combo in combinations:
        if (combo[0]+combo[1]) > 5 or (combo[2]+combo[3]) > 5 or (combo[4]+combo[5]) > 5:
            combinations.remove(combo)
        else:
            combinations[combinations.index(combo)] = [(combo[0],combo[1]),(combo[2],combo[3]),(combo[4],combo[5])]
        
        for pair in combo:
            
        

    # Print the total number of combinations and a few examples
    print(f"Total combinations: {len(combinations)}")
    for combo in combinations[:10]:  # print first 10
        print(combo)

triple_one_clans()