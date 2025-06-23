combos = []
for a in range(11):
    for b in range(11):
        for c in range(11):
            if a + b + c == 9 or a + b + c == 10:
                combos.append((a,b,c))
            elif a == 9 or a == 10:
                combos.append((a,b,c))
            elif b == 9 or b == 10:
                combos.append((a,b,c))
            elif c == 9 or c == 10:
                combos.append((a,b,c))
            elif a + b == 9 or a + b == 10:
                combos.append((a,b,c))
            elif c + b == 9 or c + b == 10:
                combos.append((a,b,c))
            elif a + c == 9 or a + c == 10:
                combos.append((a,b,c))


maxcount = 0
for combo in combos:
    count = 0
    a = combo[0]
    b = combo[1]
    c = combo[2]

    if a == 9 or a == 10:
        count += 1
    if b == 9 or b == 10:
        count += 1
    if c == 9 or c == 10:
        count += 1
    if a + b == 9 or a + b == 10:
        count += 1
    if c + b == 9 or c + b == 10:
        count += 1
    if a + c == 9 or a + c == 10:
        count += 1
    if a + b +c == 9 or a + b + c == 10:
        count += 1
    if count > maxcount:
        maxcount = count
    if count == 3:
        print(combo)

print(maxcount)