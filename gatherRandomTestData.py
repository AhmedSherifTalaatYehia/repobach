import random
import codecs
from pathlib import Path



def getSubsetDataToTrain(array,fileToWrite):
    output_dir = Path(fileToWrite)
    if not output_dir.exists():
        fileWriteName = open(fileToWrite, "w", encoding='utf-8')
        count=int(array.__len__()*0.2)
        arrayOfRandomNumber=[]
        for i in range(count):
            arrayLastIndex=array.__len__() -1
            randomNumber = random.randint(0, arrayLastIndex)
            while(randomNumber in arrayOfRandomNumber):
                randomNumber = random.randint(0, arrayLastIndex)
            arrayOfRandomNumber.append(randomNumber)
            fileWriteName.write(str(randomNumber) + "\n")
    else:
        print("already existed and change file name ")



def getSubsetDataToTrainV2(arrayOfTuple,fileToWrite):

    fileReadName=codecs.open(fileToWrite,encoding='utf-8') # read and write an arabic file u need encoding utf-8
    array=[]
    arrayofTestTuple=[]
    for eachLine in fileReadName:
        splitLine=eachLine.split("\n")
        array.append(int(splitLine[0]))

    for eachIndex in range(arrayOfTuple.__len__() ):
        if(not (eachIndex in array) ):
            arrayofTestTuple.append(arrayOfTuple[eachIndex])
    return arrayofTestTuple


def getSubsetDataToTest(arrayOfTuple,fileToRead):

    fileReadName=codecs.open(fileToRead,encoding='utf-8') # read and write an arabic file u need encoding utf-8
    array=[]
    arrayofTestTuple=[]
    for eachLine in fileReadName:
        splitLine=eachLine.split("\n")
        array.append(int(splitLine[0]))
    for eachIndex in range(array.__len__() ):
        arrayofTestTuple.append(arrayOfTuple[array[eachIndex]])
    return arrayofTestTuple


#x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#y=x.copy()
#getSubsetDataToTrain(x)
#print("done")
#print(y.__len__())
#print(getSubsetDataToTest(y))
