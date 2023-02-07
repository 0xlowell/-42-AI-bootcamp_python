import sys
import string

def text_analyser(text = None):
	'''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text'''
	if text == None:
		print ("What text would you analyze ?")
		text = input("text> ")
	if type(text) == int:
		print ("AssertionError: argument is not a string")
		sys.exit(1)
	space = sum(char.isspace() for char in text)
	upper = sum(char.isupper() for char in text)
	lower = sum(char.islower() for char in text)
	punct = 0
	for i in text:
		if i in string.punctuation:
			punct += 1
	print("The text contains", len(text), "character(s)")
	print("-", upper, "upper letter(s)")
	print("-", lower, "lower letter(s)")
	print("-", punct, "punctuation mark(s)")
	print("-", space, "space(s)")


def main():
	if len(sys.argv) != 2:
		print ("AssertionError more than one argument are provided")
		sys.exit(1)
	av = sys.argv[1]
	text_analyser(av)

if __name__ == "__main__":
	main()
