
#include <bits/stdc++.h>
using namespace std;

// Returns reverse of n
int reverse(int n)
{
	int rev = 0, r;
	while (n > 0) {
		r = n % 10;
		rev = rev * 10 + r;
		n /= 10;
	}
	return rev;
}

// Returns true if n is prime
bool isPrime(int n)
{
	// Corner cases
	if (n <= 1)
		return false;
	if (n <= 3)
		return true;

	if (n % 2 == 0 || n % 3 == 0)
		return false;

	for (int i = 5; i * i <= n; i = i + 6)
		if (n % i == 0 || n % (i + 2) == 0)
			return false;

	return true;
}


bool checkTwistedPrime(int n)
{
	if (isPrime(n) == false)
		return false;

	return isPrime(reverse(n));
}

// Driver Code
int main(void)
{
	// Printing Twisted Prime nbers upto 200
	cout << "First few Twisted Prime nbers are :- n";
	for (int i = 2; i <= 200; i++)
		if (checkTwistedPrime(i))
			cout << i << " ";

	return 0;
}

