import time
import datetime
import os

# clears data by removing interpunction, digits, line endings, redudant spaces and converting to lower case
def clearData(data): # need to pass language name in parameter to check custom interpunction
    standardInterpunction = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?", "*"]
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    customInterpunction = list()

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

try:
    # loading up files and clearing data
    filesList = os.listdir("text samples")
    for fileName in filesList:
        f = open("text samples/" + fileName, "r", encoding="utf8", newline="\n")
        fileContent = f.read()
        f.close()
        clearedData = clearData(fileContent)
        # print("clear data")

        f = open("cleared data/" + fileName, "w", encoding="utf8")
        f.write(clearedData)
        f.close()
    
    print("Finished succesfully!")

except Exception as ex:
    time = time.time()
    timestamp = datetime.datetime.fromtimestamp(time).strftime('%Y%m%d%H%M%S')
    logFile = open("error logs/errorlog" + timestamp + ".log", "w")
    logFile.write(str(ex))
    logFile.close()
    print("Error: " + str(ex))
