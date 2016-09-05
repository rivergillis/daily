#generate the nth fibonacci number
def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

fiblist = []
for i,n in enumerate(fib()):
    fiblist.append(n)
    if i == 1000:
        break

def dtofib(n):
    print("dtofib")
def fibtod(n):
    print("fibtod")

inputs = input().split(' ')
if inputs[0] == "10":
    dtofib(int(inputs[1]))
else:
    fibtod(int(inputs[1]))
