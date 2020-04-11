# Load digital dictionary file as a list of words
file = open("dictionary.txt", "r")
# Accept a word from a user
input_word = input("Enter a word to check for anagram: >>")
# Create an empty list to hold anagrams
anagram_list = []
# Sort the user-word
input_word = input_word.lower()
user_word = sorted(input_word)
# Loop through each word in the word list:
for word in file:
    word = word.strip().lower()
    # Sort the word
    word = sorted(word)
    # if word sorted is equal to user-word sorted:
    if word == user_word:
        # Append word to anagrams list
        anagram_list.append(word)
# Print anagrams list
print(anagram_list)