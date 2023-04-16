text = input()
longestWord = str()
mostFrequentWord = str()
cntFreqWord = 0
counter = 0
length = 0

wordList = text.split()
for i in range(len(wordList)):
    currentWord = wordList[i]
    for j in range(len(wordList)):
        if currentWord == wordList[j] and i != j:
            counter = counter + 1
            if counter > cntFreqWord:
                mostFrequentWord = currentWord
                cntFreqWord = counter

        if len(currentWord) > length:
            longestWord = currentWord
            length = len(currentWord)
    counter = 0

print("Самое частое слово: ", mostFrequentWord)
print("Самое длинное слово: ", longestWord)