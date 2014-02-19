# Eden Ghirmai, 2/18/14, www.codeeval.com
# prints out the the pattern generated by such a scenario given the values of
# 'A'/'B' and 'N' which are read from an input text file.

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
    	split = test.split(" ")
    	first = int(split[0])
    	second = int(split[1])
    	third = int(split[2])
    	result = ""
    	for x in range (1, third + 1): 
    		if x % first == 0 and x % second == 0:
    			result += "FB "
    		elif x % first == 0:
    			result += "F "
    		elif x % second == 0: 
    			result += "B "
    		else:
    			result += str(x) + " "

    	print result.strip()

test_cases.close()