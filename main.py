###
# 1. Користувач вводить три цифри з клавіатури.
# Залежно від вибору користувача програма виводить на екран максимум із трьох,
# мінімум із трьох або середньоарифметичне трьох чисел.
# ###
try:
    user_number1 = int(input("Enter 1st number: "))
    user_number2 = int(input("Enter 2nd number: "))
    user_number3 = int(input("Enter 3rd number: "))
    
    user_select = int(input("1.The biggest number\n2.Average\nSelect the operation:"))
    match user_select:
            case 1:
                if user_number1 > user_number2 and user_number1 > user_number3:
                    print(f"The biggest number is {user_number1}")
                elif user_number2 > user_number1 and user_number2 > user_number3:
                     print(f"The biggest number is {user_number2}")
                elif user_number3 > user_number1 and user_number3 > user_number2:
                    print(f"The biggest number is {user_number3}")
            case 2:
                n4 = (user_number1 + user_number2 + user_number3) / 3
                 print(f"Average = {n4}")

            case _:
                 print("Incorrect operation number!")
except ValueError as error:
    print("Enter only integer numbers please!")
except Exception as error:
    print(f"Exception occurred: {error}")
