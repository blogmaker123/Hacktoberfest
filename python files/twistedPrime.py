# Python program to check if a given number

# is Twisted Prime or not

def reverse(n) :

	rev = 0

	# reversing the nber

	while n > 0 :

		r = n % 10

		rev = rev * 10 + r

		n = n / 10

	return rev

# Returns true if n is prime, else false

def isPrime(n) :

	# Corner cases

	if (n <= 1):

		return False

	if (n <= 3):

		return True

	# This is checked so that we can skip

	# middle five nbers in below loop

	if (n % 2 == 0 or n % 3 == 0):

		return False

	i = 5

	while (i * i <= n):

		if (n % i == 0 or n % (i + 2) == 0):

			return False

		i = i + 6

	return True;

# function to check Twisted Prime nber

def checkTwistedPrime (n) :

	if (isPrime(n) == False):

		return False

	return isPrime(reverse(n))

# Driver Code

# Printing Twisted Prime nbers upto 200

print "First few Twisted Prime numbers are :- "

i = 2

while i<= 200 :

	if (checkTwistedPrime(i) == True) :

		print i,

	i = i + 1
