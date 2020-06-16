from dice import Die
from dice import MultiDice
from stringparser import parse

# print(dice.d4.sides)


 
while True:
    try:
        diceRollerInput = input("Enter dice roll (in the format of 3d6 d10 -2): ")
        parseOutput = parse(diceRollerInput)
        # print(parseOutput)

        # Allows user to type exit to leave.
        if diceRollerInput == "exit":
            break

        runningTotal = 0
        for i in range(len(parseOutput)):
            if len(parseOutput[i]) == 1:
                modifier = int(parseOutput[i][0])
                if modifier < 0:
                    print(str(modifier))
                elif modifier >= 0:
                    print("+"+str(modifier))

                runningTotal += modifier
            elif len(parseOutput[i]) == 2:
                quantity = int(parseOutput[i][0])
                sides = int(parseOutput[i][1])
                tempMultiDice = MultiDice(Die(sides), quantity)
                total, comboName, rollList = tempMultiDice.roll()
                print("+"+str(total), comboName, rollList)
                runningTotal += total

        print("Total:", runningTotal)
        
    except:
        print("An error occured. Try again.")
        


