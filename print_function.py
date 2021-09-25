print(1,2,3,sep=',')
# sep используется для указания способа разделения между выводимыми значениями,
# по умолчанию это пробелы, но можно указать любые символы, пример ниже
print(1,2,3,sep='$$$')
print(1,2,3,sep='@@@')

# параметр end указывает на разделение после каждой строки
print(1,2,3,sep=',',end=' than goes ')
print(5,3,6,end=' $$$ ')
print(2,3,5)

# выводим данные различными способами
dollar = 1500
cents = 55
print("I have", dollar, "dollars", cents, "cents" )

print("I have %s dollars %s cents" %(dollar, cents))