"""
multiplication-table.py
Author: Peter Bynum
Credit: user "Pitarou" from http://stackoverflow.com/questions/20415384/properly-formatted-multiplication-table
Assignment: Multiplication Table

Write and submit a Python program that prints a multiplication table. The user 
must be able to determine the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""



w = int(input("Width of multiplication table: "))
h = int(input("Height of multiplication table: "))
print()
for i in range(1,(h+1)):
    line = ''
    for j in range(1,w+1):
        line = line + "{0:>3} ".format(i*j) #http://stackoverflow.com/questions/20415384/properly-formatted-multiplication-table
    print(line)

#The line that I found online is cleverly simple. It sets a strand ("line") equal to nothing, and then it builds it up using the function in line 33.
