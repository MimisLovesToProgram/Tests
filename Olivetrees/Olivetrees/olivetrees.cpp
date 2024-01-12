// USER: ΤΟ_ΟΝΟΜΑ_ΜΟΥ_ΜΗΝ_ΞΕΧΑΣΕΙΣ_ΝΑ_ΤΟ_ΑΛΛΑΞΕΙΣ_BRO_ΘΑ_ΣΕ_ΦΑΩ
// LANG : C
// TASK : olivetrees

#include <stdio.h>

// Αρχικοποιούμε τις μεταβλητές απο το αρχείο εισόδου, και μια μεταβλητή για τα πιθανά εμβαδά.
int N, M;
int trees_M[1000000];
int areas[1000000];

int main() {
    // Πέρνουμε τις πληροφορίες που έχει το αρχείο εισόδου.
    FILE* inputFile = fopen("olivetrees.in", "r");
    fscanf(inputFile, "%d %d", &N, &M);
    for (int i = 0; i < M; i++)
        fscanf(inputFile, "%d", &trees_M[i]);
    fclose(inputFile);

    // Για κάθε αριθμό στο trees_M, κοιτάμε πόσες ελεύθερες στήλες υπάρχουν αριστερά και δεξιά απο τον αριθμό στο trees_M.
    for (int ind = 0; ind < M; ind++) {
        // Μεταβλητές που κρατούν πόσες στήλες αριστερά(lstreak) και δεξιά(rstreak) έχει ελεύθερες ένας num αριθμός απο το trees_M(σχετικά με indexes).
        int lstreak = 0, rstreak = 0;

        // Αν υπάρχει αριθμός στο trees_M πριν αυτόν στην θέση 'ind' του trees_M και εχει λιγότερα η ίσα δέντρα, προχωράμε, αλλιώς σταματάμε.
        for (int llengths = 1; ind - llengths >= 0 && trees_M[ind - llengths] <= trees_M[ind - llengths + 1]; llengths++)
            lstreak++;

        // Δουλεύουμε ομοίως με το παραπάνω for, απλά κοιτάμε προς τα δεξιά.
        for (int rlengths = 1; ind + rlengths < M && trees_M[ind + rlengths] <= trees_M[ind + rlengths - 1]; rlengths++)
            rstreak++;

        // Πρίν πάμε στον επόμενο αριθμό, σημειώνουμε το εμβαδό που προκύπτει απο αυτό τον αριθμό και την θέση του στο trees_M.
        areas[ind] = (N - trees_M[ind]) * (lstreak + rstreak + 1);
    }

    // Τέλος, γράφουμε την λύση στο αρχείο εξόδου.
    FILE* outputFile = fopen("olivetrees.out", "w");
    int maxArea = areas[0];
    for (int i = 1; i < M; i++)
        maxArea = (areas[i] > maxArea) ? areas[i] : maxArea;

    fprintf(outputFile, "%d\n", maxArea);
    fclose(outputFile);

    return 0;
}
