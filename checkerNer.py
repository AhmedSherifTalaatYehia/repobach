# remove duplicates from an array
def removeDuplicates(array):
    uniqueEntities=[]
    for eachIndex in range(len(array)):
        if( isUnique(array[eachIndex],uniqueEntities) ):
            uniqueEntities.append(array[eachIndex]);
    return uniqueEntities;


# check if element exists in array or not
def isUnique(ElementofArray,array):
    for eachIndex in range(len(array)):
        if(array[eachIndex]==ElementofArray):
            return False;
    return True;


# check if it is name entity or not
def isEntity(entity):
    entityArray=['B-MISC', 'B-LOC', 'B-PERS', 'I-PERS', 'I-LOC', 'B-ORG', 'I-ORG', 'I-MISC']
    for eachIndex in range(len(entityArray)):
        if(entityArray[eachIndex]==entity):
            return True;
    return False;





