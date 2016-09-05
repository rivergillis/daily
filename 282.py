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

def dtofib(n):
    print("dtofib")
def fibtod(s):
    print("fibtod")
    total = 0
    for index, num in enumerate(s):
        #print(total)
        total += int(num) * fiblist[len(s) - index]
        #print("adding " + num + " * " + str(fiblist[len(s)-index]))
    #print("about to return! " + str(total))
    return total

inputs = input().split(' ')
if inputs[0] == "10":
    print(str(dtofib((inputs[1]))))
else:
    print(str(fibtod((inputs[1]))))

