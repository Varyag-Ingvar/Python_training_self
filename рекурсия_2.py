def recur(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + recur(s[1:-1]) + ')' + s[-1]

s = input("Enter a word: ")
print(recur(s))

def power(x,n):
    if n==0:
        return 1
    if n%2==0:
        return power(x,n//2)*power(x,n//2)
    else:
        return power(x,n-1)*x

x=int(input("Введите число: "))
n=int(input("Введите степень: "))
print(power(x,n))


a = [1,2,[2,3,4,[3,4,[2,3],5]]]

def rec(spisok,level=1):
    print(*spisok,"level=",level)
    for i in spisok:
        if type(i)==list:
            rec(i,level+1)

rec(a)