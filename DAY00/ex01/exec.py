import sys
str = ' '.join(sys.argv[1:])
stringlength = len(str)
slicedString = str[stringlength::-1]
slicedString = slicedString.swapcase()
print(slicedString)
