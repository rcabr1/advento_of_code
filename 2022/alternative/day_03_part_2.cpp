#include <iostream>
#include <bitset>

using namespace std;

int getCharBitPosition (char c) {
	return ('a' <= c && c <= 'z') ? (c - 'a') : (c - 'A' + 26);
}

int main () {
	string rucksack[3];
	bitset<52> compartmentBits[3];
	int sumPriorities = 0;

	while (getline(cin, rucksack[0])) {
		getline(cin, rucksack[1]);
		getline(cin, rucksack[2]);

		for (int i = 0; i < 3; i++) {
			compartmentBits[i].reset();

			for (int j = 0; j < rucksack[i].size(); j++) {
				int bitPosition = getCharBitPosition(rucksack[i].at(j));

				compartmentBits[i].set(bitPosition);
			}
		}

		bitset<52> common = compartmentBits[0] & compartmentBits[1] & compartmentBits[2];

		for (int i = 0; i < 52; i++) {
			if (common.test(i)) {
				sumPriorities += (i+1);
				break;
			}
		}
	}

	cout << sumPriorities << endl;

	return 0;
}
