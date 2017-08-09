
# Find the bigger number
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

# Find the biggest number
def biggest(a,b,c):
    return bigger(a,bigger(b,c))


# find the middlenumber
def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    if big == c:
        return bigger (a,b)

# Print out a random noun
from random import randint

def random_noun():
    # your code here
    number = randint(0,1)
    if number == 0:
        return 'sofa'
    else:
        return 'llama'

print random_noun


# Print out random verb
from random import randint

def random_verb():
    # your code here
    random_num = randint(0,1)
    if random_num == 0:
        return 'run'
    else:
        return 'kayak'

# print out word
def word_transformer(word):
    # your code here
    if word == "NOUN":
        return random_noun()
    if word == "VERB":
        return random_verb()
    else:
        return word[0]

# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

def process_madlib(madlib): #define a function called "process_madlib" which takes in a string "madlib"
    processed = "" # assign variable "processed" to ""
    index = 0 # the idea is to use a "frame box" to move 1 step each to check if there is "NOUN" OR "VERB" in the sentence, now we set the index to 0 which is the place it will start
    box_length = 4 #set up the box length frame to 4 characters
    while index < len(madlib):# the length of steps can vary and we want to repeat the same steps so we use while loops, and our conditional is the index will be less than the length of madlibs
        frame = madlib[index: index + box_length]#set up the frame of 4 characters to check if the word is "NOUN" OR "VERB"
        to_add = word_transformer(frame) #set up the variable "to_add" to use the function "word_transformer" to select the random noun or verb
        processed += to_add #set the "processed" string to the right random noun or verb
        if len(to_add) == 1: # check if the length of "to_add" is 1 character or 4 characters
            index +=1
        else:
            index +=4
    return processed

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p,t):
    i = 0
    while i < len(p):
        if p[i] == t:
            return i
        i += 1
    return -1


def find_element(p,t):
    i = 0
    for e in p:
        if e == t:
            return i
        i += 1
    return -1

print find_element([1,2,3],3)


# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
