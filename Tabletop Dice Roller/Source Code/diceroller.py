from dice import Die
from dice import MultiDice
from stringparser import parse

# print(dice.d4.sides)


 
while True:
    try:
        diceRollerInput = input("Enter dice roll (in the format of 3d6 d10 -2): ")
        if diceRollerInput == '':
            raise Exception("Blank input not accepted.")
        parseOutput = parse(diceRollerInput)
        # print(parseOutput)


        # Allows user to type exit to leave.
        if diceRollerInput == "exit":
            break

        runningTotal = 0
        for i in range(len(parseOutput)):
            # Modifiers
            if len(parseOutput[i]) == 1:
                modifier = int(parseOutput[i][0])
                if modifier < 0:
                    print(str(modifier))
                elif modifier >= 0:
                    print("+"+str(modifier))

                runningTotal += modifier
            # Dice Rolls
            elif len(parseOutput[i]) == 2:
                quantity = int(parseOutput[i][0])
                sides = int(parseOutput[i][1])

                # checks for valid number of sides and quantity
                if quantity <=0 or sides <=0:
                    raise Exception("Number of dice or sides cannot be zero or lower.")
                tempMultiDice = MultiDice(Die(sides), quantity)
                total, comboName, rollList = tempMultiDice.roll()
                print("+"+str(total), comboName, rollList)
                runningTotal += total
            else:
                raise Exception("Incorrect list length. It should be one or two.")

        print("Total:", runningTotal)
        
    except:
        print("Input was either incorrect format, out of range, or blank. Please try again.")
    


