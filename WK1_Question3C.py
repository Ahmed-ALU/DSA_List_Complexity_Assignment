import timeit
from turtle import color
import matplotlib.pyplot as plt
from pympler import asizeof
import random

# Question_3C

listA = list()


# sorting the list using the given elements in ascending order
def sorting_list():
    global listA
    listA.sort()


if __name__ == "__main__":
    # Function to track the time the list_max function takes to find the maximum value in the list
    def time_taken():
        total_time = timeit.timeit(
            stmt="sorting_list()", setup="from __main__ import sorting_list", number=1)
        return total_time


def graphs():
    x = list() #x axis in time graph and space graph, the input size 
    y = list()#y axis in time graph
    ys = list() # y axis in the space graph
    counter = 1 # just for the case of printing only one time
    counter2 = 1
    length = int(1)

    for i in range(10):# 11 is the number of times we will increase the list size by 10 (10 then 20 then 30 then 40 then ....)
        listA.clear()
        for j in range(length):# increament by 10 each loop 
            randomN = random.randint(1, 1000) # add random numbers to the list to make it fair
            listA.append(randomN)
        # print (listA)
        listB = listA
        if counter < 2 and counter2 != 1: # For printing, ignore it
            print(f"The list before sorting is: {listB}", end="\n")
        size = asizeof.asizeof(listB.sort())
        if counter < 2 and counter2 != 1: # For printing, ignore it
            print(f"The list after sorting is: {listB}", end="\n")
            counter += 1
        counter2 += 1
        ys.append(size)
        y.append(time_taken())
        x.append(length)
        length += 10

    # time graph plotting
    plt.plot(x, y, marker="", markersize=10)
    plt.title("Time Verses input size Graph")
    plt.xlabel("Input Size")
    plt.ylabel("Time taken in Seconds")
    plt.style.use("seaborn")
    plt.show()

    # space graph plotting
    plt.plot(x, ys, marker="", markersize=10, color="red")
    plt.title("Space Verses input size Graph")
    plt.ylabel("Space taken")
    plt.xlabel("input size")
    plt.style.use("seaborn")
    plt.show()


graphs()

# QUESTION 5
# Estimate how long each algorithm would take for inputs of size 1,000,000. Write your estimate clearly in the code.

# In this instance we were checking how long it takes to sort values in a list.

# Our estimation is based on the following assumptions
# 1.We are doing this in a single processor
# 2. that is 32bit
# 3.There is sequential execution
# 4.1 unit time for arithmetic and logic operations
# 5. We assigned one unit time for assignment
# 6.We assigned 1 unit time for return value.
# The rest of the code within the function take negligible time thus not accounted for.

# def sorting_values():

# global listA#declaring a list global is a single operation thus takes 1 unit time

# listA.sort()#The working criteria is that it compares each value in a list by iterating through it
# thus comparing the items in the one item in list takes 1 unit time
# For our case we are comparing a list of 1000000 items, thus it would take 1000000*1unit times to compare them
# at end the method returns the sorted list, which takes 1 unit time.
# Thus total time taken =1+(1000000*1)+1=1000002 unit times.

# This is also clearly shown in our graph since most of the graphs generated for the sorting values function have a
# Big O(N), Thus the unit time increases as the size of the input increases.
