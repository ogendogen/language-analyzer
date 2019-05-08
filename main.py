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

        if not os.path.isdir("cleared data"):
            os.mkdir("cleared data")
        utils.writeAllText("cleared data/" + fileName, clearedData)

        # counting frequency
        lettersDict = utils.listToDict(analyzer.countLettersFreq(clearedData))
        if not os.path.isdir("letter frequency"):
            os.mkdir("letter frequency")
        utils.writeAllText("letter frequency/" + fileName, json.dumps(lettersDict))

        bigramsDict = utils.listToDict(analyzer.countBigramsFreq(clearedData))
        if not os.path.isdir("bigrams"):
            os.mkdir("bigrams")
        utils.writeAllText("bigrams/" + fileName, json.dumps(bigramsDict))

        trigramsDict = utils.listToDict(analyzer.countTrigramsFreq(clearedData))
        if not os.path.isdir("trigrams"):
            os.mkdir("trigrams")
        utils.writeAllText("trigrams/" + fileName, json.dumps(trigramsDict))

        # converting number of occurences to percentages
        lettersDictFinal = analyzer.sumPercentageToDict(lettersDict)
        bigramsDictFinal = analyzer.sumPercentageToDict(bigramsDict)
        trigramsDictFinal = analyzer.sumPercentageToDict(trigramsDict)

        lettersJsonFinal = json.dumps(lettersDictFinal, ensure_ascii = False)
        bigramsJsonFinal = json.dumps(bigramsDictFinal, ensure_ascii = False)
        trigramsJsonFinal = json.dumps(trigramsDictFinal, ensure_ascii = False)

        # printing csv files for charts
        if not os.path.isdir("csv outputs"):
            os.mkdir("csv outputs")
        utils.writeAllText("csv outputs/" + fileName.replace(".txt", "") + "-letters.txt", utils.dictToCsvString(lettersDictFinal, "|"))
        utils.writeAllText("csv outputs/" + fileName.replace(".txt", "") + "-bigrams.txt", utils.dictToCsvString(bigramsDictFinal, "|"))
        utils.writeAllText("csv outputs/" + fileName.replace(".txt", "") + "-trigrams.txt", utils.dictToCsvString(trigramsDictFinal, "|"))

        # printing final json document
        finalJson = { "letters": lettersJsonFinal, "bigrams": bigramsJsonFinal, "trigrams": trigramsJsonFinal}
        utils.writeAllText(fileName.replace(".txt", ".json"), json.dumps(finalJson, ensure_ascii=False))

    print("Finished succesfully!")

except Exception as ex:
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    if not os.path.isdir("error logs"):
        os.mkdir("error logs")
    utils.writeAllText("error logs/errorlog" + timestamp + ".log", str(ex))
    print("Error: " + str(ex))