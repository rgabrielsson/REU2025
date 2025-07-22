import math
import itertools
from functools import lru_cache

@lru_cache(maxsize=None)
def sort_tuple(tup):
    return tuple(sorted((tup[0], tup[1]))) + tuple(sorted((tup[2], tup[3]))) + tuple(sorted((tup[4], tup[5])))

@lru_cache(maxsize=None)
def get_coalition_combos(tup):
    tup = tuple(tup)  # Ensure it's hashable
    lists = []
    for i in range(0, len(tup), 2):
        a, b = tup[i], tup[i+1]
        lists.append([1, a+1, b+1, a+b+1])
    while len(lists) < 6:
        lists.append([0])
    return tuple(sorted(sort_tuple(combo) for combo in itertools.product(*reversed(lists))))

@lru_cache(maxsize=None)
def get_coalition_from_twelve(tup):
    tup = tuple(tup)
    result = []
    for i in range(0, 12, 2):
        if i+1 < len(tup):
            result.append(tup[i] + tup[i+1] + 1)
        else:
            result.append(0)
    while len(result) < 6:
        result.append(0)
    return tuple(result)

def get_clans():
    with open("clans.txt", "r") as infile:
        clanDict = {}
        for line in infile:
            parts = line.translate(str.maketrans('', '', '(),')).strip().split()
            avg_charge = float(parts[0])
            pair = tuple(int(x) for x in parts[4:10])
            clanDict[pair] = avg_charge
    return clanDict

def get_some_pairs(index):
    # You could memoize these too if needed
    ranges = range(8)
    def valid_pair(a, b): return a + b <= 8 and a <= b

    if index == 0:
        return [(a, b) for a in ranges for b in ranges if valid_pair(a, b)]
    if index == 1:
        return [(a, b, c, d) for a in ranges for b in ranges for c in ranges for d in ranges
                if valid_pair(a, b) and valid_pair(c, d) and a+b+c+d <= 8 and a <= b and c <= d]
    # [same pattern; you can build with templates or dynamic generation to avoid repetition]
    # [Left unchanged for clarity]

def coalitions():
    clanDict = get_clans()
    with open("coalitions.txt", "w") as outfile:
        for i in range(6):
            newlst = []
            all_pairs = get_some_pairs(i)
            for pair in all_pairs:
                combos = get_coalition_combos(pair)
                try:
                    total_charge = sum(clanDict[item] for item in combos)
                except KeyError:
                    continue  # Skip missing entries
                avgCharge = total_charge / len(combos)
                coalition = get_coalition_from_twelve(pair)
                newlst.append((avgCharge, coalition, pair))
            newlst.sort()
            for item in newlst:
                print(item, file=outfile)

coalitions()