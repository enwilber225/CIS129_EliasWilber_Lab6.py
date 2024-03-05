# Elias Wilber
# CIS129
# CN: 21339

# Defining main function

def main():
    totalHotDogs = 0
    totalHotDogs = getTotalHotDogs()
    showResults(totalHotDogs)

# Defining the function for how to get the total of hot dogs and guests
    
def getTotalHotDogs():
    number_of_guests = 0
    number_of_dogs = 0
    number_of_guests = int(input("What is the max number of guests?: "))
    number_of_dogs = int(input("How many hot dogs for each person?: "))
    Total = number_of_guests * number_of_dogs
    return Total

# Defining the function that will give us our results

def showResults(totalHotDogs):
    DOGS = 10
    BUNS = 8
    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0

    dogsLeft = (DOGS - totalHotDogs % DOGS) % DOGS
    minDogs = (totalHotDogs / DOGS) + (0**(0** dogsLeft))
    bunsLeft =(BUNS - totalHotDogs % BUNS) % BUNS
    minBuns = (totalHotDogs / BUNS) + (0**(0** bunsLeft))
    print("Minimum packages of hot dogs needed: ", minDogs)
    print("Minimum packages of hot dog buns needed: ", minBuns)
    print("Hot dogs remaining: ", dogsLeft)
    print("Hot dog buns remaining: ", bunsLeft)

main()

# This main ^^ is calling the main function from above, I think.
