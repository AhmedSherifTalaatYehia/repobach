import codecs
from checkerNer import removeDuplicates;
from checkerNer import isUnique;
from checkerNer import isEntity;
from RangeSentence import trainData;
from RangeSentence import wordLocation;


class WordEntity:

    def __init__(self,word,nameEntity):
        self.word=word;
        self.nameEntity=nameEntity;

    def printo(self):
        print(self.word,self.nameEntity)


def readingFileGenerateTrainDataV2(fileToRead):
    fileReadName=codecs.open(fileToRead,encoding='utf-8') # read and write an arabic file u need encoding utf-8
    fileWriteName=open('output.txt',"w",encoding='utf-8')
    arrayWordEntity=[]
    tupleTrainData=[]
    eachArabicSentence=""
    lineNumber=1;
    lineNumberofEntity=[];
    for eachLine in fileReadName:
        splitLine=eachLine.split(" ")
        eachArabicSentence=eachArabicSentence+splitLine[0]+" "

        entity = splitLine[1][0:len(splitLine[1])-1] # to remove \n
        #print(entity)
        if (isEntity(entity)):
            wordEntity = WordEntity(splitLine[0],entity)
            arrayWordEntity.append(wordEntity)



        if(splitLine[0]=="."):
            #tuple=({ 'entities': trainData(arrayWordEntity,eachArabicSentence)},eachArabicSentence )
            tuple=(eachArabicSentence,trainData(arrayWordEntity,eachArabicSentence))
            tupleTrainData.append(tuple)
            fileWriteName.write(str(tuple)+"\n")
            if(arrayWordEntity.__len__()>0):
                lineNumberofEntity.append(lineNumber)
            eachArabicSentence=""
            arrayWordEntity = []
            lineNumber+=1


    return tupleTrainData



def readingFileGenerateTrainData(fileToRead):
    fileReadName=codecs.open(fileToRead,encoding='utf-8') # read and write an arabic file u need encoding utf-8
    fileWriteName=open('output.txt',"w",encoding='utf-8')
    arrayWordEntity=[]
    tupleTrainData=[]
    eachArabicSentence=""
    lineNumber=1;
    lineNumberofEntity=[];
    for eachLine in fileReadName:
        splitLine=eachLine.split(" ")
        eachArabicSentence=eachArabicSentence+splitLine[0]+" "

        entity = splitLine[1][0:len(splitLine[1])-1] # to remove \n
        #print(entity)
        if (isEntity(entity)):
            wordEntity = WordEntity(splitLine[0],entity)
            arrayWordEntity.append(wordEntity)



        if(splitLine[0]=="."):
            #tuple=({ 'entities': trainData(arrayWordEntity,eachArabicSentence)},eachArabicSentence )
            tuple=(eachArabicSentence,{ 'entities': trainData(arrayWordEntity,eachArabicSentence)})
            tupleTrainData.append(tuple)
            fileWriteName.write(str(tuple)+"\n")
            if(arrayWordEntity.__len__()>0):
                lineNumberofEntity.append(lineNumber)
            eachArabicSentence=""
            arrayWordEntity = []
            lineNumber+=1

    #print("Total of Entity Sentence are ",lineNumberofEntity.__len__()," and Sentences contain Entities are in line number: ")
    #print(lineNumberofEntity)
    return tupleTrainData





#print(readingFileGenerateTrainData('annOutput.txt').__len__())


