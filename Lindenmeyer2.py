# ECOO 2019 ROUND 1 PROBLEM 2: L-SYSTEMS GO

# this file streams our data
openFile = open("./realDATA21.txt", "r")
# this puts all the data in a list called 'lines'
lines = [x.strip() for x in openFile.readlines()]
# we start at the first element of our list
index = 0


# there are 10 data sets in the input file
for f in range(10):
    # R = first non-empty string (derived from split() method)
    numRules = int(lines[index].split()[0])
    # T = second non-empty string
    numIter = int(lines[index].split()[1])
    # A = third non-empty string
    axiom = lines[index].split()[2]

    # initializes the new axiom
    newAxiom = ""
    # creates a new list containing the next single dataset
    # uses list slicing to slice from the current index to the last rule
    dataset = lines[index:index+numRules+1]

    # repeats the loop T times
    for k in range(numIter):
        # each time the new axiom is reset to an empty string
        newAxiom = ""
        # iterates through each letter of axiom
        for j in range(len(axiom)):
            # iterates through each set of rules
            for i in range(1, numRules+1):
                # assigns variables for C and S
                letter = dataset[i][0]
                replacement = dataset[i][2:]
                if axiom[j] == letter:
                    # adds S to the new axiom
                    newAxiom += replacement
        # after each iteration, the axiom gets replaced
        axiom = newAxiom

    # prints first and last letter, no new line
    print(newAxiom[0] + newAxiom[len(newAxiom)-1], end=" ")
    # prints the number of characters
    print(len(newAxiom))
    # index goes to the next dataset
    index += numRules + 1
