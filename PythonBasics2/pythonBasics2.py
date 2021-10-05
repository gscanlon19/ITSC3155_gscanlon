# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  #creating list
  n = list(str(n))
  #declaring variables
  max = 0
  ind = 0
  #dictionary
  dict = {}
  dict[3] = 0
  dict[6] = 0
  dict[9] = 0
  #loop through
  for i in n:
    x = int(i)
    #if divisible by 3
    if x % 3 == 0 and x != 0:
      dict[x] += 1
  #iterate through and find max
  for i,j in dict.items():
    if j > max:
      max = j
      ind = i
  return ind




# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  #converting to list
  s = list(s)
  count = 1
  max = 1
  l = []
  #dictionary
  dict = {}
  #loop through string to find repeats
  for i in range(0, len(s) - 1):
    #if consecutive
    if s[i] == s[i+1]:
      count += 1
    else:
      if((s[i] in dict) and dict[s[i]] > count):
        continue
      else:
        dict[s[i]] = count
        count = 1
        c = s[i]
  dict[s[len(s) - 1]] = count
  for i,j in dict.items():
    if j > max:
      max = j
  for i,j in dict.items():
    if j == max:
      l.append(i)
  return l
# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  str = s.lower()
  str = str.replace(" ", "")
  return str == str[::-1]
