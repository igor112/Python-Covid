####### WELCOME TO 2120 CORONA PROJECT#############
# Watch this video to get started:
# https://youtu.be/2K1LQGjOj3c
#
# You will need the us.csv data file in the same folder.
# The format of each data line is as follows:
# Lat,Date,Case,Long,Country/Region,Province/State
# Lat: latitude
# Date: a date between 2020-01-22 and 2020-04-07
# Case: the number of confirmed cases on that date
# Long: longitude
#
# Find each TODO comment in order and write your code below it.
# Do not erase comments.
# Do not write/modify code elsewhere.
# Note: Use tab to indent.
###################################################

# set up graphics and other libraries.
from tkinter import *
from time import sleep
from math import log
window = Tk()
canvas = Canvas(window, width=500, height=500, background="black")
canvas.pack()

#CUSTOM FUNCTIONS DEFINITIONS
def buildDates():
    date_list = []
    # Dates in the file are in thie follwing format: YYYY-MM-DD (Ex. 2020-01-09)
    for d in range(22, 32):
        date = "2020-01-"
        if d < 10:
            # adds a leading zero for single digit days
            date += "0"
        date_list += [date + str(d)]

    # TODO add for loop for all of february (29 days)







    # TODO add for loop for all of march (31 days)







    # TODO add for loop for 7 days of april







    return date_list

# TODO define a function called getDateFromLine()
# Input 1 string: a line from the file
# Return string: the date extracted from the line






# TODO define a function called getNumCasesFromLine()
# Input 1 string: a line from the file
# Return int: the number of confirmed cases extracted from the line






# TODO define a function called getLatFromLine()
# Input 1 string: a line from the file
# Return float: the latitude extracted from the line






# TODO define a function called getLongFromLine()
# Input 1 string: a line from the file
# Return float: the longitude extracted from the line







# TODO define a function called calcXCoord()
# Input 1 string: a line from the file
# Call the getLongFromLine() function
# Use the forumula: x = (long + 150) * 500/100
# Return int: the x pixel coord for drawing







# TODO define a function called calcYCoord()
# Input 1 string: a line from the file
# Call the getLatFromLine() function
# Use the forumula: y = 500 - (lat * 500/75)
# Return int: the y pixel coord for drawing








# TODO Uncomment the 7 lines below to define drawInfection()
# def drawInfection(oneLine):
#    x = calcXCoord(oneLine)
#    y = calcYCoord(oneLine)
#    c = getNumCasesFromLine(oneLine)
#    if c > 0:
#        r = log(c)
#        canvas.create_oval(x - r, y - r, x + r, y + r, fill="white", width=0)

def drawMapForDate(searchDate):
    # TODO Complete the drawMapForDate() function
    # Open, Read, and Loop through every line of the 'us.csv' file.
    # for each line, call the getDateFromLine() function.
    # if the date from that line is identical to the searchDate,
    # call the drawInfection() function for that line.





    #ignore, but do not erase the following line
    return

#TEST CODE HERE (Uncomment lines below to test your functions.)
sample_line = "43.28,2020-04-01,7,-91.37860,US,Iowa"
# print(repr(buildDates())) # should print all the dates up to 2020-04-07
# print(repr(getDateFromLine(sample_line))) # should print '2020-04-01'
# print(repr(getNumCasesFromLine(sample_line))) # should print 7
# print(repr(getLatFromLine(sample_line))) # should print 43.28
# print(repr(getLongFromLine(sample_line))) # should print -91.37860
# print(repr(calcXCoord(sample_line))) # should print 293
# print(repr(calcYCoord(sample_line))) # should print 211
# drawInfection(sample_line) # should draw 1 dot close to the center.

#MAIN CODE HERE
for day in buildDates():
    drawMapForDate(day)

    # grey rectangle behind date display
    canvas.create_rectangle(200, 15, 300, 35, fill="grey")
    # date display
    canvas.create_text(250, 25, text=day)

    # wait 0.25 seconds before drawing next frame
    sleep(0.25)
    canvas.update()

#finishing the drawing app
mainloop()