1. Write a function that takes two string inputs, **target** and **text**. Your function will search the **text** string and check if it contains **target** in it as a substring. If it does, you need to return a new string that is the same as text, but with the target substring reversed inside it. 
Example:

`find_and_reverse("reverse me", "sample text reverse me1234")`
> test string em esrever1234


2. Write a function that reads inputs from the user until they enter an empty string. Then it should print out the first characters of each input in one line, then print the second characters of every line in another line, until you print all the characters you have read. 
Example:

`flip_input()`
> Enter your text:
> Abc
> 12345
> x
> test

>Printing the output:
> A1xt
> b2 e
> c3 s
> 4 t
> 5


3. Write a function that takes an integer **shift** and a string **text** as input. Your functions should return a new string that is the same as text, but every word separated by white-spaces should have its first **shift** characters moved to the end of the string. 
Example:

`shift(3, "Welcome to COMP100")`
>"comeWel to P100COM"


4. Write a function that takes a string **text** as input. Look at the first word of the text, and let N be the number of vowels in that word. You must take every N’th letter of the text, let this new string be called ntext. Then, look at the character of ntext that is right in the middle (Take the left character in case of a tie). Replace all copies of that letter in ntext with a question mark (?) and print the result. 
Example:

`obfuscate("Here is a very strange question")`
> eei??eysrneqeto


5. Write a function that takes a string **text** as input. You should search the input text for anagrams. An anagram is a word that is created by rearranging the letters of another word. When you find that A word in the text is an anagram of another word, you should capitalize both words. Words might be separated by spaces, commas or periods (Suggestion: you can "import re" and use re.split for regex based splitting). Return a string with all anagrams capitalized. Be careful not to capitalize words that are exactly the same. 
Example:

`loud_anagrams("Lately I have been in a stressed state. I have been comforting myself with the taste of desserts.")`
> "Lately I have been in a STRESSED STATE. I have been comforting myself with the TASTE of DESSERTS."


6. Write a function that takes a sorted list of integers `int_list` and an integer target as input. Your function should determine if the target exists inside the `int_list` or not, using the bisection search.


7. You have a list called colourList such that; `colourList = ['red', 'yellow', 'green', 'white']`. Please create a new empty list called `mixedColours`. This new list will contain colour blends of two neighbouring colours, such that 

`mixedColours = ['redyellow', 'yellowgreen' , 'greenwhite']`

Print the `mixedColours`.


8. Please write a function that takes a number and checks if it is a factorial. For examples, the function should return `True` for 24 and return `False` for 36.


9. There is an array of numbers called `arr` represented as a list: `arr = [25, 11, 7, 75, 56]`. Please write a program to find the smallest number in that array.


10. Write a function to check if a triangle is right angled or not. The function should accept 3 numbers (indicating the edges of a traiangle) and return a boolean.


11. Write a function to find the sum of the series 

> 2 + 22 + 222 + 2222 + ...

for n terms. Your function should take n as an input and return the sum. For example, for n = 3, the function should return 246. (2 + 22 + 222 = 246). 

Also, write another function that takes two inputs k and n. For example, for k = 5, n = 4 the function should return the sum of 

> 5 + 55 + 555 + 5555


12. Write a function to reverse the string in a recursive way. Your implementation should be recursive and you should not use any loops.


13. Write a function which checks the given integer is prime or not in a recursive way. Your implementation should be recursive and you should not use any loops. 

**Hint:** You need to check if the given integer is divisible by all the number up until the square root of the given integer. 

For example, for 13, it is enough to check if numbers, 2,3,4 do not divide 13, we can say that is a prime number.


14. Write a function which takes two dictionaries as parameters and returns the summation of the dictionaries. The summation can be defined as element-wise sum for each element. You can assume the keys that do not appear in the dictionaries have a value of 0.

> {'a': 100, 'b': 200, 'c': 300} + {'a': 300, 'b': 200, 'd': 400} -> {'a': 400, 'b': 400, 'c': 300, 'd': 400}


15. Write a recursive function that returns the maximum element of the list. Your implementation should be recursive and you should not use any loops.


16. Find the sum of elements in the list which can contain lists as elements. Some example cases:

> [1,2,[3,4],5] -> 15
> [1,[2,3],[[4,5],6]] -> 21
> [[1,[2,[3,[4,[5,[6,[7,[8,[9,[10]]]]]]]]]]] -> 55


17. 
```
StarkSiblings = ['Arya', 'Robb', 'Jon', 'Bran', 'Sansa', 'Rickon']
StarkParents = ['Ned', 'Catlyn']
LannisterSiblings = ['Tyrion', 'Jamie', 'Cersei']
LannisterParents = ['Tywin', 'Joanna']
TargaryenSiblings = ['Rhaegar', 'Viserys', 'Daenerys']
TargaryenParents = ['Aerys', 'Rhaella']
```

Given the three most famous families from the GoT universe, write a match-making function to randomly pick two people to marry from the universe, and print a judgement either by:

* printing a message approving their union
* warning if at least one of them is already married
* asking "why again" if they are married as a couple
* disapproving if they are siblings, or if they have a child-parent relationship with separate messages
* (bonus) a cynical disapproval if the couple is Jamie and Cersei
* (bonus) a special warning if the couple is Jon and Daenerys

**Hint:** You can use assertions for very strong disapprovals.


18. Describe what a path-complete test is and suggest a path-complete test for the program you wrote in Question 17.


19. Let's say we are collecting information from a user by asking them basic questions such as their name, age, profession, telephone number, and address. By using a try block and appropriate exceptions, make sure that user enters a valid input for each, e.g. string for the name, the profession, and the address; and int for the age and the telephone number. Persistently ask for the input in the right format by properly informing the user, as long as they enter it wrong.

* Take care of the cases (by accepting and converting them to the int format) where the user puts space or dash in the phone number or enters parantheses for the area code.
* Reject the entry if the user is older than 100 or younger than 10.
* Try to format the address in a more fine-grained way by asking the street name, house number, zip code, city etc. separately with proper types for each.


20. Given the specification below, propose some black box testing cases for the gcd function we wrote in the class. How many test cases can you find that fails for our function? Use the same test cases on math module's gcd function: `math.gcd()`. Lastly, try to make our implementation bulletproof.

> Return the greatest common divisor of the specified two integer arguments. If any of the arguments is nonzero, then the returned value is the largest positive integer that is a divisor of both arguments. If both arguments are zero, then the returned value is 0. `gcd()` without arguments returns 0.


21. Given the program to get the next day of a given date, propose some glass box testing cases. State if your test is path-complete.

https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year

```
def tomorrow(date):
  (year, month, day) = date

  if (year % 400 == 0):
      leap_year = True
  elif (year % 100 == 0):
      leap_year = False
  elif (year % 4 == 0):
      leap_year = True
  else:
      leap_year = False

  if month in (1, 3, 5, 7, 8, 10, 12):
      month_length = 31
  elif month == 2:
      if leap_year:
          month_length = 29
      else:
          month_length = 28
  else:
      month_length = 30

  if day < month_length:
      day += 1
  else:
      day = 1
      if month == 12:
          month = 1
          year += 1
      else:
          month += 1
  print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

  return (year, month, day)
```


22. You are given two functions that are intended to increase x by 100. Check whether they are working or not by drawing variable scope diagrams for each.

Code 1: 

```
x = 200
def increment(x):
    x += 100
    return x

x = increment(x)

```

Code 2:

```
x = 200
def increment():
    x += 100

increment()
```


23. In this question you are asked to implement a registration system. As a practice of decomposition, we will implement the functionality of a user registration system with small functions. The skeleton code is given to you beforehand in the main function, implement the missing parts with the provided information below.

The `db` is a tuple with two variables, which holds the information of our database. The `id_counter` variable counts the ids that are registered in the database. In each registration, you need to increment it by 1. In each deletion, you don’t have to modify its value. The `user_dict` variable is a dictionary.  Use names as dictionary keys and values as user ids.

Complete the missing parts. Compare your implementation's result to the provided output.


```
def print_user(id,name):

    print(f'User ID: {id} with name {name}')

def printerr(name):

    print(f'Error! User {name} doesn’t exist!')

def adduser(db, name):

    id_counter, user_dict  = db

    # START OF YOUR CODE
    #
    # END OF YOUR CODE

    return (id_counter, user_dict)

def addusers(db, name_list):

    # START OF YOUR CODE
    #
    # END OF YOUR CODE

    return db

def find_user_by_name(db, name):
    
    print(f"Searching... {name}")
    id_counter, user_dict  = db 

    # START OF YOUR CODE
    #
    # END OF YOUR CODE

def print_users(db):

    id_counter, user_dict  = db

    # START OF YOUR CODE
    #
    # END OF YOUR CODE

def delete(db,name):

    id_counter, user_dict  = db
    print(f'Deleting... {name}')

    # START OF YOUR CODE
    #
    # END OF YOUR CODE
    
    return (id_counter, user_dict)

def main():

    id_counter = 0
    user_dict = {}
    db = (id_counter, user_dict)

    # Add a user 
    db = adduser(db, 'Ece')

    # Add users given a list of names
    db = addusers(db, ['Ali', 'Erhan', 'Betül', 'Esra'])

    # Prints its ID with name
    find_user_by_name(db, 'Erhan')

    # Delete Betül
    db = delete(db, 'Betül')
    
    # Prints its ID with name
    find_user_by_name(db, 'Betül')

    # Raise an error.
    db = delete(db, 'Hayati')

    # Print all
    print_users(db)


if __name__ == '__main__':
    main()

```

True output:

> User ID: 1 with name Ece
> User ID: 2 with name Ali
> User ID: 3 with name Erhan
> User ID: 4 with name Betül
> User ID: 5 with name Esra
> Searching... Erhan
> Found!
> User ID: 3 with name Erhan
> Deleting... Betül
> Searching... Betül
> Error! User Betül doesn’t exist!
> Deleting... Hayati
> Error! User Hayati doesn’t exist!
> User ID: 1 with name Ece
> User ID: 2 with name Ali
> User ID: 3 with name Erhan
> User ID: 5 with name Esra


24. Fill in the blanks and select the correct option.

* We (can/can't) define functions inside functions in Python. 
* We (can/can't) pass a function to another function as an argument in Python.
* When a function call is made, the ……… parameters of the caller are (copied/passed) to ……… parameters. Hence, the function cannot modify the parameters original value unless we return it. If we don't write a return statement, the value of the returned variable is ……… by default.


25. Suppose we provide a function `valid_triangle(x1, x2, x3)` to check if a triangle is valid given edge lengths `x1`, `x2` and `x3`. You can use it without knowing the implementation inside. What is this concept called? Define it with your own words and stress how it is useful.


26. Implement the `valid_triangle` function that is described in the previous question. Provide appropriate docstring so that everyone can use your implementation :)


27. Suppose you are asked to print a line, say  `x = 34`. If you type `print("x" + 34)`, you will receive an error. If you type `print(34)`, you will not receive any errors. Why? Can you suggest two different solutions for this?


28. Write a function that takes a tuple as an input and returns a tuple such that each element is incremented by 1.
First do it by converting it to a list and back, then do it without converting to a list and back. 
`increment_tuple((10,20,30))`
> (11,21,31)

29. Write a function that takes a list of tuples as input and replaces the last element of each tuple with the first element of that tuple. ** (You should not convert tuples to list). **
`replace_last([(1, 2, 3), (10, 20), (40, 50, 200, 300)])`
> [(1, 2, 1), (10, 10), (40, 50, 200, 40)]

30. Write a function that takes a nested list and reverses every other list in the main list. (Do not return a new list. Only modify the original list)
```
nested_list = [[1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15], [16, 17]]
reverse_every_other(nested_list)
print(nested_list)
```
> [[2, 1], [3, 4, 5], [9, 8, 7, 6], [10, 11, 12, 13], [15, 14], [16, 17]]

31. Write a function that takes a tuple as an input and **without converting it to a list and back** returns a tuple with the maximum element removed. (you can assume that the tuple has only 1 maximum element)
`remove_max_from_tuple((100, 20, 300, 15, 48))`
> (100, 20, 15, 48)

32. Flatten a list. write a function that takes a list of lists as an input and returns a simple flat list. (Do not modify the original list. return a new list)
`flatten_list([[10, 20, 30], [40, 50], [60, 70], [80, 90], [100, 110], [120, 130, 140]])`
> [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140] 

33. Given a list of integers, remove all the elements if the sum of that element and the index of that element is divisibly by 3.
```
l = [15,12,18,21,23,36,39]
# TODO: Your Code Here
print(l)
```
> [12, 18, 36]

34. Assume that `num_list` is a list of numbers. after performing which of the following operations, will `num_list` be different than the others?

A: 
```
for index, item in enumerate(num_list):
   num_list[index] = num_list[index] + 1
```
B:
```
for index, item in enumerate(num_list):
   num_list[index] = item + 1
```
C:
```
for index in range(len(num_list)):
   num_list[index] = num_list[index] + 1
```
D:
```
for item in num_list:
   item += 1
```

35. What will `a`, `b`, `c` be after the following operations?
```
a = [1,2,3]
b = [4,5,6]
c = a
a = b
a.append(20)
```

36. Consider the following functions:
```
def double_first1(a):
    a[0] *= 2
    return a

def double_first2(a):
    a[0] *= 2

def change_list1(a):
    a = [100, 200, 300]
    return a

def change_list2(a):
    a = [1000, 2000, 3000]
```
what will `l1`, `l2`, and `l3` be after the following operations?
```
l1 = [10,20,30]
l2 = double_first1(l1)
double_first2(l2)
l3 = change_list1(l1)
change_list2(l2)
```