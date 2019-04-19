class WordEntity:

    def __init__(self,word,nameEntity):
        self.word=word;
        self.nameEntity=nameEntity;

    def printo(self):
        print(self.word,self.nameEntity)


def trainData(arrayEntity,sentence):
    resultSet=[];
    for eachIndex in range(len(arrayEntity)):
        resultSet.append(wordLocation(arrayEntity[eachIndex],sentence))
    return resultSet


def wordLocation(wordEntity,sentence):
    ocuranceWordPosition=();
    for eachIndex in range(len(sentence)):
        wordLength=len(wordEntity.word)
        if(eachIndex+wordLength<=len(sentence)):
            if(sentence[eachIndex:eachIndex+wordLength]==wordEntity.word):
                ocuranceWordPosition=(eachIndex,eachIndex+wordLength,wordEntity.nameEntity)
                break;

    #print(ocuranceWordPosition)
    return ocuranceWordPosition;




def wordPosition(sentence,word):
    arrayOfWords=sentence.split(" ")
    arrayOfWords = [x for x in arrayOfWords if x]
    arrayOfIndics=[]
    for eachIndex in range(arrayOfWords.__len__()):
        if(arrayOfWords[eachIndex]==word):
            arrayOfIndics.append(eachIndex)
    return arrayOfIndics


sentence="Ahmed went to egypt and he was extremely delighted about it and isa Ahmed will visit us soon"
#print(wordPosition(sentence,"Ahmed"))

def modifiedGoldNer(sentence,arrayOFEntities,arrayOfGoldNer):
    for word,entity in arrayOFEntities:
        arrayOfIndics=wordPosition(sentence,word)
        for eachIndex in range(arrayOfIndics.__len__()):
            arrayOfGoldNer[arrayOfIndics[eachIndex]]=entity



# arrayOFEntities=["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
# modifiedGoldNer(sentence,[("Ahmed","PERS"),("egypt","Loc")],arrayOFEntities)
# print(arrayOFEntities)














# """
# print("hello world")
# arabicText="Google rebrands its business apps in Egypt"
# e1=WordEntity("Google","ORG")
# e2=WordEntity("Egypt","GPE")
# arrayWordEntity=[]
# arrayWordEntity.append(e1)
# arrayWordEntity.append(e2)
# print(arrayWordEntity[0].printo())
# print(trainData(arrayWordEntity,arabicText))
# print("pers is :",arabicText[37:42])
# print("location is :",arabicText[0:6])
# """
# """
# arabicText="بدأ محمود العمل في مايكروسوفت"
# print("arabic text is: ",arabicText)
#
# e1=WordEntity("محمود",'PERS')
# e2=WordEntity("مايكروسوفت",'ORG')
# arrayWordEntity=[]
# arrayWordEntity.append(e1)
# arrayWordEntity.append(e2)
#
# print(trainData(arrayWordEntity,"بدأ محمود العمل في مايكروسوفت"))
# print("pers is :",arabicText[4:10])
# print("location is :",arabicText[19:30])
#
# """


















