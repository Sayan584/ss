num1 = int(input("Биринчи санды жазыныз: "))
num2 = int(input("Экинчи санды жазыныз: "))
op = input(" Операцияны танданыз (+, -, *, / :")


if op == "+":
    ans = num1 + num2
    print("Жооп: " + str(ans))



elif op == "-":
    ans = num1 - num2
    print("Жооп: " + str(ans))

elif op == "*":
    ans = num1 * num2
    print("Жооп: " + str(ans))

elif op == "/":
    if num2 == 0:
        print("Нолго болунбойт!")
    else:
        ans = num1/num2
        print("Жооп: " + str(ans))
else:
    print("Андай операция жок")