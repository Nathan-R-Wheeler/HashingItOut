# HashingItOut
<H2>Nathan Wheeler <br>
Professor Schotter <br>
COS-226 <br>
11/18/25<br>
<h3>The repository for the 5th homework of my Data Structures and Algorithms (cos-226) class.


<br>Attempt 1: <H3>
This attempt implements a very basic hash function, it addes all of the ASCII values of the first 5 letters in the string and applies a random prime number modulo. I chose it because it seemed the most straight forward and easiest hash to achieve, and so it is the first one I attempted to make. My friend looked at it and completely insulted it, so I reformed it to be in order and in doing so I hope I made it easier to modify. It sure does hash, but... not too well. Averaging in the 14500s in collisions, and taking about 15 seconds to run. The only thing this function does "well" is run.

<br>Attempt 2. <H3>
This attempt uses the same basic hash from the last function but uses a linked list to store values instead. While it doesn't handle the collisions that well, it it much faster, only taking 0.03 seconds to run through both tables, but still averaging 14500 collisions.

<br>Attempt 3. <H3>
This attempt uses the same linked list function with the first 5 characters hashed, however this one has a few changes to the linked list, however instead of there only being 5 values in the list, this implementation makes a table size by multiplying the item counter by 2 and checking it for prime. If it is not prime, it increases 1 until it is.  This takes 0.03 seconds to run and makes 0 collisions.

<br>Attempt 4. <H3>
Attempt 4 implements Linear probing to find the nexrt availible empty slot in the table to park more values into. I removed the character limit on the first 5 and the methods involved. I also set a prime instead of it being random each time. the speed is 0.05 seconds and 3319 collisions for the Titles, and 0.64 seconds with 7487 collisions for the Quotes.

<br>Attempt 5. <H3>
