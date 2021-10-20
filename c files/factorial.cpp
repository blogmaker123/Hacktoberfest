#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int n, fact = 1;
    cin >> n; // taking the input from the user......
    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }
    cout << "The factorial of the given number is" << fact << endl;
    return 0;
}