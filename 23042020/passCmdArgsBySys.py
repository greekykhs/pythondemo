# -----------------------------------------------------------
#  How to pass command line arguments in Python?
#
# (C) 2020, Himanshu Shukla
# email acmehimanshu@gmail.com
# -----------------------------------------------------------
import sys

program_name = sys.argv[0]
arguments = sys.argv[1:]
argument_count = len(sys.argv) - 1
first_parameter=sys.argv[1]
second_parameter=sys.argv[2]

print("Program Name:"+program_name)
print("Length of arguments:"+str(count))
print("first_parameter:"+first_parameter)
print("second_parameter:"+second_parameter)

print("Printing the Arguments...")
for x in arguments:
     print(x)

position = 1
while (argument_count >= position):
    print ("Parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1

