WORDLIST_FILENAME = "words.txt"
with(open(WORDLIST_FILENAME, 'r')) as f:
    content = [x.strip('\n') for x in f.readlines()]
# content is now a list of every word in words.txt
print("Loaded " + str(len(content)) + " words")

inputString = "bhapple"
possible = []
for word in content:
    tempString = inputString
    possibleFlag = True
    for letter in word:
        if letter not in tempString:
            possibleFlag = False
            if (word == 'apple'):
                print(letter + " is not in " + tempString)
        else:
            if (len(tempString) - 1) != inputString.index(letter):
                tempString = tempString[inputString.index(letter)+1:]
            else:
                tempString = ''
                
            #tempString = tempString.replace(letter, "")
    if possibleFlag:
        possible.append(word)
        print("**************FOUND " + word)
print(possible)
