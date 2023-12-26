from math import floor
from timeit import default_timer

N = int(input("How many family teams/categories are there? "))
A = float(input("Enter A: "))
first_coupon_value = int(input("First coupon's value: "))
start = default_timer()
team_value = {}
total = 0

for i in range(N):
    local_families = 1 #int(input(f"How many families fall into the {i} category? "))
    value = floor(team_value.get(i - 1, first_coupon_value / A) * A)
    if value > 10:
        team_value[i] = value
        total += value
    else:
        team_value[i] = 0

    print(team_value[i])

print(total)
print(f"time: {default_timer() - start}")