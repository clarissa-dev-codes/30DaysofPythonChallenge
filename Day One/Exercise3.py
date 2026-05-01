#This is exercise 3
#I put it in a new file so that I could write the two functions rather than smushing it all together in the other file

def Euclidean(A, B):
    return sum((x-y) ** 2 for x, y in zip(A, B)) ** 0.5

dictionary = {"name":"Samantha",
              "age":25}

#Question 1 Different types
print(type(2))
print(type(3.2))
print(type(3+263j))

print(type('Hello World'))
print(type(True))
print(type(['helloworld', 16, 2.5]))
print(type(('string1', 'string2', 'string3')))
print(type({"Hello?", "Yes", "This is she"}))
print(type(dictionary)) #I made it a variable to make it more readable

#Question 2 (see Euclidean definition above)
distance = Euclidean((2,3), (10, 8))
print(distance)