try:
    age = int(input("Enter age: "))

# except ValueError as err:
#     print(f"Age entered is not a valid integer.")
#     print(f"err msg: {err}")

except (ValueError, ZeroDivisionError) as err:
    print(f"Age entered is not a valid integer.")
    print(f"err msg: {err}")
else:
    print("Try block executed completely")

# Raising Exceptions


def calc_age(age):
    if age <= 0:
        raise ValueError("Age cannot be less or equal to 0.")
    return 10 / age


try:
    calc_age(-1)
except ValueError as ex:
    print(ex)
