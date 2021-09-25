# a = int(input())
# b = int(input())
# while a!=b:
#     if a>b:
#         a=a-b
#     else:
#         b=b-a
# print(a)

a = int(input())
b = int(input())
while b>0:
    # c=a%b
    # a=b
    # b=c
    a,b = b,a%b # краткая запись вычислений выше
print(a)
