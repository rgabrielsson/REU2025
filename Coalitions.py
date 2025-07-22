import math
import itertools

def sort_tuple(tup):
    pair1 = tuple(sorted((tup[0], tup[1])))
    pair2 = tuple(sorted((tup[2], tup[3])))
    pair3 = tuple(sorted((tup[4], tup[5])))
    return (pair1[0], pair1[1], pair2[0], pair2[1], pair3[0], pair3[1])


def get_coalition_combos(tup):
    lists = []
    for i in range(0, len(tup), 2):
        a, b = tup[i], tup[i+1]
        lists.append([1, a+1, b+1, a+b+1])
    while len(lists) < 6:
        lists.append([0])
    return tuple(sort_tuple(combo) for combo in itertools.product(*reversed(lists)))

        

def get_coalition_from_twelve(tup):
    if len(tup) > 10:
        return (tup[0]+tup[1]+1, tup[2]+tup[3]+1, tup[4]+tup[5]+1, tup[6]+tup[7]+1, tup[8]+tup[9]+1, tup[10]+tup[11]+1)
    elif len(tup) > 8:
        return (tup[0]+tup[1]+1, tup[2]+tup[3]+1, tup[4]+tup[5]+1, tup[6]+tup[7]+1, tup[8]+tup[9]+1, 0)
    elif len(tup) > 6:
        return (tup[0]+tup[1]+1, tup[2]+tup[3]+1, tup[4]+tup[5]+1, 0, 0, 0)
    elif len(tup) > 4:
        return (tup[0]+tup[1]+1, tup[2]+tup[3]+1, 0, 0, 0, 0)
    elif len(tup) > 2:
        return (tup[0]+tup[1]+1, 0, 0, 0, 0, 0)
    else:
        return (0, 0, 0, 0, 0, 0)


def get_clans():
    infile = open("clans.txt", "r")
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
    
    clanDict = {}
    for clan in clans_list:
        clanDict[clan[2]] = clan[0]

    return clanDict



def get_some_pairs(index):
    if index == 0:
        return [(a, b) for a in range(6) for b in range(a, 6) if a + b <= 6]
    elif index == 1:
        return [(a, b, c, d) for a in range(6) for b in range(a, 6) for c in range(6) for d in range(c, 6) if a + b <= 6 if c + d <= 6 if a + b + c + d <= 6]
    elif index == 2:
        return [(a, b, c, d, e, f) for a in range(6) for b in range(a, 6) for c in range(6) for d in range(c, 6) for e in range(6) for f in range(e, 6) if a + b <= 6 if c + d <= 6 if e + f <= 6 if a + b + c + d <= 6]
    elif index == 3:
        return [(a, b, c, d, e, f, g, h) for a in range(6) for b in range(a, 6) for c in range(6) for d in range(c, 6) for e in range(6) for f in range(e, 6) for g in range(6) for h in range(g, 6) if a + b <= 6 if c + d <= 6 if e + f <= 6 if g + h <= 6 if a + b + c + d <= 6 if e + f + g + h <= 6]
    elif index == 4:
        return [(a, b, c, d, e, f, g, h, i, j) for a in range(6) for b in range(a, 6) for c in range(6) for d in range(c, 6) for e in range(6) for f in range(e, 6) for g in range(6) for h in range(g, 6) for i in range(6) for j in range(i, 6) if a + b <= 6 if c + d <= 6 if e + f <= 6 if g + h <= 6 if i + j <= 6 if a + b + c + d <= 6 if e + f + g + h <= 6]
    elif index == 5:
        return [(a, b, c, d, e, f, g, h, i, j, k, l) for a in range(6) for b in range(a, 6) for c in range(6) for d in range(c, 6) for e in range(6) for f in range(e, 6) for g in range(6) for h in range(g, 6) for i in range(6) for j in range(i, 6) for k in range(6) for l in range(k, 6) if a + b <= 6 if c + d <= 6 if e + f <= 6 if g + h <= 6 if i + j <= 6 if k + l <= 6 if a + b + c + d <= 6 if e + f + g + h <= 6 if i + j + k + l <= 6]




def coalitions():
    clanDict = get_clans()
    outfile = open("coalitions.txt","w") 
    for i in range(6):
        all_pairs = get_some_pairs(i)

        #check each clan and find the worst charge
        newlst = []
        for pair in all_pairs:
            set = get_coalition_combos(pair)

            total_charge = 0 
            items = 0 
            for item in set:
                total_charge += clanDict[item]
                items += 1
            avgCharge = total_charge/items
            coalition = get_coalition_from_twelve(pair)

            newlst.append((avgCharge,coalition,pair))

        #write results to clans
        newlst.sort()
        for item in newlst:
            print(item,file=outfile)
    outfile.close()

coalitions()
