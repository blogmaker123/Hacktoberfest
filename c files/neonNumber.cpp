
#include <iostream>
using namespace std;
#include <math.h>

int checkNeon(int x)
{

	int sq = x * x;


	int sum_digits = 0;
	while (sq != 0) {
		sum_digits = sum_digits + sq % 10;
		sq = sq / 10;
	}
	return (sum_digits == x);
}

int main(void)
{
	// Printing Neon Numbers upto 10000
	for (int i = 1; i <= 10000; i++)
		if (checkNeon(i))
			cout << i << " ";
}
