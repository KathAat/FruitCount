#Gets input from customer from list of Apples, Mangos, Oranges, and Bananas and counts it all together
#once Exit is typed in. Will display the total amount of each fruit after.

#Beginning counts of the fruits. All begin with 0.
applecount = 0;
mangocount = 0;
orangecount = 0;
bananacount = 0;

#List of the possible fruits to pull from. 0: Apple, 1: Mango, 2: Orange, 3: Banana.
#Of course, this could've been done with a string or variable but lists work best!
#Took Python last semester and definitely learned lists work best.
fruits = ["Apple", "Mango", "Orange", "Banana"];

#While True: this loop will run until Exit is typed.
while True:
    #Fruitinput is the input taken from the user. It will be used to calculate the total amount later.
 fruitinput = input("Choose: Apple, Mango, Orange, Banana. To exit, type Exit. ");
    #IF the input equals to "Exit", the while loop stops and calculates all in total at the bottom.
 if fruitinput == "Exit":
  break;
    #IF input is equal to Apple, the apple count gets +1. applecount += 1 is essentially saying
    #applecount = applecount + 1. The apple count will continue to get +1 until exit is inputted.
 if fruitinput == fruits[0]:
  applecount += 1;
 if fruitinput == fruits[1]:
  mangocount += 1;
 if fruitinput == fruits[2]:
  orangecount += 1;
 if fruitinput == fruits[3]:
  bananacount += 1;


#Printing the total ending amount of each fruit with lines divided. It's taking the new total count
#after the loop ends and placing it into the variable and printing it out.
print("\nApples:", applecount, "\nMangos:", mangocount,"\nOranges:", orangecount,"\nBananas:", bananacount);