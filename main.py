"""Author: Aldrin
   Program: First Program
   Description: An ugly Program
   Date: 5/9/2013"""

"""Function: Main
   Purpose: This is the main function
   Input: A type of cheese
   Output: A simple message"""
def main():
        # Tell the user something
	print("Welcome to the cheese shop!")

	# Get information from the user
	cheeseType = raw_input("What kind of cheese would you like?")

        # We dont have that kind
	print("Sorry, we're all out of " + cheeseType)
	
if __name__ == "__main__": main()
