# Python program to illustrate string
# with unique characters using
# brute force technique

def uniqueCharacters(str):

	# If at any time we encounter 2
	# same characters, return false
	for i in range(len(str)):
		for j in range(i + 1,len(str)):

			if(str[i] == str[j]):
				return False

	# If no duplicate characters
	# encountered, return true
	return True


# Driver Code
word = 'Sample'

lst = list(word)
print(lst)
# if(uniqueCharacters(str)):
# 	print("The String ", str," has all unique characters");
# else:
# 	print("The String ", str, " has duplicate characters");

# This code contributed by PrinciRaj1992
