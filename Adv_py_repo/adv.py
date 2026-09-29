# #day 1
# #Create a listed called nums containing numbers 1 thru 5
# nums = [1,2,3,4,5,]
# print(nums)
# print(nums[0])
# # teacher
# nums=[1,2,3,4,5]
# print(nums)

# squares = [n*n for n in nums]
# print(squares)

# even_map= {n:n%2==0 for n in nums}
# print(even_map)

# #Create a list containing the squares of the numbers in your nums list by looping through your list
# square = []
# for num in nums:
#     square.append(num**2)
# print(square)
# # teacher
# squares = [n*n for n in nums]
# print(squares)

# square = []
# for num in range(5):
#     square.append(num**2)
# print(square)

# #Map each number in your nums list to a Boolean value by checking 
# # whether it is even or odd
# mapping = {n:n%2==0 for n in nums}
# print(mapping)
# #teacher
# even_map= {n:n%2==0 for n in nums}
# print(even_map)


# def compute(age):
#     if age >= 18:
#         return("You are an adult")
#     else:
#         return("You are a minor")
# message= compute(18)
# print(message)

# #day 2
# fruits = ["apple", "banana", "orange", "mango"]
# print(fruits[1])
# print(fruits[-1])

# fruits = ["apple", "banana", "orange", "mango", "grape"]
# print(fruits[1:4])
# print(fruits[:3])
# print(fruits[0:6:2]) #using steps

# import numpy as np
# array = np.array([1,2,3,4,5])
# print(array)
# print(array.ndim)
# print(array.shape)


# import numpy as np
# array = np.array ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# # to access a row
# print(array[0:3])
# print(array[0:3:2])
# # to access a col for all rows we need a colon (:) prior to the col indices
# print(array[:,0])
# print(array[0,0])


#day 3
#Indexing/Slicing, Adding/Removing items 
#Indexing means accessing one specific item from a list.
#Slicing means getting a portion of a list rather than just one item
# fruits = ["apple", "banana", "orange", "mango"]
# print(fruits[1])
# print(fruits[-1])
# fruits = ["apple", "banana", "orange", "mango", "grape"]
# print(fruits[1:4])
# print(fruits[:3])
# print(fruits[0:6:2])

# #There are several ways to add/remove things to/from a list.
# fruits = ["apple", "banana"]
# fruits.append("orange")
# fruits.insert (1, "melon") 
# fruits.extend(["kiwi", "mango"])
# print(fruits)
# fruits.remove("banana") 
# fruits.pop(1) # remove by position
# del fruits[1] # delete by index

import pandas as pd
df = pd.read_csv("Airbnb.csv")
df.info
# list_A = pd.series(['A','B+', 'B+'],index = ['jack', 'mat', 'anna'])
# list_B = pd.series(['B','C+', 'C+'],index = ['zac', 'cat', 'annabel'])
