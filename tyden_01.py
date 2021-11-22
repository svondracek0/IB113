def print_primes(n):
    for i in range(2, n + 1):
		div_count = 0
		for j in range(2, i):
			if (j % i == 0):
            	div_count += 1
        if div_count == 1:
            print (j)
