from operator import itemgetter

# clears data by removing interpunction, digits, line endings, redudant spaces and converting to lower case
def clearData(data): # need to pass language name in parameter to check custom interpunction
    standardInterpunction = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?", "*"]
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    customInterpunction = list(["‘","–","—","»","«","„","“","’","”","°","¿","¡","…","¬","\t","\n","\r","\r\n"])
    outputData = ""
    for literal in data:
        if not isinstance(literal, str):
            continue
        if literal in standardInterpunction:
            continue
        if literal in customInterpunction:
            continue
        if literal in digits:
            continue
        if literal == "\n" or literal == "\r" or literal == "\r\n":
            outputData = outputData + " "
        
        outputData = outputData + literal.lower()

    return outputData

def sumPercentageToDict(inputDict):
    outputDict = dict()
    sum = 0
    for key in inputDict:
        sum += inputDict[key]
    
    for key in inputDict:
        outputDict[key] = float(inputDict[key]) / float(sum)

    return outputDict

def countLettersFreq(text):
    litery = []
    letter_dict = {}
    for letter in text:
        if letter != ' ':
            try:
                letter_dict[letter] += 1
            except KeyError:
                letter_dict[letter] = 1
    for letter in sorted(letter_dict.items(), key=itemgetter(1), reverse=True):
        litery += letter
    return litery

def countBigramsFreq(text):
    bigramy = []
    bigram_dict = {}
    bigram_holder = []
    for letter in text:
        if letter == ' ':
            bigram_holder = []
            continue
        else:
            bigram_holder.append(letter)

        if len(bigram_holder) == 2:
            bigram = bigram_holder[0] + bigram_holder[1]
            try:
                bigram_dict[bigram] += 1
            except KeyError:
                bigram_dict[bigram] = 1

            last = bigram_holder.pop()
            bigram_holder = []
            bigram_holder.append(last)

    for bigram in sorted(bigram_dict.items(), key=itemgetter(1), reverse=True):
        bigramy += bigram
    return bigramy
    
def countTrigramsFreq(text):
    trigramy = []
    trigram_dict = {}
    trigram_holder = []
    for letter in text:
        if letter == ' ':
            trigram_holder = []
            continue
        else:
            trigram_holder.append(letter)

        if len(trigram_holder) == 3:
            trigram = trigram_holder[0] + trigram_holder[1] + trigram_holder[2]
            try:
                trigram_dict[trigram] += 1
            except KeyError:
                trigram_dict[trigram] = 1

            l1 = trigram_holder.pop()
            l2 = trigram_holder.pop()
            trigram_holder = []
            trigram_holder.append(l2)
            trigram_holder.append(l1)

    for trigram in sorted(trigram_dict.items(), key=itemgetter(1), reverse=True):
        trigramy += trigram
    return trigramy