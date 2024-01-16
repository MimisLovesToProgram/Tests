/* USER: username
LANG: C
TASK: olivetrees */

#include <stdio.h>
#include <stdlib.h>

/* Initializing the variables from the input file, and another variable for the possible areas. */

int main() 
{
    int N, M;
    int* trees_M;
    int* areas;

    /* Getting the data from the input file. */
    FILE* inputFile = fopen("olivetrees.in", "r");
    fscanf(inputFile, "%d %d", &N, &M);

    /* Allocating memory to the variables. */
    trees_M = (int*)malloc(M * sizeof(int));
    areas = (int*)malloc(M * sizeof(int));

    for (int i = 0; i < M; i++)
        fscanf(inputFile, "%d", &trees_M[i]);
    fclose(inputFile);

    /* For each number in trees_M, checking how many columns there are left and right of the number in trees_M. */
    for (int ind = 0; ind < M; ind++) {
        /* Variables determining how many columns left(lstreak) and right(rstreak) there are for a number 'num' from trees_M (according to indexes).*/
        int lstreak = 0, rstreak = 0;

        /* If there is a number in trees_M before the one in index position 'ind' in trees_M and has a less or equal number of trees, we move on.*/
        for (int llengths = 1; ind - llengths >= 0 && trees_M[ind - llengths] <= trees_M[ind - llengths + 1]; llengths++)
            lstreak++;

        /* Working similarly to the above 'for', just looking to the right. */
        for (int rlengths = 1; ind + rlengths < M && trees_M[ind + rlengths] <= trees_M[ind + rlengths - 1]; rlengths++)
            rstreak++;

        /* Before moving on to the next number, we store the area coming from that number and it's position in trees_M. */
        areas[ind] = (N - trees_M[ind]) * (lstreak + rstreak + 1);
    }

    /* Finally, writting the output in the output file. */
    FILE* outputFile = fopen("olivetrees.out", "w");
    int maxArea = areas[0];
    for (int i = 1; i < M; i++)
        maxArea = (areas[i] > maxArea) ? areas[i] : maxArea;

    fprintf(outputFile, "%d\n", maxArea);
    fclose(outputFile);

    /* And freeing the memory we previously allocated. */
    free(trees_M);
    free(areas);

    return 0;
}