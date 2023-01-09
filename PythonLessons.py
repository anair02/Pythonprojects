#references 
#User input using the input function
name = input('Who are you? ')
print('Welcome',name)

#try and except 
#when the first conversion fails instead of giving an error it will try out the except clause
#except code is only triggered when the try code fails 
#don't put blocks of code inside a try because if one line fails then the other lines won't run and it will skip to except
astr = 'Hello Bob'
try: 
    istr = int(astr)
except:
    istr = -1

#loops and the format in python
while n > 0 :
    print("Lather")
    n = n - 1
print("Blast off")

#break statements
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

#Definite loop example 
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')
#The result 
#5 4 3 2 1 Blastoff!

#finding the smallest value using None
# "is" is stronger than =
# "is" implies that 'it is the same as'
# 'is not' is also a logical operator
# use is sparingly 
smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
print('After',smallest)

#input accepts only string type so you have to conver if you want a value of any other type
apple = input('Enter: ')
#Enter: 100
x = int(apple) - 10
print(x)
#90

#Slicing string 
s = 'Monty Python'
print(s[0:4])
#Mont 
print(s[6:7])
#p
print(s[6:20])
#Python
#Even though 20 doesn't exist python ignores that and just prints what is there
print(s[:2])
#Mo
print(s[8:])
#thon
print(s[:])
#Monty Python


#String concatenation
a = 'Hello'
b = a + 'There'
print(b)
#HelloThere
c = a + ' ' + 'There'
print(c)
#Hello There

#using in as a logical operator 
fruit = 'banana'
'n' in fruit 
#True 
'm' in fruit 
#False
'nan' in fruit 
#true
if 'a' in fruit :
    print('found it!')
#Found it!

#String library examples 
#these string library functions do not modify the original string they return a new string 
greet = "Hello There"
zap = greet.lower()
print(zap)
#hello there

#Searching a string
fruit = 'banana'
pos = fruit.find('na')
print(pos)
#2

#Search and replace 
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')

#Opening a file 
handle = open('mbt.txt','r')
#open(filename,mode)
#filename is a string
#mode is optional and should be 'r' if you're reading the file and 'w' if you're going to write to the file
#handle is not the file itself it only allows you to talk to the file 

#File handle as a sequence
xfile = open('mbt.txt')
for cheese in xfile:
    print(cheese)
#in this case cheese represents everyline in the file and each line is printed as such

#Reading the whole file 
fhand = open('mtx.txt')
inp = fhand.read()
print(len(inp))
#9867
print(inp[:20])
#From stephen mehers 

#Searching through a file 
fhand = open('mtx.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
#use the strip function to get rid of the spaces that will appear from the right end 


#Looking inside lists
friends = ['Joseph','Glenn','Mary']
print(friends[1])
#Glenn
#you can make changes in lists but you can not change strings (except for upper case and lower case)

#range functions 
print(range(4))
#[0,1,2,3]
#range function returns a list of numbers that range from 0 to one less than the parameter

#Example 
friends = ['Jerry','Emma','Sally']
print(len(friends))
#3
print(range(len(friends)))
#[0,1,2,3]

#Building a list from scratch 
stuff = list()
stuff.append('book')
stuff.append(99)           
#list stays in the order that you add

#Putting a list in dscending order using the sorted method
#lst = sorted(lst, reverse = True)

#Is something in the list??
some = [1,9,20,10,16]
9 in some
#True
#Python provides operators that lets you check if an item is in the list or not

#Lists can be sorted
friends = ["Joseph",'Glen','Sally']
friends.sort()
print(friends)
#[Glen,Joseph,Sally]
#the sort method means 'sort yourself' in this case it did it in alpahtical order 

#Split breaks a string into parts and produces a list of strings
abc = 'With three words'
stuff = abc.split()
print(stuff)
#['With','three',words]
#you can specify what delimmiter character to use in the splitting 
thing = line.split(';')

#Dictionaries vs. lists
#List is organized and each value is added in order
#dictionary: a bag of values (not organized) but each has it's own label and you can use the label to retrieve them
#Associative arrays(dictionary)
#Example 
purse = dict()
purse['money'] = 12
purse['candy'] = 3
print(purse)
#{'money': 12, 'candy': 3}

#Dictionary literals 
jjj = {'chuck': 1, 'fred': 42}
print(jjj)
#{fred: 42, chuck: 1}
#note that dictionaies don't always print in the order that you put them in because they are not like lists

#We can use an in operator to see if a certain key is in the dictionary
#in avoids getting a traceback 
'csvec' in jjj
#Result: False 

#IMPORTANT FOR DICTIONARIES
#di[w] = di.get(w,0) + 1
#what this says: get the old value from the key (w) or from 0 and add 1 to it 

#Two iteration variables 
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa,bbb in jjj.items():
    print(aaa,bb)
#Result: jan 100 
#        chuck 1
#        fred 42
#How it works
#aaa     bbb
#[jan]   100
#[chuck] 1
#[fred] 42


#Tuples are a lot like lists
#tuples are another kin dof sequence that functions 
#elements starting at 0 
#you can not modify tuples (unlike lists)
#you CAN NOT do with tuples (sort, append, reverse)
x = ('Glenn', 'Sally','Joseph')
print(x[2])
#Joseph

#Why Tuples and not lists?
#Tuples are simpler and more efficient in terms of memeory usage and performance than lists
#When making "temporary variables" we prefer tuples over lists

#Tuples and assignments 
(x,y) = (4, 'fred')

#You can compare tuples 
(0,1,2) < (5,1,2)
#True
('Jones', 'Sally') < ('Jones','Sam')
#True
#in this string l comes before m so the < is true in this case

#Sorting lists of tuples
#We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
#items() method returns a view object that shows the key value pairs of a dictionary, as tuples in a list
d = {'a':10, 'b':1, 'c':22}
d.items()
#dict_items([('a',10), ('c',22), ('b',1)])
sorted(d.items())
#[('a',10), ('c',22), ('b',1)]

#TCP connections/Sockets
#In computer networking, one process is runing on one computer while another process is runing on another computer
#and the internet (in this case but can be any internet protocol based computer network)
# allows for communication between these two 'sockets'

#Sockets in python 
import socket
#calling a socket function in the socket library
#socket.AF_INET means you're creating a socket that goes across the internet 
#stream socket meaning its a series of characters that come one after another 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#makes a connection across the internet (kind of like a phone call)
#mysock.connect('Host',port)
mysock.connect('data.pr4e.org',80)

#What are we going to send and recieve with our socket?
#this is called the application protocol 

#Hypertext transfer protocol (HTTP)
# dominanat application layer protocol on the internet
#invented for the web (to retrieve HTML, images, documents)

#NumPy 
#faster to read because uses less bytes of memory than lists
#no type cheking when iterating through objects (unlike lists that have 
# strings and float, ect.)

#NumPy had continguous memory 
#Lists have their information scattered around the computer's memory
#all the infromation is not   right next to each other 
#so in order to retrieve the information in the lists there's some bouncing around that happens 
#obviously this process is slow 
#NumPy has continguous memory so all the information is stored right next to each other 
#the start of the NumPy memory and the total size and type of memory block is stored 

#NumPy allows you to use SIMD Vector Processing 
#Single Instruction Multiple Data
#SIMD allows you to perform computations on all the data at the same time 


