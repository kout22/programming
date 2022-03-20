for i in range(5):
    print(i)
for j in range(5,10):
    print(j)
for k in range(0,10,3):
    #0~10まで3ごとに＝0,3,6,9
    print(k)
for l in range(0,3,10):
    #0~3まで10ごとに=0
    print(l)


a = ['Nice','to','meet','you']
for i in range(len(a)):
    print(i+1, a[i])
    #enumerate関数の方が便利らしい

b = sum(range(4))
#0+1+2+3=6 sum関数ってエクセルとかにもあるよね
print(b)

c = list(range(4))
#0,1,2,3
print(c)

#list使わずに直接printしてみると…
print(range(4))
# range(0,4)だそうです。