#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define len(x)  (sizeof(x) / sizeof((x)[0]))

int main() {
	int n_simulation = 10000;
	int n_flips = 1000;
	int heads[n_simulation];
	int mean = 0;
	srand(time(NULL));

	for (int i=0; i<n_simulation; i++) {
		int h = 0;
		for (int j=0; j<n_simulation; j++) {
			int coin = rand() % 2;
			h += coin;
		}
		heads[i] = h;
	}
	for (int x=0; x<len(heads); x++) mean += heads[x];
	mean /= n_flips;
	printf("Probability of getting head: %f", (double)mean/n_flips);
}
