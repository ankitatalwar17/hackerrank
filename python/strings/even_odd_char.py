#Objective 
#Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

#Task 
#Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as 
#space-separated strings on a single line (see the Sample below for more detail).

#Note:()  is considered to be an even index.

#Input Format

#The first line contains an integer,  (the number of test cases). 
#Each line  of the  subsequent lines contain a String, .

#Constraints
#1<=T<=10
#2<=length of S<=10000

#Output Format

#For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# number of strings
n =int(input())
# loop for each strin . Using String Slicing and format function
for i in range (1,n+1):
    my_str = str(input())
    print ('{} {}'.format(my_str[::2], my_str[1::2]))
