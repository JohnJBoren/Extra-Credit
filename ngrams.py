import random
from random import choice
import os
#This is used to build a list of all of the words in a book
mainwordlist = []
#This is used to store unique words and the words associated with them up to the next n - grams
beginnings = {}
n = 5
counter = 0
#Read all of the words of the selected text
def readWords():
    global mainwordlist
    book = None
    while book is None:
        os.system("cls")
        book = input("\nChoose the book you wish to use\n1) Alice in Wonderland\n2) Romeo and Juliet\n3) Siddartha:\n")
        try:
            #If the entry is not between the two values, Prompt again
            book = int(book)
            if not (0 <= book < 4):
                print("{input} is not > 0, please re-enter.".format(input=book))
                book = None
                os.system("PAUSE")
            elif ( book == 1):
                with open('alice.txt','r') as f:
                    for line in f:
                        for word in line.split():
                           mainwordlist.append(word.lower())
            elif ( book == 2):
                with open('romeoandjuliet.txt','r') as f:
                    for line in f:
                        for word in line.split():
                           mainwordlist.append(word.lower())
            elif ( book == 3):
                with open('Siddhartha.txt','r') as f:
                    for line in f:
                        for word in line.split():
                            mainwordlist.append(word.lower())
        except:
            print("{input} is not a positive integer, please re-enter your selection.".format(input=book))
            os.system("PAUSE")

#Find bigrams
def find_bigrams(s):
    global mainwordlist
    return zip(mainwordlist, mainwordlist[1:])
#Find n-grams
def find_ngrams(s):
    global n
    global mainwordlist
    return zip(*[mainwordlist[i:] for i in range(n)])

#Print out 100 random words
def nextWords(list1):
    global counter
    while(counter < 100):
        nextword = random.choice(list1)
        print(nextword, end = " ")
        counter += 1
        list1 = beginnings[nextword]
        nextWords(list1)

#Prompt for the integer of n in n-grams
def getGrams():
    global n
    ngrams = None
    while ngrams is None:
        os.system("cls")
        n = input("\nPlease enter the n in n-grams: ")
        try:
            ngrams = int(n)
            n = ngrams
            if (n <= 0):
                print("{input} is not > 0, please re-enter.".format(input=n))
                ngrams = None
                os.system("PAUSE")
        except:
            print("{input} is not a positive integer, please re-enter your selection.".format(input=n))
            os.system("PAUSE")

def buildGrams():
    global n
    t = find_ngrams(mainwordlist)
    for each in t:
        if each[0] not in beginnings:
            beginnings[each[0]] = each[1:]
        else:
            beginnings[each[0]] += each[1:]

    firstWord, list1 = random.choice(list(beginnings.items()))
    nextWords(list1)

def main():
    global counter
    os.system("cls")
    getGrams()
    readWords()
    print("\n")
    buildGrams()
    
#Uncomment this section to see the elements of the beginnings dictionary printed out
    #print("\n\n\t\t- This is an example of the ngrams that were built -\n\n")
    #for lists in beginnings:
        #print( lists, " ", beginnings[lists], "\n")

    # Clear out the lists and dictionary used so that we can build them again if needed
    mainwordlist.clear()
    beginnings.clear()
    repeat = None
    counter = 0
    while repeat is None:
        input_value = input("\n\nEnter 1 to repeat the calculation or 2 to exit: ")
        try:
            repeat = int(input_value) # try and convert the string input to a number
            if (repeat == 1):
                main()
            elif (repeat == 2):
                quit()
            else:
                repeat = None
        except ValueError:
            print("{input} is not a number, please enter a number only".format(input=input_value)) # Prompt to renter

main()
