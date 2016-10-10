#https://www.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/
#120 -> 120/2 -> 60/3 -> 20/4 -> 5/5 -> 1 => 5!
def load_input():
    input_nums = []
    fh = open("input.txt", 'r')
    for line in fh.readlines():
        input_nums.append(int(line.strip()))
    return input_nums

def reverse_fact(n):
    denom = 2
    while n > 1:
       n /= denom
       denom += 1
    return (n,denom-1)

for num in load_input():
    quotient, denom = reverse_fact(num)
    if quotient == 1:
        print(str(num) + " = " + str(denom) + "!")
    else:
        print(str(num) + "\t" + "NONE")
