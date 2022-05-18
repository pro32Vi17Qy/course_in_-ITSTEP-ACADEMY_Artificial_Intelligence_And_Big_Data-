# def division(a,b):
#     try:
#         res = a/b
#     except:
#         try:
#             a = int(a)
#             b= int(b)
#             res = a/b
#         except ZeroDivisionError:
#             res = 0
#         except ValueError:
#             res = 0
#     print(res)
#
# division(input(),input())
#
# x = 15
# try:
#     print(x)
# except:
#     print("Something went wrong")
# else:
#     print("Something else do")
# finally:
#     print("The program has complated it\'s work")
#
# def checker(var1):
#     if(typ(var1)) != str:
#         raise TypeError(f"Sorry we can\'t work with {type(var1)}, we need class str!")
#     else:
#         return var1
# fir(10)
# checker(fir)

class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house can not be build"
    def check_material(amount_of_material, limit_value):
        if amount_of_material > limit_value:
            return "enough material"
        else:
            raise BuildingError(amount_of_material)

materials = 123
check_materials(materials, 300)