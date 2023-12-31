# USER: ΤΟ_ΟΝΟΜΑ_ΜΟΥ_ΜΗΝ_ΞΕΧΑΣΕΙΣ_ΝΑ_ΤΟ_ΑΛΛΑΞΕΙΣ_BRO_ΘΑ_ΣΕ_ΦΑΩ
# LANG: C
# TASK: olivetrees

# Αρχικοποιούμε τις μεταβλητές απο το αρχείο εισόδου, και μια μεταβλητή για τα πιθανά εμβαδά.
N = 0
M = 0
trees_M = []
areas = []

# Πέρνουμε τις πληροφορίες που έχει το αρχείο εισόδου.
with open("olivetrees.in") as f:
    N, M = f.readline().split()
    trees_M = [int(item) for item in f.readline().split()]

N = int(N)
M = int(M)

# Μεταβλητές που κρατούν πόσες στήλες αριστερά (lstreak) και δεξιά (rstreak) έχει ελεύθερες ένας num αριθμός απο το trees_M (σχετικά με indexes).
rstreak = 0
lstreak = 0

# Για κάθε αριθμό στο trees_M, κοιτάμε πόσες ελεύθερες στήλες υπάρχουν αριστερά και δεξιά απο τον αριθμό στο trees_M.
for ind, num in enumerate(trees_M):
    for llengths in range(1, M):
        # Αν υπάρχει αριθμός στο trees_M πριν αυτόν στην θέση 'ind' του trees_M και εχει λιγότερα η ίσα δέντρα, προχωράμε, αλλιώς σταματάμε.
        if ind - llengths >= 0 and trees_M[ind - llengths] <= trees_M[ind - llengths + 1]:
            lstreak += 1
            continue
        break

    for rlengths in range(1, M):
        # Δουλεύουμε ομοίως με το παραπάνω for, απλά κοιτάμε προς τα δεξιά.
        if ind + rlengths < M and trees_M[ind + rlengths] <= trees_M[ind + rlengths - 1]:
            rstreak += 1
            continue
        break

    # Πρίν πάμε στον επόμενο αριθμό, σημειώνουμε το εμβαδό που προκύπτει απο αυτό τον αριθμό και την θέση του στο trees_M.
    areas.append((N - num) * (lstreak + rstreak + 1))
    lstreak = 0
    rstreak = 0

# Τέλος, γράφουμε την λύση στο αρχείο εξόδου.
with open("olivetrees.out", "w") as f:
    f.write(f"{max(areas)}\n")
