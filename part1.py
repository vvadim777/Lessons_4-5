from math import hypot

class NonNumericError(ValueError):
    pass
class IconsistentDataError(ValueError):
    pass
class BigList(ValueError):
    pass

try:
    entered_list = input("Введите первые катеты: ").split()
    entered_list1 = input("Введите вторые катеты: ").split()
    if len(entered_list)!=len(entered_list1):
        raise IconsistentDataError('Массивы не равны')
    num_list = [int(i) for i in entered_list + entered_list1]
    a = hypot(num_list[0], num_list[2])
    b = hypot(num_list[1], num_list[3])
    s = (num_list[0] * num_list[2]) / 2
    s1 = (num_list[1] * num_list[3]) / 2
    print(f'Треугольник 1 с катетами {num_list[0]} и {num_list[2]} имеет площадь {s} и гипотенузу {a}')
    print(f'Треугольник 2 с катетами {num_list[1]} и {num_list[3]} имеет площадь {s1} и гипотенузу {b}')
except:
    raise NonNumericError("Введены не числа")

try:
    entered_list = input("Введите катеты: ").split()
    if len(entered_list) > 4:
        raise BigList('Слишком много чисел')
    num_list = [int(i) for i in entered_list]
    x = hypot(num_list[0], num_list[1])
    y = hypot(num_list[2], num_list[3])
    s2 = (num_list[0] * num_list[1]) / 2
    s3 = (num_list[2] * num_list[3]) / 2
    print(f'Треугольник 1 с катетами {num_list[0]} и {num_list[1]} имеет площадь {s2} и гипотенузу {x}')
    print(f'Треугольник 2 с катетами {num_list[2]} и {num_list[3]} имеет площадь {s3} и гипотенузу {y}')
except:
    raise NonNumericError("Введены не числа")