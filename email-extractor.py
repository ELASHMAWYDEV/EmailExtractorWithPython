file = input("Enter The File Name (for Ex aws.txt): ")
handle = open(file)
listOfEmails = list()
for line in handle:
    wordList = line.split()
    for sentence in wordList:
        if sentence.find("@") == -1:
            continue
        else:

            if sentence.find("<") == -1 and sentence.find(">") == -1:
                listOfEmails.append(sentence)
            else:
                sentence = sentence[1:-1]
                listOfEmails.append(sentence)
            #Remove Duplicates
            listOfEmails = list(dict.fromkeys(listOfEmails))
print("\n".join(listOfEmails))

        