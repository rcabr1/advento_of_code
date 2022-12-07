#include <cstdio>

int main () {
	char abc, xyz;
	int pointsPart1 = 0;
	int pointsPart2 = 0;

	while (scanf (" %c %c", &abc, &xyz) != EOF) {
		pointsPart1 += 1 * (xyz - 'X') + 3 * ((xyz - 'X' - abc + 'A' + 4) % 3) + 1;
		pointsPart2 += 3 * (xyz - 'X') + 1 * ((xyz - 'X' + abc - 'A' + 2) % 3) + 1;
	}

	// Parte 1
	printf ("%d\n", pointsPart1);

	// Parte 2
	printf ("%d\n", pointsPart2);

	return 0;
}
