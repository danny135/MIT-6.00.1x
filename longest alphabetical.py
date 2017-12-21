s = "fartmuffinsabcdefg"
######################################################################
current = ""
longest = ""
for i in range(len(s)):
    if current == "" or ord(s[i]) >= ord(current[-1]):
        current += s[i]
        if len(current) > len(longest):
            longest = current
    else:
        current = s[i]
print "Longest substring in alphabetical order is:", longest
######################################################################
raw_input()
