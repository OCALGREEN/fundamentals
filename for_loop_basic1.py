print("Basics")
for x in range(151):
    print(x)

print("Multiples of 5")
for x in range(5, 1001):
    if x%5 == 0:
        print(x)

print("Counting, the Dojo Way")
for x in range(1, 101):
    if x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    else:
        print(x)

print("Woha! That Sucker is Huge")
sum = 0
for x in range(500001):
    if x%2 != 0:
        sum += x
print(sum)

print("Countdown by Fours")
for x in range(2018, 0, -4):
    print(x)

print("Fexible Counter")
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if x%mult == 0:
        print(x)