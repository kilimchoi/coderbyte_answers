from math import sqrt
def Division(num1, num2):
	factors = []
	greatest_divisor_so_far = 1
	for n in range(2, num1+1):
		if num1 % n == 0:
			factors.append(n)
	for factor in factors:
		if num2 % factor == 0:
			if factor > greatest_divisor_so_far:
			   greatest_divisor_so_far = factor
	return greatest_divisor_so_far
