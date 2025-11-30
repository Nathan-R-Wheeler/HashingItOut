#Nathan Wheeler
#Professor Troy
#Cos-226
#11/13/25

import csv
import time
import random
from sympy import isprime

#how hashing works


#Play mix and match with my stuff
#linear probing method, at minimum we need a table the size of the data
#linked list method, when collide, add to end of linked list at index

#calculate size of table itself not knowing input size

#FOR LINEAR PROBING THE TABLE HAS TO BE BIGGER THAN THE INPUT

#hash the hash function

#quadratic probing: for j in range(1, tableSize + 1) 
#t = (hv + j * j) % tableSize

class node:
    def __init__(self, key, value, nextNode = None):
        self.key = key
        self.value = value
        self.next = nextNode

class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        #watch for collisions, initiate a counter
        collisions = 0
        #check to see if there is key & value
        if not key  or not value:
            print("Key or Value was none")
            return collisions
        
        newNode = node(key, value)

        if self.head is None:
            self.head = newNode
        
            return collisions
        
        currentNode = self.head
        parentNode = None

        while (currentNode is not None):
            if currentNode.key == key:
                #then the key exists
                return collisions
            else:
                parentNode = currentNode
                currentNode = currentNode.next
            collisions += 1
        parentNode.next = newNode
        return collisions
        


class DataItem:

    def __init__(self, movieName, genre, releaseDate, director, revenue, rating, minDuration, productionCompany, quote):
        self.movieName = movieName
        self.genre = genre
        self.releaseDate = releaseDate 
        self.director = director
        self.revenue = revenue
        self.rating = rating
        self.minDuration = minDuration
        self.productionCompany = productionCompany
        self.quote = quote

#Uses movie as key
class HashTables():
    #make the empty hash table
    def __init__(self, size):
        self.size = size
        self.collisions = 0

        #for linked list
        self.linkedList = [linkedList() for i in range(size)]


        #for linear probing
        self.linearTable = [None] * size

        #for quadratic probing
        self.quadraticTable = [None] * size

        #to fix collisions and time for implementation #4
        self.prime = self.nextPrime(129)

    def nextPrime(self, num):
        while True:
            if isprime(num):
                return num
            num += 1

    # #inserts into the hash function
    # def insert(self, key, value):
    #     hashedKeys = self.hashKey(key)
    #     index = hashedKeys % self.size
    #     linkedList = self.linkedList[index]
    #     self.collisions += linkedList.insert(hashedKeys, value)

    def linearInsert(self, key, value):
        hashed = self.hashKey(key)
        index = hashed % self.size
        collisions = 0
        while True:
            insertionSlot = self.linearTable[index]

            #check if empty
            if insertionSlot is None:
                self.linearTable[index] = (key, value)
                self.collisions += collisions
                return
            
            #if the key is the same, update it
            if insertionSlot[0] == key:
                return
            
            #if there is a collision, check the next slot
            collisions += 1
            index = (index + 1) % self.size

            #in case the table gets full
            if collisions >= self.size:
                print("The table got full")


    def quadraticInsert(self, key, value):
        hash = self.hashKey(key)
        hashedValue = hash % self.size
        collisions = 0 

        
        for i in range(self.size):
            index = (hashedValue + (i * i)) % self.size
            insertionSlot = self.quadraticTable[index]


            #if there is an empty slot
            if insertionSlot == None:
                self.quadraticTable[index] = (key, value)
                self.collisions += collisions
                return
            #if the key already exists, we update it
            if insertionSlot[0] == key:
                self.quadraticTable[index] = (key, value)
                return
            collisions += 1

        print("The table filled up!")
            
            

      

    #Hashes using the title of the movie


    #take a random number and check if it is prime using the 
    #sympy library check, if it is prime, return it
    def hashKey(self, key):
        #do things to stringData, turn it into an int
        #initialize a hashed number
        hashNum = 0
        for ch in key:
            hashNum = (hashNum * self.prime + ord(ch))
        return hashNum
            


#input spreadsheet data into dataITems through csv 
def main():
    file = "MOCK_DATA.csv"
    counter = 0
    dataItems = []

    with open(file, 'r', newline= '', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if (len(row) >= 9):
                items = DataItem(
                    movieName = row[0],
                    genre = row[1],
                    releaseDate = row[2],
                    director = row[3],
                    revenue = row[4],
                    rating = row[5],
                    minDuration = row[6],
                    productionCompany = row[7],
                    quote = row[8]
                )

                dataItems.append(items)
                counter += 1
    hashTable = HashTables(0)
    tableSize = hashTable.nextPrime(counter * 2)
                #hash the dataitems as they come in
    hashTable = HashTables(tableSize)

    #run for title
    print("Running Title")
    start = time.time()
    for items in dataItems:
        nameKey = items.movieName if items.movieName is not None else ""
        #hashTable.insert(nameKey, items)
        hashTable.quadraticInsert(nameKey, items)
    end = time.time()
    print(f"Loaded {counter} items.")
    print(f"{end-start:0.2f} seconds")
    print(f'there were {hashTable.collisions} collisions')

    hashTable = HashTables(tableSize)
    #run for quote
    print("Running quote")
    start = time.time()
    for items in dataItems:
        quoteKey = items.quote if items.quote is not None else ""
        #hashTable.insert(quoteKey, items)
        hashTable.quadraticInsert(quoteKey, items)

    end = time.time()
    print(f"Loaded {counter} items.")
    print(f"{end-start:0.2f} seconds")
    print(f'there were {hashTable.collisions} collisions')

if __name__=="__main__":
    main()

