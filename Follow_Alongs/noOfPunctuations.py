import string

def countPunctuation(line):
    count = 0
    for i in line:
        if i == " ":
            continue
        elif i in string.punctuation:
            count += 1
    print('There are', count, 'punctuations')

line = input('Enter a sentence:')
countPunctuation(line)
