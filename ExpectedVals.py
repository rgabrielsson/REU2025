import math
import itertools

def get_clans():
    infile = open("clans14.txt", "r")
    clans_list = []
    for line in infile:
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        parts = line.strip().split()
        avg_charge = float(parts[0])
        clan = tuple(int(x) for x in parts[1:4])
        pair = tuple(int(x) for x in parts[4:10])
        clans_list.append((avg_charge, clan, pair))
    return clans_list


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
    #print(f"Generated {len(combinations)} combinations for tuple {tup}")
    return combinations



# find all families in a given clan
# for each family, find all family members
# for each family member, find the number of ways to choose num vings
# return total number of ways to choose vings
def get_vings(tup, num):
    # get all families in a clan
    families = get_combos(tup)

    #for each family, find all family members and calculated how many num-vings there are
    total_vings = 0
    for family in families:
        a = family[0]
        b = family[1]
        c = family[2]
        members = [3, a+3, b+3, c+3, a+b+3, a+c+3, b+c+3, a+b+c+3]
        count = 0
        for member in members:
            if member >= num:
                total_vings += math.comb(member,num)
            else:
                count += 1
    
        if count > 4:
            print(f"Warning: {count} family members in {family} have vings with d < {num}.")

        if a == b == c == 0:
            print(family, members, count)
    
    return total_vings



def expected_val(num):
    clans = get_clans()
    max_charge = 0
    d = 0
    for clan in clans:
        vings = get_vings(clan[2], num)

        charge = clan[0] * 8*2**len(clan[2])
        charge = charge / vings

        if charge > max_charge:
            max_charge = charge
            max_vings = vings
            d = sum(clan[1]) + 3
    print(f"Expected value for {num}: {max_charge} with d = {d} and {max_vings} vings.")
    


def main():   
    expected_val(0)
    expected_val(1)
    expected_val(2)
    expected_val(3)
    # expected_val(4)
    # expected_val(5)

main()