s = "dasdlwlgolwladlsdoglwleodle"
######################################################################
vowel_count = 0
for i in range(len(s)):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        vowel_count += 1
print "Number of vowels:", vowel_count
######################################################################
print s
raw_input()