# Write a function that, given a 4-digit number, returns the largest digit in that number. Numbers between 0 and 999 are counted as 4-digit numbers with leading 0's.
# largest_digit(1234) -> 4
# largest_digit(3253) -> 5
# largest_digit(9800) -> 9
# largest_digit(3333) -> 3
# largest_digit(120) -> 2
# In the last example, given an input of 120, we treat it as the 4-digit number 0120.

def largest_digit(n):
    biggest = 0
    for c in str(n):
        if int(c) > biggest:
            biggest = int(c)
    return biggest

