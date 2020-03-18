# Exercise Five (Sets)

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

one = 'Eric' in friends and 'John' in friends
print(one)

two = friends.union(my_friends)
print(two)

three = friends.intersection(my_friends)
print(three)

four = friends.difference(my_friends)
print(four)

five = friends.symmetric_difference(my_friends)
print(five)

six = list(set(cars))
print(six)