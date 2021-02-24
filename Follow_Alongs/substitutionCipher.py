import string

def decryptFromFile(shift):
    d = {}
    for i in range(len(string.ascii_letters) - shift):
        d[string.ascii_letters[i]] = string.ascii_letters[i + shift]
    data = ""
    with open("input.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                #  print('End of file')
                break
            if c in d:
                data += d[c]
            else:
                data += c
    print('Decrypted Form:', data)

def decryptFromInput(line, shift):
    d = {}
    for i in range(len(string.ascii_letters) - shift):
        d[string.ascii_letters[i]] = string.ascii_letters[i + shift]
    data = ""
    for i in range(len(line)):
        if line[i] in d:
            data += d[line[i]]
        else:
            data += line[i]
    print('Decrypted Form:',data)

def encryptFromFile(shift):
    d = {}
    for i in range(len(string.ascii_letters)):
        d[string.ascii_letters[i]] = string.ascii_letters[i-shift]
    data = ""
    #  Displaying the contents of file
    print('Content of file is:')
    file = open("input.txt", "r")
    indiline = file.readline()
    while indiline != "":
        print(indiline)
        indiline = file.readline()
    file.close()
    with open("input.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                #  print('End of file')
                break
            if c in d:
                data += d[c]
            else:
                data += c
    print('Encrypted Form:',data)

def encryptFromInput(line, shift):
    d = {}
    for i in range(len(string.ascii_letters)):
        d[string.ascii_letters[i]] = string.ascii_letters[i - shift]
    data = ""
    for i in range(len(line)):
        if line[i] in d:
            data += d[line[i]]
        else:
            data += line[i]
    print('Encrypted Form:',data)
    #  print("The program ends here")

def main():
    print('Want me to take input from file or will you give me an input?')
    choice = 0
    print('1-Take from file')
    print('2-I will give it')
    choice = int(input('So which one will it be?'))
    key = int(input('Please enter the shift:'))
    if choice == 1:
        encryptFromFile(key)
        decryptFromFile(key)
    else:
        line = input('Please enter here:')
        encryptFromInput(line, key)
        decryptFromInput(line, key)

main() #  Kinda like OOP(C/C++/Java)
