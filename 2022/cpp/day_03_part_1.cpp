#include <iostream>
#include <bitset>

using namespace std;

int getCharBitPosition (char c) {
	return ('a' <= c && c <= 'z') ? (c - 'a') : (c - 'A' + 26);
}

int main () {
	string rucksack;
	bitset<52> compartmentBits;
	int sumPriorities = 0;

	while (getline(cin, rucksack)) {
		int rucksackSize = rucksack.size();

		compartmentBits.reset();

		for (int i = 0; i < rucksackSize / 2; i++) {
			int bitPosition = getCharBitPosition(rucksack.at(i));
			compartmentBits.set(bitPosition);			
		}

		for (int i = rucksackSize / 2; i < rucksackSize; i++) {
			int bitPosition = getCharBitPosition(rucksack.at(i));

			if (compartmentBits.test(bitPosition)) {
				sumPriorities += (bitPosition + 1);
				break;
			}
		}
	}

	cout << sumPriorities << endl;

	return 0;
}
