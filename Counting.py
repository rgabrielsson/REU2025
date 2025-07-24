import math
import itertools

# #get rid of duplicates
# def remove_permutation_duplicates(list_of_lists):
#     seen = set()
#     result = []
#     for lst in list_of_lists:
#         key = tuple(sorted(lst))
#         if key not in seen:
#             seen.add(key)
#             result.append(lst)
#     return result

# #get charge on a given 0-ving based on formula
# def calc_charge(val):
#     charge = 2**(val-1) * (9-val) / val
#     if charge < 0:
#         charge = charge / math.comb(val,3)
#     return charge

# #get every possible family
# def get_families():
#     families = []
#     for a in range(15):
#         for b in range(15):
#             for c in range(15): 
#                 families.append((a,b,c))       
#     return families         
    
# def families():
#     families = get_families()
#     worst_charge = 0
#     worst_families = []
#     pairings = []

#     #iterate over families to find the ones with highest charge
#     for family in families:
#         a = family[0]
#         b = family[1]
#         c = family[2]
#         c3 = calc_charge(3)
#         ca = calc_charge(a+3)
#         cb = calc_charge(b+3)
#         cc = calc_charge(c+3)
#         cab = calc_charge(a+b+3)
#         cac = calc_charge(a+c+3)
#         ccb = calc_charge(b+c+3)
#         cabc = calc_charge(a+b+c+3)
#         charges = [c3,ca,cb,cc,cab,cac,ccb,cabc]
#         total = sum(charges) / len(charges)
#         pairings.append((total,(a,b,c)))

#         #identify highest possible total charge
#         if total >= worst_charge:
#             worst_charge = total
    
#     #sort and return list of families and paired charges
#     pairings.sort()
#     return pairings


# def get_combos(tup):
#     list1 = [1,tup[0]+1, tup[1]+1,tup[0]+tup[1]+1]

#     if len(tup) > 4:
#         list2 = [1,tup[2]+1, tup[3]+1,tup[2]+tup[3]+1]
#         list3 = [1,tup[4]+1, tup[5]+1,tup[4]+tup[5]+1]
#     elif len(tup) > 2:
#         list2 = [1,tup[2]+1, tup[3]+1,tup[2]+tup[3]+1]
#         list3 = [0]
#     else:
#         list2 = [0]
#         list3 = [0]

#     # Get all combinations
#     combinations = list(itertools.product(list3, list2, list1))

#     return combinations
        







# def clans001():
#     familyList = families()
#     familyDict = {}
#     for family in familyList:
#         familyDict[family[1]] = family[0]

#     #get all pairs of (a,b) that add up to at most 9
#     all_pairs = [(a, b) for a in range(10) for b in range(a, 10) if a + b <= 10]

#     #check each clan and find the worst charge
#     worst_charge = 0
#     for pair in all_pairs:
#         triple = get_combos(pair)

#         total_charge = 0 
#         items = 0 
#         for item in triple:
#             charge = familyDict[item]
#             total_charge += charge
#             items += 1
#         avgCharge = total_charge/items
#         if avgCharge > worst_charge:
#             worst_charge = avgCharge
#             worst_pair = [pair]
#         elif avgCharge == worst_charge:
#             worst_pair.append(pair)
#     print(worst_charge)
#     print(worst_pair)

# clans001()







# def clans011():
#     familyList = families()
#     familyDict = {}
#     for family in familyList:
#         familyDict[family[1]] = family[0]

#     #get all pairs of (a,b) that add up to at most 9
#     all_pairs = [(a, b, c, d) for a in range(10) for b in range(a, 10) for c in range(10) for d in range(c,10) if a + b <= 10 if c+d <=10]

#     #check each clan and find the worst charge
#     worst_charge = 0
#     for pair in all_pairs:
#         fifteen = get_combos(pair)

#         total_charge = 0 
#         items = 0 
#         for item in fifteen:
#             total_charge += familyDict[item]
#             items+= 1
#         avgCharge = total_charge/items
#         if avgCharge > worst_charge:
#             worst_charge = avgCharge
#             worst_pair = [pair]
#         elif avgCharge == worst_charge:
#             worst_pair.append(pair)

#     print(worst_charge)
#     print(worst_pair)


# #clans011()






# def clans111():
#     over70 = []
#     familyList = families()
#     familyDict = {}
#     for family in familyList:
#         familyDict[family[1]] = family[0]

#     #get all pairs of (a,b) that add up to at most 9
#     all_pairs = [(a, b, c, d, e, f) for a in range(10) for b in range(a, 10) for c in range(10) for d in range(c,10) for e in range(10) for f in range(e,10) if a + b <= 10 if c+d <=10 if e+f <=10]

#     #check each clan and find the worst charge
#     worst_charge = 0
#     for pair in all_pairs:
#         set = get_combos(pair)

#         total_charge = 0 
#         items = 0 
#         for item in set:
#             total_charge += familyDict[item]
#             items += 1
#         avgCharge = total_charge/items
#         if avgCharge > worst_charge:
#             worst_charge = avgCharge
#             worst_pair = [pair]
#         elif avgCharge == worst_charge:
#             worst_pair.append(pair)
        
#         if avgCharge > 72:
#             over70.append((f"{avgCharge:.2f}",pair))
#             #over70.append(pair)
    
#     over70.sort()  
#     # print(worst_charge)
#     # print(worst_pair)
#     return(over70)
#     #print(over70)

# #clans111()

# over70 = clans111()
# #print(over70)
# new = []
# for item in over70:
#     charge = item[0]
#     item = item[1]
#     newlst = ([item[0]+item[1]+1, item[2]+item[3]+1,item[4]+item[5]+1])
#     if newlst not in new:
#         new.append(newlst)

# cleaned = remove_permutation_duplicates(new)
# #print(cleaned)



# #print((71.75+74.2431818181818)/(2))


def calc_charge_1s(val):
    charge = 2**(val-1) * (9-val) / val
    return charge

def calc_charge_2s(val):
    charge = 2**(val-1) * (9-val) / math.comb(val,2)
    return charge


for i in range(1, 15):
    print(f"Charge for {i} is {calc_charge_1s(i)}")

print("--------------------------")

for i in range(2, 15):
    print(f"Charge for {i} is {calc_charge_2s(i)}")