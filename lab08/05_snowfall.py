# -*- coding: utf-8 -*-
import simple_draw as sd
from random import uniform
 
sd.resolution = (1000, 700)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

n = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
 # TODO здесь ваш код

x_list = []  
y_list = []  
a_list = []
b_list = []
c_list = []
l_list = []
 
for _ in range(n):
    y_points = sd.random_number(500, 600)  # создаем рандомные координаты х
    x_points = sd.random_number(100, 1000)  
    x_list.append(x_points)  # запись координат х в список (на последнее место)
    y_list.append(y_points)  
    lengths = sd.random_number(10, 40)  # рандомный размер снежинки
    factor_aa = round(uniform(0.3, 0.7), 2)  # рандомное место ответвления лучиков
    factor_bb = round(uniform(0.25, 0.45), 2)  # рандомная длина лучиков
    factor_cc = sd.random_number(10, 100)  # рандомный угол отклонения лучиков
    l_list.append(lengths)  # запись координат размера снежинок в список
    a_list.append(factor_aa)  
    b_list.append(factor_bb)  
    c_list.append(factor_cc)  
 
 
def snowf(center, length, color, factor_a, factor_b, factor_c):  # отрисовка снежинки
    sd.snowflake(center, length, color, factor_a, factor_b, factor_c)  
    x_list[i] += sd.random_number(-10, 10)
 
 
while True:
    for i in range(n):
        point = sd.get_point(x_list[i], y_list[i])  # задаем координаты
        fac_a = a_list[i]
        fac_b = b_list[i]
        fac_c = c_list[i]
        l_length = l_list[i]
        snowf(center=point,length=l_length, color=sd.COLOR_RED, factor_a=fac_a, factor_b=fac_b, factor_c=fac_c)  # вызываем ф-цию отрисовки снежинки
        y_list[i] -= 44  # падаем на 10 пикс.
        # x_list[i] += .5
        if y_list[i] < 50:  # проверка упала ли снежинка
            break  
        point1 = sd.get_point(x_list[i], y_list[i])
        snowf(center=point1, length=l_length, color=sd.COLOR_WHITE, factor_a=fac_a, factor_b=fac_b,
              factor_c=fac_c)  # вызываем ф-цию отрисовки снежинки
        sd.sleep(0.01)  # таймаут
    if sd.user_want_exit():
        break
    sd.clear_screen()
sd.pause()


# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

