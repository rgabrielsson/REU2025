import math
import itertools

#get rid of duplicates
def remove_permutation_duplicates(list_of_lists):
    seen = set()
    result = []
    for lst in list_of_lists:
        key = tuple(sorted(lst))
        if key not in seen:
            seen.add(key)
            result.append(lst)
    return result

#get charge on a given 0-ving based on formula
def calc_charge(val):
    charge = 2**(val-1) * (9-val)
    if charge < 0:
        charge = charge / math.comb(val,3)
    return charge

#get every possible family
def get_families():
    families = []
    for a in range(20):
        for b in range(20):
            for c in range(20): 
                families.append((a,b,c))       
    return families         
    
def families():
    families = get_families()
    worst_charge = 0
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

        #find the total charge on each family
        total = sum(charges) / len(charges)
        pairings.append((total,(a,b,c)))

        #identify highest possible total charge
        if total >= worst_charge:
            worst_charge = total
    
    #sort and return list of families and paired charges
    pairings.sort()
    return pairings

#get every combination for each clan
def get_combos(tup):
    if len(tup) > 4:
        list1 = [1,tup[0]+1, tup[1]+1,tup[0]+tup[1]+1]
        list2 = [1,tup[2]+1, tup[3]+1,tup[2]+tup[3]+1]
        list3 = [1,tup[4]+1, tup[5]+1,tup[4]+tup[5]+1]
    elif len(tup) > 2:
        list1 = [1,tup[0]+1, tup[1]+1,tup[0]+tup[1]+1]
        list2 = [1,tup[2]+1, tup[3]+1,tup[2]+tup[3]+1]
        list3 = [0]
    elif len(tup) > 0:
        list1 = [1,tup[0]+1, tup[1]+1,tup[0]+tup[1]+1]
        list2 = [0]
        list3 = [0]
    else:
        list1 = [0]
        list2 = [0]
        list3 = [0]

    # Get all combinations
    combinations = list(itertools.product(list3, list2, list1))

    return combinations
        

#use the six-code for a clan to get the 3-code
def get_clan_from_six(tup):
    if len(tup) > 4:
        return (tup[0]+tup[1]+1, tup[2]+tup[3]+1, tup[4]+tup[5]+1)
    elif len(tup) > 2:
        return (tup[0]+tup[1]+1, tup[2]+tup[3]+1, 0)
    elif len(tup)>0:
        return (tup[0]+tup[1]+1, 0, 0)
    else:
        return (0, 0, 0)

def clans():
    familyList = families()
    familyDict = {}
    for family in familyList:
        familyDict[family[1]] = family[0]

    #get all pairs of (a,b) that add up to at most 9
    all_pairs1 = [(a, b, c, d, e, f) for a in range(10) for b in range(a, 10) for c in range(10) for d in range(c,10) for e in range(10) for f in range(e,10) if a + b <= 10 if c+d <=10 if e+f <=10]
    all_pairs2 = [(a, b) for a in range(10) for b in range(a, 10) if a + b <= 10]
    all_pairs3 = [(a, b, c, d) for a in range(10) for b in range(a, 10) for c in range(10) for d in range(c,10) if a + b <= 10 if c+d <=10]
    all_pairs = all_pairs2 + all_pairs3 + all_pairs1 + [()]

    #check each clan and find the worst charge
    newlst = []
    for pair in all_pairs:
        set = get_combos(pair)

        total_charge = 0 
        items = 0 
        for item in set:
            total_charge += familyDict[item]
            items += 1
        avgCharge = total_charge/items
        clan = get_clan_from_six(pair)
        newlst.append((avgCharge,clan,pair))

    #write results to clans
    outfile = open("clans.txt","w") 
    newlst.sort()
    for item in newlst:
        print(item,file=outfile)
    outfile.close()

#run clan finder
clans()
