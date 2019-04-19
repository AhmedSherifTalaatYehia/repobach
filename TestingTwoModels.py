from gatherRandomTestData import getSubsetDataToTest
import itertools
import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer
from repobach.readingArabicFile import readingFileGenerateTrainDataV2
from spacy.tokens import Span


def wordPosition(sentence, word):
    arrayOfWords = sentence.split(" ")
    arrayOfWords = [x for x in arrayOfWords if x]
    arrayOfIndics = []
    for eachIndex in range(arrayOfWords.__len__()):
        if (arrayOfWords[eachIndex] == word):
            arrayOfIndics.append(eachIndex)
    return arrayOfIndics


def modifiedGoldNer(sentence, arrayOFEntities, arrayOfGoldNer):
    for word, entity in arrayOFEntities:
        arrayOfIndics = wordPosition(sentence, word)
        for eachIndex in range(arrayOfIndics.__len__()):
            arrayOfGoldNer[arrayOfIndics[eachIndex]] = "U-"+entity


def evaluate(ner_model, examples):
    scorer = Scorer()
    stopper=0


    for input, annot in examples:
        doc_gold_text = ner_model.make_doc(input)
        doc = ner_model(input)
        arrayOFEntities=[(ent.text, ent.label_) for ent in doc.ents]
        gold = GoldParse(doc_gold_text, entities=annot)
        print("entities is ",arrayOFEntities)
        print("sentence",input)
        print("annot is",annot)
        #for first,last,entity in annot:
            #print("word is",input[int(first):int(last)])
        #print("gold ner ",gold.ner)
        #modifiedGoldNer(input,arrayOFEntities,gold.ner)
        #print("gold ner after modified ",gold.ner)
        stopper+=1
        pred_value = ner_model(input)
        print(type(pred_value.ents))
        span=Span(pred_value,20,21,0)

        print("span type",type(span),span.label_)

        for ent in pred_value.ents:
            print("pred value is",type(ent))
            print(ent.text)
            print(ent.text,"after modified")
            print(ent.label_)
            print(ent.start)
            print(ent.end)
            #print(pred_value[ent.start:ent.end])
        #pred_value.ents=span
        print("after modification", pred_value.ents)
        print("pred_value",pred_value)
        scorer.score(pred_value, gold)
    return scorer.scores


def Testing(fileToReadArray,modelDirectory,mode,fileToRead):
    array = []
    for eachIndex in range(fileToReadArray.__len__()):
        data = readingFileGenerateTrainDataV2(fileToReadArray[eachIndex])
        array.append(data)
    if(mode):
        data = list(itertools.chain.from_iterable(array))
        Test_Data=getSubsetDataToTest(data,fileToRead)
    else:
        Test_Data=list(itertools.chain.from_iterable(array))
    print("size of TestData is",Test_Data.__len__())
    ner_model = spacy.load(modelDirectory)
    results = evaluate(ner_model, Test_Data)
    print(results)


#files=['uniqueData.txt']
#model="/home/ahmed/PycharmProjects/nlp/model2"
# True use subset data to test and not all data is used to test
#Testing(files,model,True,"/home/ahmed/PycharmProjects/nlp/miniminniSubset.txt")



