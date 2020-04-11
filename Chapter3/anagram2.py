import load_dictionary
file = load_dictionary.load("dictionary.txt")
anagram_list = []
# input a SINGLE word or SINGLE name below to find its anagram(s):
name = "Shaba"
print("Input name = {}".format (name))
name = name.lower()
print("Using name = {}".format (name))
# sort name & find anagrams
name_sorted = sorted(name)
for word in file:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)
# print out list of anagrams
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n')