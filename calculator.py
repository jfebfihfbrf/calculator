first = input("Write your number : ")
second =input("write your number :")
operators =input("write operators")

first =int(first)
second =int(second)
if operators =="+":
    print(first + second )


elif operators =="-":
    print(first - second )

elif operators =="*":
    print(first * second )

elif operators =="/":
    print(first / second )

elif operators =="%":
    print(first % second )
else:
    print("Invalid operation ")
