file = open("dictionary.txt", "r") # Load digital dictionary file as a list of words
lst = [] # Create an empty list to hold palindromes
x = "\n"
for word in file: # Loop through each word in the word list:
    word = word.strip()
    if(len(word) > 1 and word == word[::-1]): #   If word sliced is == word sliced backward:
        lst.append(word) # Append word to the palindrome list
x = x.join(lst)
print(x) # Print palindrome list
