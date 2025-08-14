import math

#get charge on a given 0-ving based on formula
def calc_charge(val):
    charge = 2**(val-1) * (9-val)
    if charge < 0:
        charge = charge / math.comb(val,3)
    return charge

#get every possible family
def get_families():
    families = []
    for a in range(15):
        for b in range(15):
            for c in range(15): 
                families.append((a,b,c))       
    return families         


def remove_permutation_duplicates(list_of_lists):
    seen = set()
    result = []
    for lst in list_of_lists:
        key = tuple(sorted(lst))
        if key not in seen:
            seen.add(key)
            result.append(lst)
    return result

def families():
    families = remove_permutation_duplicates(get_families())
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
        pairings.append((total,(a,b,c)))

        #identify highest possible total charge
        if total >= worst_charge:
            worst_charge = total
    
    outfile = open("families.txt","w")

    #find all families that give the worst possible charge
    pairings.sort()
    for pairing in pairings:
        print(pairing,file = outfile)
    
    outfile.close

families()
