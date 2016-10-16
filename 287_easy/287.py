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

# Bonus 1
# Write a function that, given a 4-digit number, performs the "descending digits" operation. This operation returns a number with the same 4 digits sorted in descending order.
# desc_digits(1234) -> 4321
# desc_digits(3253) -> 5332
# desc_digits(9800) -> 9800
# desc_digits(3333) -> 3333
# desc_digits(120) -> 2100

def desc_digits(n):
    l = list(str(n).zfill(4))
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(l)-1):
            if l[i] < l[i+1]:
                is_sorted = False
                l[i], l[i+1] = l[i+1], l[i]
    return int(''.join(l))

def asc_digits(n):
    return int(''.join(sorted(list(str(n).zfill(4)))))

def kaprekar(n):
    s = str(n)
    unique = False
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                unique = True
    if not unique:
        return 0

    kapcount = 0
    while (n != 6174):
        n = desc_digits(n) - asc_digits(n)
        kapcount += 1

    return kapcount

def max_kaprekar():
    biggest = 0
    for i in range(10000):
        kap = kaprekar(i)
        if kap > biggest:
            biggest = kap
        if kap == 7:
            print(i)
    return biggest



print(desc_digits(1234))
print(asc_digits(4321))
print(kaprekar(6589))
max_kaprekar()
