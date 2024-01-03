
# Author : Sreelakshmi Odatt Venu
#  Date Created : 18 / 12 /2023 
# Date Edited : 02/01/2023
# This is a simple madlib program in python where the user input their emotions , 
# favourite drink , programming language ,
# the and display the mad libs story 
# intitialising the variable  with the inputs

emotion = input(" Please enter your emotion: ")
drink = input (" Please enter your favourite drink: ")
programming_language = input(" Please enter the programming language you use: ")
adjective = input(" Please enter an adjective: ")
time = input(" Please enter the time you spent to code in minutes: ")
food = input (" Please enter your favourite food:  ")

# printing the output with the user-input values
print(" ")
print(" This is your Madlib Programmers Story: ")
print(" Today, as a passionate programmer, I woke up feeling " + emotion)
print(" After a quick code review and a cup of " + drink + ", I sat down with my computer.") 
print(" My first task was to implement a new feature in the " + programming_language +  " codebase.")
print(" It took me " + time + " minutes, but I felt a sense of " + adjective + " when it finally worked !")
print(" For lunch, I had my favourite food ," + food + " .")
print(" In the afternoon, I joined an engaging meeting about the upcoming software release.")
print(" By the end of the day, I was " + emotion + " but proud of my coding endeavors.")
