from math import floor
from timeit import default_timer

team_size = {}

with open("input.txt") as f:
    first_line = f.readline().split()
    N = int(first_line[0])
    A = float(first_line[1])
    available = int(first_line[2])
    for ind, line in enumerate(f.readlines()):
        team_size[ind] = int(line)

start = default_timer()
team_value = {}
total = 0
prev = 0
prev_teams = {}

for num in range(available):
    total = 0
    for i in range(N):
        value = floor(team_value.get(i - 1, num / A) * A)
        if value >= 10:
            team_value[i] = value
            total += value * team_size[i]
        else:
            team_value[i] = 0

    if total > available:
        break
    prev = total
    prev_teams = team_value.copy()

print(prev)
for item in prev_teams.values():
    print(item)

print(f"time: {default_timer() - start}")