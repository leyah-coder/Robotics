print("What animal do you like more? Cats, Dogs or both, take this test to find out!!!")

cat_points = 0
dog_points = 0
both_points = 0

print("Lets start!!")
input("press enter to start!")

answer = input("Would you rather A go outside B stay inside C both D neither?          ")
if answer == "A" or answer == "a":
    dog_points += 1
elif answer == "B" or answer == "b":
    cat_points += 1
elif answer == "C" or answer == "c":
    cat_points += 0.5
    dog_points += 0.5
elif answer == "D" or answer == "d":
    both_points += 1

answer = input("Do you A like to soscialize B Don't C both D niether?              ")
if answer == "A" or answer == "a":
    dog_points += 1
    cat_points -= 0.5
elif answer == "B" or answer == "b":
    cat_points += 1
    dog_points -= 0.5
elif answer == "C" or answer == "c":
    cat_points += 0.5
    dog_points += 0.5
elif answer == "D" or answer == "d":
    both_points += 1

answer = input("What letter does your name start with?          ")
if answer == "A" or answer == "B" or answer == "C" or answer == "D" or answer == "E":
    dog_points += 1
    cat_points -= 0.5
elif answer == "F" or answer == "G" or answer == "H" or answer == "I" or answer == "J":
    cat_points += 1
    dog_points -= 0.5
elif answer == "K" or answer == "L" or answer == "M" or answer == "N" or answer == "O":
    cat_points += 0.5
    dog_points += 0.5
elif answer == "P" or answer == "Q" or answer == "R" or answer == "S" or answer == "T" or answer == "U" or answer == "V" or answer == "W" or answer == "X" or answer == "Y" or answer == "Z":
    both_points += 1

answer = input("How is it important to, A, have consistent engagement, B a more independent relationship, or C, don't care?              ")
if answer == "A" or answer == "a":
    dog_points += 1
    cat_points -= 0.5
elif answer == "B" or answer == "b":
    cat_points += 1
    dog_points -= 0.5
elif answer == "C" or answer == "c":
    cat_points += 0.5
    dog_points += 0.5


answer = input("What's more appealing: A a pet that's always by your side,B, one that curls up with you on its own terms, or C don't care?              ")
if answer == "A" or answer == "a":
    dog_points += 1
    cat_points -= 0.5
elif answer == "B" or answer == "b":
    cat_points += 1
    dog_points -= 0.5
elif answer == "C" or answer == "c":
    both_points += 1

answer = input("Do your friends describe you as, A, calm and playful, B, wild and crazy, or C a bit of both?         ")
if answer == "A" or answer == "a":
    cat_points += 1
elif answer == "B" or answer == "b":
    dog_points += 1
elif answer == "C" or answer == "c":
    both_points += 1


input("You like...")
# end of quiz:
if dog_points > cat_points and dog_points > both_points:
    print("DOGS MORE")
    print("WOOF!!!!")
elif cat_points > dog_points and cat_points > both_points:
    print("CATS MORE")
    print("MEOW!!!")
elif both_points > dog_points and cat_points:
        print("both!!")
elif both_points == dog_points == cat_points:
    print("Both!!!")
