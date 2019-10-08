import sys

##def printData():
##    print(sys.argv)
##
##printData()


##def printSum():
##    print(int(sys.argv[1])+int(sys.argv[2]))
##
##printSum()

##print(sys.version)
### Interpreter will search for packages in these paths
##print(sys.path) 


##print(sys.maxint)
##The sys.maxint constant was removed, since there is no longer a limit to the value of integers.
##However, sys.maxsize can be used as an integer larger than any practical list or string index.
##It conforms to the implementation’s “natural” integer size
##and is typically the same as sys.maxint in previous releases on the same platform (assuming the same build options).
print(sys.maxsize)
print(type(sys.stdin))
print(type(sys.stdout))
print(type(sys.stderr))
print(sys.stdin)
print(sys.stdout)
print(sys.stderr)


# Output:
##9223372036854775807
##<class 'idlelib.run.PseudoInputFile'>
##<class 'idlelib.run.PseudoOutputFile'>
##<class 'idlelib.run.PseudoOutputFile'>
##<idlelib.run.PseudoInputFile object at 0x7f0eab0226a0>
##<idlelib.run.PseudoOutputFile object at 0x7f0eab0226d8>
##<idlelib.run.PseudoOutputFile object at 0x7f0eab022710>
