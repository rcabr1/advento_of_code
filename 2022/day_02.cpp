#include <cstdio>

int main () {
	char abc, xyz;
	int pointsPart1 = 0;
	int pointsPart2 = 0;
	int mapperPart1[3][3] = {{4, 8, 3}, {1, 5, 9}, {7, 2, 6}};
	int mapperPart2[3][3] = {{3, 4, 8}, {1, 5, 9}, {2, 6, 7}};

	while (scanf (" %c %c", &abc, &xyz) != EOF) {
		pointsPart1 += mapperPart1[abc - 'A'][xyz - 'X'];
		pointsPart2 += mapperPart2[abc - 'A'][xyz - 'X'];
	}

	// Parte 1
	printf ("%d\n", pointsPart1);

	// Parte 2
	printf ("%d\n", pointsPart2);

	return 0;
}
