a = input("Введите строку: ")  
b = a.split(';')   
c = b[0]   
for i in b: 
    if len(i) > len(c):  
        c = i   
 
print("Самое длинное слово:", c)