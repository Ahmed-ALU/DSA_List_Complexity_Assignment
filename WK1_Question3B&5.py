import timeit
import matplotlib.pyplot as plt
from pympler import asizeof
import random

# Question_3B
strA = str()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def lowercase_conversion():
    # Taking the name from the user amd convert them into lower case by using lower() method
    global strA
    strA = strA.lower()


if __name__ == "__main__":
    # Function to track the time the list_max function takes to find the maximum value in the list
    def time_taken():
        total_time = timeit.timeit(stmt="lowercase_conversion()",
                                   setup="from __main__ import lowercase_conversion", number=1)
        return total_time


def graphs():
    global strA
    x = list() #x axis in time graph and space graph, the input size 
    y = list()#y axis in time graph
    ys = list() # y axis in the space graph
    counter = 1 # just for the case of printing only one time
    length = int(1)#the list length everytime

    for i in range(11):  # 11 is the number of times we will increase the str size by 10 (10 then 20 then 30 then 40 then ....)
        strA = ""
        for j in range(length): # increament by 10 each loop 
            letter = random.choice(alphabet) # just to add random letter to make it fair
            strA = strA + letter
        strB = strA
        size = asizeof.asizeof(strB.lower())
        ys.append(size)
        y.append(time_taken())
        if counter < 3: # ignore it it is only for the sake of printing 
            print(f"The string before lowering is {strB}")
            print(f"The string after lowering is {strA}")
            counter += 1
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

# In this instance we were checking how long it takes to  convert a string to lowercase.

# Our estimation is based on the following assumptions
# 1.We are doing this in a single processor
# 2. that is 32bit
# 3.There is sequential execution
# 4.1 unit time for arithmetic and logic operations
# 5. We assigned one unit time for assignment
# 6.We assigned 1 unit time for return value.
# The rest of the code within the function take negligible time thus not accounted for.

# def lowercase_conversion():

# global strA#declaring a variable global is a single operation thus takes 1 unit time

# strA = strA.lower()#converting a string to lowercase is single operation(assignment) irrespective of length,
# thus takes 1 unit time at end the method returns a string that has been converted to lowercase, which is a single
# operation. Thus total time taken =1+1+1=3 unit times.

# This is also clearly shown in our graph since most of the graphs generated for the lowercase conversion function
# have a Big O(1),
# Thus the unit time remains constant as the length of a string gates bigger.
