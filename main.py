###
# 2. Користувач вводить з клавіатури кількість метрів.
# Залежно від вибору користувача програма переводить метри милі, дюйми або ярди.
###

try:
    user_number = float(input("Enter the value in meters:"))

    user_select = input("Choose the measurement unit:\nm-miles, i - inches, y - yards:")

    match user_select:
        case 'm':
                n1 = user_number * 0.000621
                print(f"{user_number} meters = {n1} miles")
        case 'i':
                n2 = user_number * 39.37
                print(f"{user_number} meters = {n2} inches")
        case 'y':
                n3 = user_number * 0.914
                print(f"{user_number} meters = {n3} yards")
        case _:
                print("Incorrect measurement unit")

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

except ValueError as error:
    print("Enter only numbers please!")
