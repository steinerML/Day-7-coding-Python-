#Nested list exercises.

#1 Create a nested list

dog = ['Freddie', 'Tyson', 'James' , 'Rick' , 123.33, 9, True, 1.1, 2001, ['Callaghan', 'Whiskers'],['Install', 'Quit'],['Connection', 13.55 , False, 12, 11.84, 'Saturn is a cool planet']]

#2 Acces a nested list element by index

#Let's access the following elements:
#- 11.84 (1)
#- Connection (2)
#-Freddie (3)
#-Whiskers (4)
#Saturn is a cool planet (5)
#123.33 (6)
#True (7)
#1.1 (8)
#2001 (9)
#Callaghan (10)

print(dog[11][4]) #1
print(dog[11][0]) #2
print(dog[0]) #3
print(dog[9][1]) #4
print(dog[11][5]) #5
print(dog[4]) #6
print(dog[6]) #7
print(dog[7]) #8
print(dog[8]) #9
print(dog[9][0]) #10

#####################################

#WARNING: When accessing nested list using a positive indexation, we use a zero-based indexing!! But when we use the negative list indexing, we use a one(1)-based indexing!. As -0 does not exist, I assume :)

#3 Negative List Indexing in a Nested List
#LET'S CALL THE SAME ELEMENTS USING A NEGATIVE LIST INDEXING.

dog2 = ['Freddie', 'Tyson', 'James' , 'Rick' , 123.33, 9, True, 1.1, 2001, ['Callaghan', 'Whiskers'],['Install', 'Quit'],['Connection', 13.55 , False, 12, 11.84, 'Saturn is a cool planet']]

#Let's access the following elements:
#- 11.84 (1)
#- Connection (2)
#-Freddie (3)
#-Whiskers (4)
#Saturn is a cool planet (5)
#123.33 (6)
#True (7)
#1.1 (8)
#2001 (9)
#Callaghan (10)

print(dog2[-1][-2]) #1 (11.84)
print(dog2[-1][-6]) #2 (Connection)
print(dog2[-12]) #3 (Freddie)
print(dog2[-3][-1]) #4 (Whiskers)
print(dog2[-1][-1]) #5 (Saturn is a cool planet)
print(dog2[-8]) #6 (123.33)
print(dog2[-6]) #7 (True)
print(dog2[-5]) #8 (1.1)
print(dog2[-4]) #9 (2001)
print(dog2[-3][-2]) #10

#4 Change Nested List Item value
#We'll substitute the former values by the word 'Hola' and some integers
dog2[-1][-2]='Hola!'
dog2[-1][-6]='Hola!'
dog2[-12]='Hola!'
dog2[-3][-1]='Hola!'
dog2[-1][-1]='Hola!'
dog2[-8]=12
dog2[-6]= 99
dog2[-5]='Hola!'
dog2[-4]='Hola!'
dog2[-3][-2]= 133

#print
print(dog2[-1][-2])
print(dog2[-1][-6])
print(dog2[-12])
print(dog2[-3][-1])
print(dog2[-1][-1])
print(dog2[-8])
print(dog2[-6])
print(dog2[-5])
print(dog2[-4])
print(dog2[-3][-2])

#5 Add items to a Nested List
dog3 = ['Freddie', ['Tyson', 'James'] , ['Rick', 'Peter']]
#dog3 = ['Freddie', 'Tyson', 'James' , 'Rick' ['Callaghan', 'Whiskers'],['Install', 'Quit'],['Connection', 'Saturn']]

dog3[1].append('Added#1')
dog3[2].append('Added#2')
print(dog3)

#5.1 Insert item at a specific location in a nested list using insert ()
#Imagine we want to add a name between James and Sabrina. And also add a name before Freddie!
dog4 = ['Freddie', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
dog4[1].insert(2, 'Samantha')
print(dog4)
dog5 = ['Fred', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
dog5.insert(0,'Samantha')
print(dog5)
#Adding Samantha again next to it!
dog5.insert(1,'Samantha')
print(dog5)

#Merge lists into another using extend()
dog5 = ['Fred', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
#Merge multiple elements at the end of the list
dog5.extend([1,2,3])
print(dog5)

#Merge tuple items at the end of the list
dog6 = ['Freddie', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
dog6.extend((1,2,3))
print(dog6)

#Merge set items to a list
dog7 = ['Freddie', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
dog7.extend({1,2,3})
print(dog7)

#Add element at a certain position using insert()
#In this case, the very first element is being replaced!

dog8 = ['Freddie', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
dog8.insert(0,'ADDED via insert()')
print(dog8)

#Now we insert it in the first nested list, position 2 (between James and Sabrina)
dog9 = ['Freddie', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
dog9[1].insert(2,'ADDED via insert()')
print(dog9)

#Now we add values at the end of a nested list, in this case Nested List [1]
dog10 = ['Freddie', ['Tyson', 'James', 'Sabrina'] , ['Rick', 'Peter', 'Mathew']]
dog10[1].append('This has been appended')
print(dog10)

#Now we will merge one list into another using extend() (at the end of it)
dog11 = ['Element#1', 'Element#2', ['Element#3', 'Element#4'], 'Element#5', 'Element#6', ['Element#7', 'Element#8']]
dog11[5].extend([1,2,3])
print(dog11)

#6 Remove items from a Nested List

#We'll remove Element#3 and Element#8
dog11 = ['Element#1', 'Element#2', ['Element#3', 'Element#4'], 'Element#5', 'Element#6', ['Element#7', 'Element#8']]
x = dog11[2].pop(0)
print(dog11)
x = dog11[5].pop(1)
print(dog11)

#7 Find Nested List length
print(len(dog11))

#Find length of a given nested list, in this case NL2 (Element 3 & 4) and NL5 (Element 7 & 8)
dog12 = ['Element#1', 'Element#2', ['Element#3', 'Element#4'], 'Element#5', 'Element#6', ['Element#7', 'Element#8']]
print(len(dog12[2]))
print(len(dog12[5]))

#8 Iterate through a Nested List.

members_list = [['Peter', 22],['Martin', 25],
    ['Thomas', 19],['Sam', 25]]   
for data_field in members_list:
    print(data_field[0], "is", data_field[1], "years old.")

