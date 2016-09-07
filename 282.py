#https://www.reddit.com/r/dailyprogrammer/comments/5196fi/20160905_challenge_282_easy_unusual_bases/
#generate the nth fibonacci number
def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

#add the first 1000 fibonacci numbers to a list
fiblist = []
for i,n in enumerate(fib()):
    fiblist.append(n)
    if i == 1000:
        break

# convert from decimal base to base fib
def dtofib(n):
    remainders = []
    # find the highest divisible fib
    i = 20
    while i > 0:
        if n >= fiblist[i]:
            remainders.append(1)
            n -= fiblist[i]
        else:
            remainders.append(0)
        i -= 1
    s = ''.join(str(e) for e in remainders)
    return str(int(s))


# convert from base fib to decimal base
def fibtod(s):
    total = 0
    for index, num in enumerate(s):
        total += int(num) * fiblist[len(s) - index]
    return total

# gather input, determine what the base is, send to the function
inputs = input().split(' ')
if inputs[0] == "10":
    print(str(dtofib((int(inputs[1])))))
else:
    print(str(fibtod((inputs[1]))))

