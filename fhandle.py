""" This program counts each character in a file.
It counts each character like '\n', ',', etc """


with open("fhandle1.txt", "r") as fi:
    li = fi.read()

count = {}   #making a empty dictionary for storing the counted value
let = []     #this list is used to put each character of the file.


for wo in li:
    let.append(wo)   #appending each character of file to the list let.

for le in let:      
    count[le] = 0
    for anle in let:
        if anle == le:
            count[le] += 1


print(count)    #diplaying the no of characters in the dictionary form



