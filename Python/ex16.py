#Reading and Writing Files - Exercise 16, Learn Python the Hard Way
from sys import argv

script, filename = argv

print "We're goig to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncanting the file. Goobye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close

