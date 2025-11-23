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

#hash the hash function

#quadratic probing: for j in range(1, tableSize + 1) 
#t = (hv + j * j) % tableSize

class node:
    def __init__(self, key, value, nextNode = None):
        self.key = key
        self.value = value
        self.next = nextNode

    def nextNode(self, next):
        self.next = next

# class linkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def insert(self, key, value):
#         #check to see if there is key & value
#         if not key  and value:
#             print("Key or Value was none")
#             return
#         newNode = node(key, value)
#         if self.size == 0:
#             self.head = newNode
#             self.tail = newNode
#             self.size = 1
#             return
#         self.head.next = newNode
#         self.head = newNode
#         #increase the ammount of links in the list
#         self.size += 1
#         return
        


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
        self.prime = HashTables.randPrime(1000, 15000)
        self.collisions = 0
        self.valueTable = [None] * size
        self.keyTable = [None] * size

    #inserts into the hash function
    def insert(self, key, value):
        hashedKeys = self.hashKey(key)
        index = hashedKeys % self.size

        if (self.keyTable[index] is None):
            self.keyTable[index] = key
            self.valueTable[index] = value
        elif (self.keyTable[index] != key):
            self.collisions += 1
            hasPlacedValue = False
            while(not hasPlacedValue):
                index += 1
                if (index >= self.size):
                    index = 0

                if (self.keyTable[index] is None):
                    self.keyTable[index] = key
                    self.valueTable[index] = value
                    hasPlacedValue = True
                elif (self.keyTable[index] == key):
                    hasPlacedValue = True

    #Hashes using the title of the movie
    def hashKey(self, Key):
        #do things to stringData, turn it into an int
        numbered = HashTables.toASCII(Key)
        added = sum(numbered)

        #simplest hash
        key = (added % self.prime)

        return key

    def toASCII(stringData):
            firstFive = stringData[:5]
            toNumber = [ord (char) for char in firstFive]
            print (toNumber)
            return toNumber

    #take a random number and check if it is prime using the 
    #sympy library check, if it is prime, return it
    def randPrime(min, max):
        while True:
            prime = random.randint(min, max)
            if isprime(prime):
                return prime


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
                #hash the dataitems as they come in

    hashTable = HashTables(len(dataItems))

    start = time.time()
    for items in dataItems:
        movieName = items.movieName if items.movieName is not None else ""
        quote = items.quote if items.quote is not None else ""
        key = movieName + quote
        hashTable.insert(key, items)

    end = time.time()
    print(f"Loaded {counter} items.")
    print(f"{end-start:0.2f} seconds")
    print(f'there were {hashTable.collisions} collisions')

if __name__=="__main__":
    main()

