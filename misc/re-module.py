import re
txt = "The rain in Spain"

x = re.search("^The", txt)
x = re.search("^The.*Spain$", txt) #Search the string to see if it starts with "The" and ends with "Spain":
print (x)

#findall - Returns a list of containing all matches
#search - Returns a Match Object if there is a match anywhee in the string
# sub	Replaces one or many matches with a string

# [a-z] - denotes a set of character
# [0-9] - denotes a set of character/digits
# he..o - any character
# ^Hello - starts with 
# world$ - ends with 
# aix* - zero or more occurance
# aix+ - one or more occurance
# al{2} - exactly the specified number of occurancees
# falls|stays - either or 
# [arn] - a, r, n match
# [a-n] - range
# [^arn] - not match (no a, r, n)
# [0-9]- match for any digits
# [a-zA-Z] - any letter
# [+] - return a match for any + character

# \A - match a beginning ex- x = re.findall("\AThe", txt)
# \b - at the begining or end () ex- x = re.findall(r"\bain", txt)
# \d - retuns match if matches digits  x = re.findall("\d", txt)
# \D - no digits x = re.findall("\D", txt)
# \s -white space match
# \S - no whitespace
