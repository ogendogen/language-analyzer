def writeAllText(filePath, text):
    f = open(filePath, "w", encoding="utf8")
    f.write(text)
    f.close()

def readAllText(filePath):
    f = open(filePath, "r", encoding="utf8")
    ret = f.read()
    f.close()
    return ret

def listToDict(inputList):
    i = iter(inputList)
    return dict(zip(i, i))

def dictToCsvString(inputDict, separator):
    outputStr = ""
    for key in inputDict:
        outputStr += key + separator + str(inputDict[key]) + "\r\n"
    return outputStr