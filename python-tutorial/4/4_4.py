#break文とccontinue文とループのelse節
from re import I


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, n//x)
            break
    else:
        print (n, 'is a prime number')

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("found an odd number", num)