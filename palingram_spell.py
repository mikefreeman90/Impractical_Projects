file = open("dictionary.txt", "r")# Load digital dictionary as a list of words

def find_palingram():
    palingram_list = [] # Start an empty list to hold palingrams
    for word in file: # For word in list
        word = word.split()
        end = len(word) # Get length of word
        rev_word = word[::-1]
        if(end > 1):#If Length > 1
            for i in range(end): # Loop through the letters in the word
                """If reversed word fragment at front of word is in word list and letters after form a
                palindromic sequence"""
                if(word[i:] == rev_word[:end-i] and rev_word[end-i:] in file):
                    palingram_list.append(word, rev_word[end-i:])#Append word and reversed word to palingram list
                """If reversed word fragment at end of word is in word list and letters
                before form a palindromic sequence"""
                if(word[:i] == rev_word[end-i:] and rev_word[:end-i] in file):
                    palingram_list.append(rev_word[:end-i], word) # Append reversed word and word to palingram list
    file.close()
    return palingram_list

# Sort palingram list alphabetically
palingram = find_palingram()
palingram_sorted = sorted(palingram)
print(palingram_sorted)

