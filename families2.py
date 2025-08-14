"""
How many triangles?

The membership keeps increasing

There must be a rule

Ta + Tb <= Tab


Steps:
1. Get total charge for each member
2. Get charge divided by membership
3. Average based on number of contributions

Goal: minimize x, where x is at most charge_v * membership_v for each member

Linear programming




Variables: 
- membership of each family member
- charge of each family member
- visibility of each family member



Path 1:
- enumerate all cases
- use linear programming for each separately
- will take more cases and more time, but less effort
- solve for every possible visibility

Path 2:
- use code that solves for every case at once using variables
- seems smarter
- visibility charge(4) <= certain amount


Note:
- variables are not integers
- ignore for now, it will probably not matter






Worst case:
- 7 things have maximum charge = 7 * 4096
- smallest visiblity such that charge(p) * visibility(p) >= 7 * 4096
- happens really quick, at like 23

"""



"""
Notes:

- For each family member, determine how many different families it can contribute to.
- Then, give an equal share of the total charge to each family (and for each possible case)
- Now, calculate the total charge on each family in every one of these cases
- Finally, give a weighted amount of charge back to each family member based on their contribution to the families they are part of.

Thus, for each member,


visibility
cont_fams <= vis choose 3 (very naive bound, find a better one later)
charge = total charge / cont_fams ?



Goal: minimize x, where x is at most charge_v * membership_v for each member

Put in format:
Minimize :  x = charge_v * membership_v
Subject to the constraints: 
T = 3
Ta, Tb, Tc >= 3
Ta + Tb - 3 <= Tab
Ta + Tc - 3 <= Tac
Tc + Tb - 3 <= Tbc
Ta + Tb + Tc - 6 <= Tabc
d = a+b+c+3

f <= math.comb(T,3)
fa <= math.comb(Ta,3)
fb <= math.comb(Tb,3)
fc <= math.comb(Tc,3)
fab <= math.comb(Tab,3)
fac <= math.comb(Tac,3)
fbc <= math.comb(Tbc,3)
fabc <= math.comb(Tabc,3)

"""
from itertools import combinations
from scipy.optimize import linprog





# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize) 

# Create problem Variables 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0

# Objective Function
Lp_prob += 3 * x + 5 * y   

# Constraints:
Lp_prob += T == 3
Lp_prob += Ta, Tb, Tc >= 3
Lp_prob += Tab >= Ta + Tb - 3
Lp_prob += Tac >= Ta + Tc - 3
Lp_prob += Tbc >= Tc + Tb - 3
Lp_prob += Tabc >= Ta + Tb + Tc - 6

Lp_prob += f <= math.comb(T,3)
Lp_prob += fa <= math.comb(Ta,3)
Lp_prob += fb <= math.comb(Tb,3)
Lp_prob += fc <= math.comb(Tc,3)
Lp_prob += fab <= math.comb(Tab,3)
Lp_prob += fac <= math.comb(Tac,3)
Lp_prob += fbc <= math.comb(Tbc,3)
Lp_prob += fabc <= math.comb(Tabc,3)

# Display the problem
print(Lp_prob)

status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))  
