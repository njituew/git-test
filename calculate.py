def calculate(n, k, d):
	flag = False
	for digit in range(10):
		if (n * 10 + digit) % k == 0:
			n = n * 10 + digit
			flag = True
			break
	return "-1" if flag == False else str(n) + "0" * (d - 1)
