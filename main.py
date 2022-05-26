# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if word == sorted (anagram):
        return True
    return False
#declearing function
word =input("Enter First Word: \n")
anagram =input("Enter Second Word: \n")
#checking above code
print(find_anagram(word, anagram))

