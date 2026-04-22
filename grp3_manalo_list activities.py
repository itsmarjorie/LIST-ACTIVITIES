# ACTIVITY 1: CREATE A LIST

fruits = ["grapes", "apple", "mango"]
print(fruits)

# ACTIVITY 2: ACCESS ITEMS

fruits = ["apple", "banana", "cherry"]

# print first item
print(fruits[0])
# print last item
print(fruits[-1])

# ACTIVITY 3:LIST LENGTH

colors = ["red", "blue", "green", "yellow"]
print(len(colors))

# ACTIVITY 4: CHANGE ITEM

fruits = ["apple", "banana", "cherry"]

fruits[1] = "orange"
print(fruits)

# ACTIVITY 5: ADD ITEMS

fruits = ["apple", "banana"]

# Add "mango"
fruits.append("mango")

# Insert "grape" at index 1
fruits.insert(1, "grape")

print(fruits)

# ACTIVITY 6: REMOVE ITEMS

fruits = ["apple", "banana", "cherry"]

# Remove "banana"
fruits.remove("banana")

# Remove last item
fruits.pop()

print(fruits)

# ACTIVITY 7:FOR LOOP

animals = ["dog", "cat", "bird"]

for animal in animals:
  print(animals)

# ACTIVITY 8: WITH INDEX

numbers = [10, 20, 30]

for i in range(len(numbers)):
  print(i, ":", numbers[i])

# ACTIVITY 9: CHECK IF ITEM EXISTS

fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
  print("Banana is in the list")

# ACTIVITY 10: SORTING

numbers = [5, 2, 9, 1]

# Sort ascending
numbers.sort()
print(numbers)

# Sort Descending
numbers.sort(reverse=True)
print(numbers)

# ACTIVITY 11: COPY LIST

list1 = ["a", "b", "c"]

list2 = list1.copy()
print(list2)
