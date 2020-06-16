import dice

def parse(inputString):
    
    separated = inputString.split(' ')
    
    quantitiesAndSizes = []
    for i in range(len(separated)):
        separatedValues = separated[i].split('d')
        quantitiesAndSizes.append(separatedValues)
    # print(quantitiesAndSizes)

    # This block accounts for inputs like "d20" instead of "1d20".
    for i in range(len(quantitiesAndSizes)):
        if quantitiesAndSizes[i][0] == '':
            quantitiesAndSizes[i][0] = '1'

    '''
    # This block throws an exception if any of the values in the nested list
    # aren't integers like they're supposed to be.
    for i in range(len(quantitiesAndSizes)):
        # Modifiers
        if len(quantitiesAndSizes[i]) == 1:
            if quantitiesAndSizes[i][0] 

        # Dice Rolls
        elif len(quantitiesAndSizes[i]) == 2:
            for i in range(2):
                if
    '''

    
    return(quantitiesAndSizes)
    
        
# parse("3    + 3")
# parse("3d6+4d8")

# test = parse("3d6+4d 8  +  1")
# print(test)

# print(len(test[1]))

# print(test[1][1])

# print(parse("d20"))
