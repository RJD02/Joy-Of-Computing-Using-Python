#  Program to find out if two strings are anagram of each other

def anagram(string1, string2):
    #  If the lengths of strings don't match then we have no chance
    if len(string1) != len(string2):
        return False
    string1 = string1.lower()
    string2 = string2.lower()
    for i in string1:
        if i not in string2:
            return False
    return True

string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')
print('Are given two strings anagrams of each other?',anagram(string1, string2))
#  Our program takes O(n) unlike in course where we sort and then compare.
#  We take O(n) because the lower() also efectively scans in O(n)
#  And then we loop for once through the length of O(n)
#  Where n = len(string1) = len(string2) (Only when we have possibility of string1 and string2 being anagrams
