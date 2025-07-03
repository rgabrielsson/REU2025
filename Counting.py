import math
import itertools

# def test_cases():
#     testset = [9,10]

#     combos = []
#     for a in range(11):
#         for b in range(11):
#             for c in range(11):
#                 if a + b + c in testset:
#                     combos.append((a,b,c))
#                 elif a in testset:
#                     combos.append((a,b,c))
#                 elif b in testset:
#                     combos.append((a,b,c))
#                 elif c in testset:
#                     combos.append((a,b,c))
#                 elif a + b in testset:
#                     combos.append((a,b,c))
#                 elif c + b in testset:
#                     combos.append((a,b,c))
#                 elif a + c in testset:
#                     combos.append((a,b,c))


#     maxcount = 0
#     for combo in combos:
#         count = 0
#         a = combo[0]
#         b = combo[1]
#         c = combo[2]

#         if a in testset:
#             count += 1
#         if b in testset:
#             count += 1
#         if c in testset:
#             count += 1
#         if a + b in testset:
#             count += 1
#         if c + b in testset:
#             count += 1
#         if a + c in testset:
#             count += 1
#         if a + b +c in testset:
#             count += 1
#         if count > maxcount:
#             maxcount = count
#         if count == 3 and a != 1 and b != 1 and c != 1:
#             print(combo)
#             print(a+b+c)

#     #print(maxcount)


# def find_lowest_k(ving):
#     start_charge = 2**(ving-1) * (9-ving)
#     charge = 4096
#     k=12
#     while charge >= 0:
#         k=k+1
#         charge = ((math.factorial(k)/(math.factorial(ving)*math.factorial(k-ving)))*start_charge + 2**(k-1) * (14-k))/((math.factorial(k)/(math.factorial(ving)*math.factorial(k-ving)))+1)
#     print(ving)
#     print(k)
#     print(charge)
#     print("---------")


# #test_cases()


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
                families.append((a,b,c))       
    return families         
    

def families():
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
        pairings.append((total,(a,b,c)))

        #identify highest possible total charge
        if total >= worst_charge:
            worst_charge = total
    
    #find all families that give the worst possible charge
    pairings.sort()
    # for pairing in pairings:
    #     if pairing[0] == worst_charge:
    #         worst_families.append(pairing[1])
    #     if pairing[0] > 0.5*worst_charge and pairing[1][0] == 0:
    #         print(pairing)  
    
    return pairings


#families()


def generate_triple_one_clans():
    # Step 1: Generate all unordered pairs (a, b) where a <= b and the total of a+b+1 is at most 5
    all_pairs = [(a, b) for a in range(5) for b in range(a, 5) if a + b <= 4]

    # Step 2: Generate all unique sets of 3 such pairs, unordered
    unique_sets = list(itertools.combinations_with_replacement(all_pairs, 3))

    # Step 3 (Optional): Sort each pair and each set for consistency
    unique_sets = [tuple(sorted(pair_set)) for pair_set in unique_sets]

    #Step 4: Unpack unique_sets into a list of 6 values
    combinations = []
    for set in unique_sets:
        combinations.append((set[0][0],set[0][1],set[1][0],set[1][1],set[2][0],set[2][1]))

    # # Display results
    # print(f"Total unique sets: {len(unique_sets)}")
    # for s in unique_sets[:20]:  # show only first 10 for brevity
    #     print(s)

    return combinations


#get a dictionary linking clans to the type of (1,1,1) they can reduce to
def get_clan_dict(clans):
    clandict = {}
    for clan in clans:
        key = ""
        for i in range(len(clan)):
            if clan[i] == 0:
                key += "0"
            else:
                key += "1"
        if key not in clandict:
            clandict[key] = [clan]
        else:
            clandict[key].append(clan)
    return clandict



#put it all together
def test3():
    #get a list of (charge,family) pairings and make it into a dictionary linking family to the charge on that family
    pairings = families()
    familydict = {}
    for pairing in pairings:
        family = pairing[1]
        if family not in familydict:
            familydict[family] = pairing[0]
        
    #get every unique possible combination of a,b,c,d,e,f and put them in a dictionary that links them to the pattern they follow
    triple_one_clans = generate_triple_one_clans()
    clandict_111 = get_clan_dict(triple_one_clans)

    # unpack the clandictionary and iterate over it to get the averaged charge on each (1,1,1) pattern
    clanrefs = []
    worst_charge = 0
    for key,value in clandict_111.items():
        charge = 0
        num_fams = 0

        #get charge on each family and divide by number of families
        for v in value:
            family = (v[0]+v[1]+1,v[2]+v[3]+1,v[4]+v[5]+1)
            # print(family)
            # print(familydict[family])
            charge += familydict[family]
            num_fams += 1
        average_charge = charge/num_fams

        #get the worst charge over all clans
        if average_charge > worst_charge:
            worst_charge = average_charge
        clanrefs.append((average_charge,key))
    
    #get worst clans
    worst_clans = []
    for ref in clanrefs:
        if ref[0] == worst_charge:
            worst_clans.append(ref[1])

    #display worst charge and clan 
    print(worst_charge)
    print(worst_clans)
                
            
test3()














def generate_011_clans():
    # Step 1: Generate all unordered pairs (a, b) where a <= b and the total of a+b+1 is at most 5
    all_pairs = [(a, b) for a in range(5) for b in range(a, 5) if a + b <= 4]

    # Step 2: Generate all unique sets of 3 such pairs, unordered
    unique_sets = list(itertools.combinations_with_replacement(all_pairs, 2))

    # Step 3 (Optional): Sort each pair and each set for consistency
    unique_sets = [tuple(sorted(pair_set)) for pair_set in unique_sets]

    #Step 4: Unpack unique_sets into a list of 6 values
    combinations = []
    for set in unique_sets:
        combinations.append((set[0][0],set[0][1],set[1][0],set[1][1]))

    # Display results
    print(f"Total unique sets: {len(unique_sets)}")
    # for s in unique_sets[:20]:  # show only first 10 for brevity
    #     print(s)

    return combinations


#generate_011_clans()






#put it all together
def test4():
    #get a list of (charge,family) pairings and make it into a dictionary linking family to the charge on that family
    pairings = families()
    familydict = {}
    for pairing in pairings:
        family = pairing[1]
        if family not in familydict:
            familydict[family] = pairing[0]
        
    #get every unique possible combination of a,b,c,d,e,f and put them in a dictionary that links them to the pattern they follow
    clans_011 = generate_011_clans()
    clandict_011 = get_clan_dict(clans_011)

    # unpack the clandictionary and iterate over it to get the averaged charge on each (1,1,1) pattern
    clanrefs = []
    worst_charge = 0
    for key,value in clandict_011.items():
        charge = 0
        num_fams = 0

        #get charge on each family and divide by number of families
        for v in value:
            family = (0, v[0]+v[1]+1,v[2]+v[3]+1)
            # print(family)
            # print(familydict[family])
            charge += familydict[family]
            num_fams += 1
        average_charge = charge/num_fams

        #get the worst charge over all clans
        if average_charge > worst_charge:
            worst_charge = average_charge
        clanrefs.append((average_charge,key))
    
    #get worst clans
    worst_clans = []
    for ref in clanrefs:
        if ref[0] == worst_charge:
            worst_clans.append(ref[1])

    #display worst charge and clan 
    print(worst_charge)
    print(worst_clans)
                
            
test4()












def generate_001_clans():
    # Step 1: Generate all unordered pairs (a, b) where a <= b and the total of a+b+1 is at most 5
    all_pairs = [(a, b) for a in range(5) for b in range(a, 5) if a + b <= 4]

    # Display results
    print(f"Total unique sets: {len(all_pairs)}")
    # for s in all_pairs[:20]:  # show only first 10 for brevity
    #     print(s)

    return all_pairs


#generate_011_clans()






#put it all together
def test5():
    #get a list of (charge,family) pairings and make it into a dictionary linking family to the charge on that family
    pairings = families()
    familydict = {}
    for pairing in pairings:
        family = pairing[1]
        if family not in familydict:
            familydict[family] = pairing[0]
        
    #get every unique possible combination of a,b,c,d,e,f and put them in a dictionary that links them to the pattern they follow
    clans_001 = generate_001_clans()
    clandict_001 = get_clan_dict(clans_001)

    # unpack the clandictionary and iterate over it to get the averaged charge on each (1,1,1) pattern
    clanrefs = []
    worst_charge = 0
    for key,value in clandict_001.items():
        charge = 0
        num_fams = 0

        #get charge on each family and divide by number of families
        for v in value:
            family = (0, 0, v[0]+v[1]+1)
            # print(family)
            # print(familydict[family])
            charge += familydict[family]
            num_fams += 1
        average_charge = charge/num_fams

        #get the worst charge over all clans
        if average_charge > worst_charge:
            worst_charge = average_charge
        clanrefs.append((average_charge,key))
    
    #get worst clans
    worst_clans = []
    for ref in clanrefs:
        if ref[0] == worst_charge:
            worst_clans.append(ref[1])

    #display worst charge and clan 
    print(worst_charge)
    print(worst_clans)
                
            
test5()
