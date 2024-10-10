import os
# cwd =  os.getcwd()
cwd = os.path.dirname(os.path.abspath(__file__))
cwd = cwd + '\\'
print("Opening file at \'"+cwd+"\'")
def sortBest(words):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabetCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    temp = words.copy()
    for word in temp:
        for i, value in enumerate(alphabet):
            if value in word:
                alphabetCount[i] +=1
    valueOfEachWord = []
    for word in temp:
        valueOfThisWord = 0         
        seenLetter = []
        for letter in word:
            if letter not in seenLetter:
                seenLetter.append(letter)
                valueOfThisWord += alphabetCount[alphabet.index(letter)]
        valueOfEachWord.append(valueOfThisWord)

    temp = [x for _, x in sorted(zip(valueOfEachWord, temp))]
    temp.reverse()
    words = temp.copy()
    return words
inputed = input("Search in all English words or common words (\'all\' or \'common\'): ")
if inputed =="common":
    with open(cwd+'words.txt','r') as f:
        words = f.readlines()
elif inputed =="all":
    with open(cwd+'allwords.txt','r') as f:
        words = f.readlines()
else:
    print("Not Correct input!!!")
    exit(0)
    
for i, word in enumerate (words):
    if (len(word)>5):
        words[i] = word[:-1]

while (True):
    print ("Number of words Availabe:",len(words))
    print("Enter \'best\' to show best words")
    word = input("Enter your word: ")
    if word == "best":
        words = sortBest (words)
        myRange = min(10,len(words))
        for i in range(myRange):
            print(str(i+1)+". "+words[i])
        continue
    if word == "best all":
        words = sortBest (words)
        for i in range(len(words)):
            print(str(i+1)+". "+words[i])
        continue
    listOfLetters = list(word)
    if len(listOfLetters)!=5:
        print("Incorrect length! Try again")
        continue
    print("your letters are:",listOfLetters)
    listOfCorrectPositions = list(input("Enter 0,1,2 for each word: "))
    print(listOfCorrectPositions)
    if len(listOfCorrectPositions)!= 5:
        print("Incorrect length! Try again")
        continue
    for i,checking2 in enumerate(listOfCorrectPositions):
        if checking2 == '2':
            for index,value in enumerate(listOfLetters):
                if index == i:
                    continue
                if listOfLetters[i] == value and listOfCorrectPositions[index] != '2':
                    listOfCorrectPositions[index] = 1
    print(listOfCorrectPositions)
    for index in range(len(listOfLetters)):
        if listOfCorrectPositions[index] == '0':
            temp = []
            for i, value in enumerate(words):
                if listOfLetters[index] not in value:
                    temp.append(value)
            words = temp.copy()
        if listOfCorrectPositions[index] == '1':
            temp = []
            for i, value in enumerate(words):
                if listOfLetters[index] in value:
                    temp.append(value)
            words = temp.copy()
            temp = []
            for i, value in enumerate(words):
                if listOfLetters[index] != value[index]:
                    temp.append(value)
            words = temp.copy()
        if listOfCorrectPositions[index] == '2':
            temp = []
            for i, value in enumerate(words):
                if listOfLetters[index] == value[index]:
                    temp.append(value)
            words = temp.copy()
