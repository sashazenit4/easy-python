# year_of_birth = int(input("Введите ваш год рождения: "))
# sex = input("Укажите пол M или F: ")
# >
# <
# >=
# <=
# not
# ==
# !=
# and
# or
# xor - исключающее или
#
# if year_of_birth >= 2009 and sex == 'M':
#     print("You are alpha boy")
# elif year_of_birth >= 2009 and sex == 'F':
#     print("You are a alpha girl")
# elif year_of_birth >= 1997:
#     print("You are a zoomer")
# elif year_of_birth >= 1990:
#     print("You are a millennial")
# else:
#     print("You are not a zoomer and you are not millennial")

a = False
b = True

if (a or b) and not (a and b):
    print("A xor B is true")
else:
    print("A xor B is False")