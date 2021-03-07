#Калькулятор v1
question = input("+,-,/,* ? : ")
a = float (input("Введите число: "))
b = float (input("Введите число:  "))

if question == "+":
    c = a + b
    print ("Результат: " + str( c ))
elif question == "-":
    c = a - b
    print ("Результат:" + str(c))
if question == "*":
    c = a * b
    print ("Результат:" + str(c))
elif question == "/":
    c = a / b
    print ("Результат:" + str(c))
else:
    Print ("ДАННАЯ ОПЕРАЦИЯ НЕ ВОЗМОЖНА")
