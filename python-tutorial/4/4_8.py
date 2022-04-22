from re import I, L


def adk_ok(prompt, retries=4, remindedr='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
            print(remindedr)

#とりあえず写してみたがよくわからん。残念




i=5

def f(arg=i):
    print(arg)
#ここまでの範囲(またの名をscope)でデフォルト値が決まるらしい

i=6
#だからこのi=6はargには関係ないらしい
f()
#つまりここでは"5"が出力される


def f(a,L=[]):
    L.append(a)
    #appendは添えるという意味らしい。
    #L=[]にaを加える？てことは[]でlistを定義してるので
    #どんどん値が加えられていってるてことね
    return L
    #値が加えられていった後の結果
    #これがないと、Noneになってしまう

print(f(1))
print(f(2))
print(f(3))
print(f(-1))
print(f(5))
print(f(-1.5))
print(f("こんにちは"))
print(f("complete"))
print(f("nice"))
