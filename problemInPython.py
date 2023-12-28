# USER: ΤΟ_ΟΝΟΜΑ_ΜΟΥ_ΜΗΝ_ΞΕΧΑΣΕΙΣ_ΝΑ_ΤΟ_ΑΛΛΑΞΕΙΣ_BRO_ΘΑ_ΣΕ_ΦΑΩ
# LANG: C
# TASK: olivetrees

N = 0
M = 0
trees_M = []
areas = []

with open("input.txt") as f:
    N, M = f.readline().split()
    trees_M = [int(item) for item in f.readline().split()]

N = int(N)
M = int(M)
rstreak = 0
lstreak = 0

# Code for area finding here
for ind, num in enumerate(trees_M):
    for llengths in range(1, M):
        if ind - llengths >= 0 and trees_M[ind - llengths] <= trees_M[ind - llengths + 1]:
            lstreak += 1
            continue
        break

    for rlengths in range(1, M):
        if ind + rlengths < M and trees_M[ind + rlengths] <= trees_M[ind + rlengths - 1]:
            rstreak += 1
            continue
        break

    areas.append((N - num) * (lstreak + rstreak + 1))
    lstreak = 0
    rstreak = 0

with open("output.txt", "w") as f:
    f.write(f"{max(areas)}\n")
