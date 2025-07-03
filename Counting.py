import math
import itertools

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



def clans001():
    familyList = families()
    familyDict = {}
    for family in familyList:
        familyDict[family[1]] = family[0]

    #get all pairs of (a,b) that add up to at most 9
    all_pairs = [(a, b) for a in range(10) for b in range(a, 10) if a + b <= 10]

    #get the charge on the base family
    charge001 = familyDict[(0,0,1)]

    #check each clan and find the worst charge
    worst_charge = 0
    for pair in all_pairs:
        triple = [(0,0,pair[0]+1),(0,0,pair[1]+1),(0,0,pair[0]+pair[1]+1)]
        avgCharge = (familyDict[triple[0]] + familyDict[triple[1]] + familyDict[triple[1]] + charge001) / 4
        if avgCharge > worst_charge:
            worst_charge = avgCharge
            worst_pair = [pair]
        elif avgCharge == worst_charge:
            worst_pair.append(pair)
    print(worst_charge)
    print(worst_pair)

clans001()







def clans011():
    familyList = families()
    familyDict = {}
    for family in familyList:
        familyDict[family[1]] = family[0]

    #get all pairs of (a,b) that add up to at most 9
    all_pairs = [(a, b, c, d) for a in range(10) for b in range(a, 10) for c in range(10) for d in range(c,10) if a + b <= 10 if c+d <=10]

    #get the charge on the base family
    charge011 = familyDict[(0,1,1)]

    #check each clan and find the worst charge
    worst_charge = 0
    for pair in all_pairs:
        fifteen = [(0,1,pair[0]+1),
                   (0,1,pair[1]+1),
                   (0,1,pair[2]+1),
                   (0,1,pair[3]+1), 
                   (0,1,pair[0]+pair[1]+1),
                   (0,1,pair[2]+pair[3]+1),
                   (0,pair[0]+1,pair[2]+1),
                   (0,pair[0]+1,pair[3]+1),
                   (0,pair[1]+1,pair[2]+1),
                   (0,pair[1]+1,pair[3]+1),
                   (0,pair[0]+pair[1]+1,pair[2]+pair[3]+1),
                   (0,pair[1]+1,pair[2]+pair[3]+1),
                   (0,pair[0]+1,pair[2]+pair[3]+1),
                   (0,pair[0]+pair[1]+1,pair[3]+1),
                   (0,pair[0]+pair[1]+1,pair[2]+1)]
        total_charge = charge011
        items = 1
        for item in fifteen:
            total_charge += familyDict[item]
            items+= 1
        avgCharge = total_charge/items
        if avgCharge > worst_charge:
            worst_charge = avgCharge
            worst_pair = [pair]
        elif avgCharge == worst_charge:
            worst_pair.append(pair)
    print(worst_charge)
    print(worst_pair)

clans011()



#in progress
def clans111():
    familyList = families()
    familyDict = {}
    for family in familyList:
        familyDict[family[1]] = family[0]

    #get all pairs of (a,b) that add up to at most 9
    all_pairs = [(a, b, c, d, e, f) for a in range(10) for b in range(a, 10) for c in range(10) for d in range(c,10) for e in range(10) for f in range(e,10) if a + b <= 10 if c+d <=10 if e+f <=10]

    #get the charge on the base family
    charge111 = familyDict[(1,1,1)]

    #check each clan and find the worst charge
    worst_charge = 0
    worst_sets = []
    for pair in all_pairs:
        set = [(1,1,pair[0]+1),]
        total_charge = charge111
        items = 1
        for item in set:
            total_charge += familyDict[item]
            items += 1
        avgCharge = total_charge/items
        if avgCharge > worst_charge:
            worst_charge = avgCharge
            worst_sets.append(set)
    print(worst_charge)
    #print(worst_sets)


#clans111()
















# def generate_111_clans():
#     # Step 1: Generate all unordered pairs (a, b) where a <= b and the total of a+b+1 is at most 5
#     all_pairs = [(a, b) for a in range(5) for b in range(a, 5) if a + b <= 4]

#     # Step 2: Generate all unique sets of 3 such pairs, unordered
#     unique_sets = list(itertools.combinations_with_replacement(all_pairs, 3))

#     # Step 3 (Optional): Sort each pair and each set for consistency
#     unique_sets = [tuple(sorted(pair_set)) for pair_set in unique_sets]

#     #Step 4: Unpack unique_sets into a list of 6 values
#     combinations = []
#     for set in unique_sets:
#         combinations.append((set[0][0],set[0][1],set[1][0],set[1][1],set[2][0],set[2][1]))

#     # # Display results
#     # print(f"Total unique sets: {len(unique_sets)}")
#     # for s in unique_sets[:20]:  # show only first 10 for brevity
#     #     print(s)

#     return combinations


# #get a dictionary linking clans to the type of (1,1,1) they can reduce to
# def get_clan_dict(clans):
#     clandict = {}
#     for clan in clans:
#         key = ""
#         for i in range(len(clan)):
#             if clan[i] == 0:
#                 key += "0"
#             else:
#                 key += "1"
#         if key not in clandict:
#             clandict[key] = [clan]
#         else:
#             clandict[key].append(clan)
#     return clandict



# #put it all together
# def test3():
#     #get a list of (charge,family) pairings and make it into a dictionary linking family to the charge on that family
#     pairings = families()
#     familydict = {}
#     for pairing in pairings:
#         family = pairing[1]
#         if family not in familydict:
#             familydict[family] = pairing[0]
        
#     #get every unique possible combination of a,b,c,d,e,f and put them in a dictionary that links them to the pattern they follow
#     triple_one_clans = generate_111_clans()
#     clandict_111 = get_clan_dict(triple_one_clans)

#     # unpack the clandictionary and iterate over it to get the averaged charge on each (1,1,1) pattern
#     clanrefs = []
#     worst_charge = 0
#     for key,value in clandict_111.items():
#         charge = 0
#         num_fams = 0

#         #get charge on each family and divide by number of families
#         for v in value:
#             family = (v[0]+v[1]+1,v[2]+v[3]+1,v[4]+v[5]+1)
#             # print(family)
#             # print(familydict[family])
#             charge += familydict[family]
#             num_fams += 1
#         average_charge = charge/num_fams

#         #get the worst charge over all clans
#         if average_charge > worst_charge:
#             worst_charge = average_charge
#         clanrefs.append((average_charge,key))
    
#     #get worst clans
#     worst_clans = []
#     for ref in clanrefs:
#         if ref[0] == worst_charge:
#             worst_clans.append(ref[1])

#     #display worst charge and clan 
#     print(worst_charge)
#     print(worst_clans)
                
            
# # test3()














# def generate_011_clans():
#     # Step 1: Generate all unordered pairs (a, b) where a <= b and the total of a+b+1 is at most 5
#     all_pairs = [(a, b) for a in range(5) for b in range(a, 5) if a + b <= 4]

#     # Step 2: Generate all unique sets of 3 such pairs, unordered
#     unique_sets = list(itertools.combinations_with_replacement(all_pairs, 2))

#     # Step 3 (Optional): Sort each pair and each set for consistency
#     unique_sets = [tuple(sorted(pair_set)) for pair_set in unique_sets]

#     #Step 4: Unpack unique_sets into a list of 6 values
#     combinations = []
#     for set in unique_sets:
#         combinations.append((set[0][0],set[0][1],set[1][0],set[1][1]))

#     # Display results
#     # print(f"Total unique sets: {len(unique_sets)}")
#     # for s in unique_sets[:20]:  # show only first 10 for brevity
#     #     print(s)

#     return combinations


# #generate_011_clans()






# #put it all together
# def test4():
#     #get a list of (charge,family) pairings and make it into a dictionary linking family to the charge on that family
#     pairings = families()
#     familydict = {}
#     for pairing in pairings:
#         family = pairing[1]
#         if family not in familydict:
#             familydict[family] = pairing[0]
        
#     #get every unique possible combination of a,b,c,d,e,f and put them in a dictionary that links them to the pattern they follow
#     clans_011 = generate_011_clans()
#     clandict_011 = get_clan_dict(clans_011)

#     # unpack the clandictionary and iterate over it to get the averaged charge on each (1,1,1) pattern
#     clanrefs = []
#     worst_charge = 0
#     for key,value in clandict_011.items():
#         charge = 0
#         num_fams = 0

#         #get charge on each family and divide by number of families
#         for v in value:
#             family = (0, v[0]+v[1]+1,v[2]+v[3]+1)
#             # print(family)
#             # print(familydict[family])
#             charge += familydict[family]
#             num_fams += 1
#         average_charge = charge/num_fams

#         #get the worst charge over all clans
#         if average_charge > worst_charge:
#             worst_charge = average_charge
#         clanrefs.append((average_charge,key))
    
#     #get worst clans
#     worst_clans = []
#     for ref in clanrefs:
#         if ref[0] == worst_charge:
#             worst_clans.append(ref[1])

#     #display worst charge and clan 
#     print(worst_charge)
#     print(worst_clans)
                
            
# #test4()











#Wrong and obsolete (I think)

# def generate_001_clans():
#     # Step 1: Generate all unordered pairs (a, b) where a <= b and the total of a+b+1 is at most 5
#     all_pairs = [(a, b) for a in range(5) for b in range(a, 5) if a + b <= 5]

#     # Display results
#     # print(f"Total unique sets: {len(all_pairs)}")
#     # for s in all_pairs[:20]:  # show only first 10 for brevity
#     #     print(s)

#     return all_pairs


# #generate_011_clans()






# #put it all together
# def test5():
#     #get a list of (charge,family) pairings and make it into a dictionary linking family to the charge on that family
#     pairings = families()
#     familydict = {}
#     for pairing in pairings:
#         family = pairing[1]
#         if family not in familydict:
#             familydict[family] = pairing[0]
        
#     #get every unique possible combination of a,b,c,d,e,f and put them in a dictionary that links them to the pattern they follow
#     clans_001 = generate_001_clans()
#     clandict_001 = get_clan_dict(clans_001)

#     # unpack the clandictionary and iterate over it to get the averaged charge on each (1,1,1) pattern
#     clanrefs = []
#     worst_charge = 0
#     for key,value in clandict_001.items():
#         charge = 0
#         num_fams = 0

#         #get charge on each family and divide by number of families
#         for v in value:
#             family = (0, 0, v[0]+v[1]+1)
#             # print(family)
#             # print(familydict[family])
#             charge += familydict[family]
#             num_fams += 1
#         average_charge = charge/num_fams

#         #get the worst charge over all clans
#         if average_charge > worst_charge:
#             worst_charge = average_charge
#         clanrefs.append((average_charge,key))
    
#     #get worst clans
#     worst_clans = []
#     for ref in clanrefs:
#         if ref[0] == worst_charge:
#             worst_clans.append(ref[1])

#     #display worst charge and clan 
#     print(worst_charge)
#     print(worst_clans)
                
            
# #test5()
