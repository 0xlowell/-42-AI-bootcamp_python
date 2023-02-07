import sys

def main():
	
	if len(sys.argv) == 1:
		print("Usage: python operations.py <number1> <number2>", '\n', "Example:", '\n', '\t', "python3 operations.py 10 3")
		sys.exit(1)
	
	else:
		if len(sys.argv) != 3:
			print ("AssertionError: more than 2 arguments are provided")
			sys.exit(1)

	av = sys.argv
	A = av[1]
	B = av[2]
	
	if A.isdigit() == False or B.isdigit() == False:
		print ("AssertionError: only integers")
		sys.exit(1)


	sum = int(A) + int(B)
	print("Sum:", sum)

	sum = int(A) - int(B)
	print ("Difference:", sum)

	sum = int(A) * int(B)
	print ("Product:", sum)
	
	if A != '0' and B != '0':
		sum = int(A) / int(B)
		print ("Quotient:", sum)
	else:
		print("Quotient:", "ERROR (division by zero)")

	if A != '0' and B != '0':
		sum = int(A) % int(B)
		print ("Remainder:", sum)
	else:
		print("Remainder:", "ERROR (modulo by zero)")

if __name__ == "__main__":
	main()

#Sum: A+B
#Difference: A-B
#Product: A*B
#Quotient: A/B
#Remainder: A%B
