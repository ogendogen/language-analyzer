import time
import datetime
import os
import json

# custom modules
import utils
import analyzer

try:
    # parsing files
    filesList = os.listdir("text samples")
    for fileName in filesList:
        # reading files and clearing data
        fileContent = utils.readAllText("text samples/" + fileName)
        clearedData = analyzer.clearData(fileContent)
        utils.writeAllText("cleared data/" + fileName, clearedData)

        # counting frequency
        lettersDict = utils.listToDict(analyzer.countLettersFreq(clearedData))
        utils.writeAllText("letter frequency/" + fileName, json.dumps(lettersDict))

        bigramsDict = utils.listToDict(analyzer.countBigramsFreq(clearedData))
        utils.writeAllText("bigrams/" + fileName, json.dumps(bigramsDict))
        
        trigramsDict = utils.listToDict(analyzer.countTrigramsFreq(clearedData))
        utils.writeAllText("trigrams/" + fileName, json.dumps(trigramsDict))

        # converting number of occurences to percentages
        lettersDictFinal = analyzer.sumPercentageToDict(lettersDict)
        bigramsDictFinal = analyzer.sumPercentageToDict(bigramsDict)
        trigramsDictFinal = analyzer.sumPercentageToDict(trigramsDict)

        lettersJsonFinal = json.dumps(lettersDictFinal, ensure_ascii = False)
        bigramsJsonFinal = json.dumps(bigramsDictFinal, ensure_ascii = False)
        trigramsJsonFinal = json.dumps(trigramsDictFinal, ensure_ascii = False)

        # printing csv files for charts
        utils.writeAllText("csv outputs/" + fileName.replace(".txt", "") + "-letters.txt", utils.dictToCsvString(lettersDictFinal, "|"))
        utils.writeAllText("csv outputs/" + fileName.replace(".txt", "") + "-bigrams.txt", utils.dictToCsvString(bigramsDictFinal, "|"))
        utils.writeAllText("csv outputs/" + fileName.replace(".txt", "") + "-trigrams.txt", utils.dictToCsvString(trigramsDictFinal, "|"))

        # printing final json document
        finalJson = { "letters": lettersJsonFinal, "bigrams": bigramsJsonFinal, "trigrams": trigramsJsonFinal}
        utils.writeAllText(fileName.replace(".txt", ".json"), json.dumps(finalJson, ensure_ascii=False))

    print("Finished succesfully!")

except Exception as ex:
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    utils.writeAllText("error logs/errorlog" + timestamp + ".log", str(ex))
    print("Error: " + str(ex))