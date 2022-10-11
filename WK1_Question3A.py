# Question_3A
import timeit
import matplotlib.pyplot as plt
from pympler import asizeof

listA = list()


# Finding the maximum value in the list using max method
def list_max():
    global listA
    max(listA)


if __name__ == "__main__":
    # Function to track the time the list_max function takes to find the maximum value in the list
    def time_taken():
        total_time = timeit.timeit(stmt="list_max()", setup="from __main__ import list_max", number=1)
        return total_time


def graphs(): 
    x = list() #x axis in time graph and space graph, the input size 
    y = list() #y axis in time graph
    ys = list() # y axis in the space graph
    counter = 1 # just for the case of printing only one time
    counter2 = 1 # the same
    global listA
    length = int(1) #the list length everytime 

    for i in range(11): # 11 is the number of times we will increase the list size by 10 (10 then 20 then 30 then 40 then ....)
        listA.clear() # clear the list each loop to avoid confusion  
        # size = 0
        for j in range(length): # The loop to add the elemnts in the list depending on the lenght that increases by 10 each time
            listA.append(j) 
        listB = listA
        if counter < 3 and counter2 != 1: # Ignore it, it is only for the sake of printing 
            print(f"The list is: {listB}", f"The Maximum Value is {max(listB)}")
            counter += 1
        counter2 += 1
        size = asizeof.asizeof(max(listB)) # getting the size 
        ys.append(size) # make the sizes list
        y.append(time_taken()) # make the times list
        x.append(length) # make the input size list
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
    plt.xlabel("Input Size")
    plt.ylabel("Space taken")
    plt.style.use("seaborn")
    plt.show()


graphs()

# QUESTION 5
# Estimate how long each algorithm would take for inputs of size 1,000,000. Write your estimate clearly in the code.

# In this instance we were checking how long it takes to find the maximum value in a list.


# Our estimation is based on the following assumptions
# 1.We are doing this in a single processor
# 2.32bit
# 3.There is sequential execution
# 4.1 unit time for arithmetic and logic operations
# 5. We assigned one unit time for assignment
# 6.We assigned 1 unit time for return value.

# def list_max():

# global listA#declaring a list global is a single operation thus takes 1 unit time

# max(listA)#The working criteria is that it compares each value in a list by iterating through it
# thus comparing the items in the one item in list takes 1 unit time
# For our case we are comparing a list of 1000000 items, thus it would take 1000000*1unit times to compare them
# at end the method returns the maximum value, which takes 1 unit time.
# Thus total time taken =1+(1000000*1)+1=1000002 unit times.

# This is also clearly shown in our graph since most of the graphs generated for the list_max() function have a Big
# O(N), Thus the unit time increases as the size of the input increases.




