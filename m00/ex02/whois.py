import sys

def main():

	av = sys.argv
#	print (len(sys.argv))	
	if len(sys.argv)!= 2:
		print ("AssertionError more than one argument are provided")
	x = av[1]
#	print (x.isdigit())
	if (x.isdigit() == True):
		if (int(x) % 2) == 0:
			print ("The number is even")
		else:
			print ("The provided number is odd")
	else:
		print("AssertionError: argument is not an integer")
if __name__ == "__main__":
	main()
