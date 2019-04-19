import time
from collections import Counter

import pygal

from die import Die

timestr = time.strftime("%Y%m%d-%H%M%S")
# path to saves
path = "plot_images/"


def one_or_two_dice():
    # returns whether the user wants to roll one or two dice
    while True:
        try:
            number_of_dice = int(input("How many dice do you want to roll (1 or 2):"))
        except ValueError:
            print("please input either 1 or 2")
            continue
        else:
            if number_of_dice == 1 or 2:
                return number_of_dice
                break
            else:
                continue


def number_of_sides():
    # returns the number of sides on the dice
    while True:
        try:
            sides = int(input("Please input an integer for the number of sides on the dice:"))
        except ValueError:
            print("input is not a whole number, please try again")
            continue
        else:
            return sides
            break


def number_of_rolls():
    # returns the number of rolls
    while True:
        try:
            rolls = int(input("Please input an integer for the number of times to roll the dice :"))
        except ValueError:
            print("input is not a whole number, please try again")
            continue
        else:
            return rolls
            break


def type_of_diagram():
    # returns the number of rolls
    while True:
        try:
            diagram = int(input("Select analysis: 1 = dice frequency, 2 = sum:"))
        except ValueError:
            print("please input either 1 or 2")
            continue
        else:
            if diagram == 1 or 2:
                return diagram
                break
            else:
                continue


sum_diagram = False

# ask for the number of dice to play with
number_of_dice = one_or_two_dice()

# if multiple dice see if the graph is to display the frequency of the rolls or the frequency of the sums of rolls
if number_of_dice == 2:
    responce = type_of_diagram()
    if responce == 2:
        sum_diagram = True

# get the details for the dice - number of sides
print("please input the details for dice 1")
D1_number_sides = number_of_sides()
dice1 = Die(D1_number_sides)
if number_of_dice == 2:
    # only set up second dice with custom values if user is playing with two dice, otherwise set uop with default
    print("please input the details for dice 2")
    D2_number_sides = number_of_sides()
    dice2 = Die(D2_number_sides)
else:
    dice2 = Die()
    D2_number_sides = dice2.num_sides
rolls = number_of_rolls()

# make  roll Dice and store results in a list
D1_results = []
D2_results = []
for roll in range(rolls):
    D1_result = dice1.roll()
    D1_results.append(D1_result)
    D2_result = dice2.roll()
    D2_results.append(D2_result)

# analayze the results
D1_frequencies = []
D2_frequencies = []
for value in range(1, dice1.num_sides + 1):
    frequency = D1_results.count(value)
    D1_frequencies.append(frequency)
for value in range(1, dice2.num_sides + 1):
    frequency = D2_results.count(value)
    D2_frequencies.append(frequency)

# add sum up each roll
sum_of_each_roll = []
for x in range(len(D1_results)):
    sum = D1_results[x] + D2_results[x]
    sum_of_each_roll.append(sum)





D1_sides = list(range(1, dice1.num_sides + 1))
D1_answer = list(zip(D1_sides, D1_frequencies))
D2_sides = list(range(1, dice2.num_sides + 1))
D2_answer = list(zip(D2_sides, D2_frequencies))

# output

print("\nDice has been rolled " + str(rolls) + " times \n")

# loop through the zipped tuples and print out he numbers each value has been rolled, noting that list reference from 0
print("\n\nFor DICE 1\n")
for side_value in range(1, dice1.num_sides + 1):
    side_reference = side_value - 1
    print("the number " + str(side_value) + " appears " + str(D1_answer[side_reference][1]) + " times")

# sanity check the number of rolls by adding up frequency
count = 0
for item in D1_answer:
    count += item[1]
print("sanity check of rolls by adding up frequency: " + str(count))

# if playing with 2 dice
if number_of_dice == 2:

    print("\n\nFor DICE 2\n")
    for side_value in range(1, dice2.num_sides + 1):
        side_reference = side_value - 1
        print("the number " + str(side_value) + " appears " + str(D2_answer[side_reference][1]) + " times")

    # sanity check the number of rolls by adding up frequency
    count = 0
    for item in D2_answer:
        count += item[1]
    print("Sanity check of rolls by adding up frequency: " + str(count))



D1_frequencies = []
for item in D1_answer:
    D1_frequencies.append(item[1])

D2_frequencies = []
for item in D2_answer:
    D2_frequencies.append(item[1])

# sum up the two result lists
sum_count = Counter(sum_of_each_roll)
sum_count = sorted(sum_count.items())

# visualise the results
hist = pygal.Bar()

sum_x_axis = []
for item in sum_count:
    sum_x_axis.append(item[0])

# print("x-axis= "+str(sum_x_axis))

# build diagram for the frquency of each result
if sum_diagram == False:

    hist.title = "Results of rolling " + str(number_of_dice) + " dice " + str(rolls) + " times"
    # create a set of all the sides
    sides_set = set(tuple(D1_sides)) | set(tuple(D2_sides))
    total_list_of_sides = sides_set
    hist.x_labels = total_list_of_sides
    hist.x_title = "Results"
    hist.y_title = "Frequency"

    hist.add("D" + str(D1_number_sides), D1_frequencies)
    # combine frequnecy of both dice and then produce list
    counter1 = Counter(dict(D1_answer))
    counter2 = Counter(dict(D2_answer))
    answer = counter1 + counter2
    answer = sorted(answer.items())
    combined_frequency = []
    for item in answer:
        combined_frequency.append(item[1])

    if number_of_dice == 2:
        hist.add("D" + str(D2_number_sides), D2_frequencies)
        hist.add("Combined", combined_frequency)
else:
    hist.title = "Sum of rolling Two Dice of " + str(D1_number_sides) + " and " + str(D2_number_sides) + " sides"
    # create a set of all the sides
    hist.x_labels = sum_x_axis
    hist.x_title = "Results"
    hist.y_title = "Frequency"
    sum_answers = []
    for item in sum_count:
        sum_total = item[1]
        sum_answers.append(sum_total)

    hist.add("SUM of roll", sum_answers)


hist.render_to_file(path + "diceroll_" + timestr + ".svg")

# print(sum_count)
# todo Refactor by removing the conversion of the tuple into two lists one of keys and one of values
# todo make it work with as many dice as desired - list of dice
