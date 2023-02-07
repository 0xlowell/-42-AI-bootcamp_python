import sys

def main():
	av = sys.argv[1::]


	print (av)

#	print (len (av))

	av = av[::-1]
	y = ""
	for i  in av:
		y += i[::-1]
		y += ' '
		
	print(y)


if __name__ == "__main__":
	main()
