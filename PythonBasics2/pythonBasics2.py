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
  x = n/3

  return int(x)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  count = 0
  max = 0
  c = s[0]
  for i in range(0, len(s) - 1):
    if s[i] == s[i+1]:
      count += 1
    else:
      if count > max:
        max = count
        c = s[i]
      count = 1
  if count > max:
    max = count
    c = s[i]
  return c

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
