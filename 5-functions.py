def sum_of_list(*numbers):
    """
    Takes in *args  and return sum of arguments
    """
    result = 0
    for num in numbers:
        result += num

    return result


x = sum_of_list(1, 2, 3, 4, 5)
print(x)


def user_information(**info):
    print(info)
    return None


x = user_information(name="Aadi", age="24", gender="M")
print(x)


def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num

    return total


print("Start")
print(multiply(1, 2, 3))


def fizz_buzz(num):

    remainder_with_3 = num % 3
    remainder_with_5 = num % 5

    if remainder_with_3 == 0 and remainder_with_5 == 0:
        print("FizzBuzz")
    elif remainder_with_3 == 0:
        print("Fizz")
    elif remainder_with_5 == 0:
        print("Buzz")
    else:
        print(num)
