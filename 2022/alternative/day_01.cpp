#include <iostream>
#include <algorithm>

using namespace std;

int main () {
	int maxSum[3] = {0, 0, 0};
	int currSum = 0;
	string s;

	while (getline(cin, s)) {
		if (s != "") {
			currSum += stoi(s);
			continue;
		}

		for (int i = 0; i < 3; i++) {
			if (currSum > maxSum[i])
				swap(currSum, maxSum[i]);
		}

		currSum = 0;
	}

	cout << maxSum[0] << endl;
	cout << maxSum[0] + maxSum[1] + maxSum[2] << endl;

	return 0;
}
