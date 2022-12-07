# -*- coding: utf-8 -*-
# import simple_draw as sd
# from random import uniform
# import numpy as np
 
# sd.resolution = (1000, 700)

# # На основе кода из практической части реализовать снегопад:
# # - создать списки данных для отрисовки N снежинок
# # - нарисовать падение этих N снежинок
# # - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# n = 100

# # Пригодятся функции
# # sd.get_point()
# # sd.snowflake()
# # sd.sleep()
# # sd.random_number()
# # sd.user_want_exit()
#  # TODO здесь ваш код

# x_list = []  
# y_list = []  
# a_list = []
# b_list = []
# c_list = []
# l_list = []

# for _ in range(n):
#     y_points = np.random.randint(900, high = 10000, size = 10)[0]  # создаем рандомные координаты х
#     x_points = np.random.randint(50,  high = 1000, size = 10)[0]  
#     x_list.append(x_points)  # запись координат х в список (на последнее место)
#     y_list.append(y_points)  
#     lengths = np.random.randint(10,  high = 40, size = 1)[0]  # рандомный размер снежинки
#     factor_aa = np.round(uniform(0.3, 0.9), 2)  # рандомное место ответвления лучиков
#     factor_bb = np.round(uniform(0.25, 0.45), 2)  # рандомная длина лучиков
#     factor_cc = np.random.randint(10, high = 100, size = 1)[0]  # рандомный угол отклонения лучиков
#     l_list.append(lengths)  # запись координат размера снежинок в список
#     a_list.append(factor_aa)  
#     b_list.append(factor_bb)  
#     c_list.append(factor_cc)  
 
 
# def snowf(center, length, color, factor_a, factor_b, factor_c):  # отрисовка снежинки
#     sd.snowflake(center, length, color, factor_a, factor_b, factor_c)  
#     x_list[i] += np.random.randint(-5, high = 5, size = 1)[0]
 
 
# while True:
#     for i in range(n):
#         point = sd.get_point(x_list[i], y_list[i])  # задаем координаты
#         fac_a = a_list[i]
#         fac_b = b_list[i]
#         fac_c = c_list[i]
#         l_length = l_list[i]
#         # snowf(center=point,length=l_length, color=sd.COLOR_WHITE, factor_a=fac_a, factor_b=fac_b, factor_c=fac_c)  # вызываем ф-цию отрисовки снежинки
#         y_list[i] -= 5  # падаем на 10 пикс.
#         x_list[i] += .5
#         if y_list[i] < 50:  # проверка упала ли снежинка
#             break  
#         point1 = sd.get_point(x_list[i], y_list[i])
#         snowf(center=point1, length=l_length, color=sd.COLOR_WHITE, factor_a=fac_a, factor_b=fac_b,
#               factor_c=fac_c)  # вызываем ф-цию отрисовки снежинки
#         sd.sleep(0.000000001)  # таймаут
#     if sd.user_want_exit():
#         break
#     sd.clear_screen()
# sd.pause()

# snowfleaks((255, 255, 255,), 100, 0.2)


import simple_draw as sd
import random
sd.resolution = 1080, 600
# function return dict wiht ltis
def snowf_value(amount):# функция возвращает список со словарём в котором данные для снежинки
    N = 100      # количество снежинок
    snowf_lists = []
    color_list_tuple = [(255, 255, 255), (0, 0, 0), (255, 0, 0),# список разной цветовой палитры
                        (255, 127, 0), (255, 255, 0), (0, 255, 0),
                        (0, 255, 255), (0, 0, 255), (255, 0, 255),
                        ]
    for i in range(N):# цикл заполняет словарь с данными снежинки
        length_list = [x for x in range(4, 30, random.randint(3, 9))] # генерируем список случайных величин длинны
        f = {'length': length_list,
             'x': random.randint(20, 3000),# координата "х"
             'y': random.randint(500, 1500),# координата "у"
             "color" : random.choice(color_list_tuple)# выбирает случайный цвет снежинки
             }
        snowf_lists.append(f)
    return snowf_lists
 
c = 0
def snowfleaks(color_list, amount, speed, quantity_snowflake=True):# рисуем многослойную снежинку передаём функции цвет, количество снежинок
    x, y = 0, 0                                                 # скорость отрисовки и условие при отсутствии которого получаем снегопад
    snowf_lists = snowf_value(amount=amount)# получаем данные для снежинки
    while True:
        sd.start_drawing()# функция simple-draw начинает рисовать в pygame
        # the loop takes data from the list, draws a white snowflake and a blue circle
        for index, count in enumerate(snowf_lists):# запускаем двумерный цикл первый проходит по словарю списка
            for snowf_list in snowf_lists[index]['length']:# второй проходит по списку длинны "length"
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=color_list)  # рисуем многослойную снежинку
            sd.circle(center_position=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), radius=40,
                      color=sd.background_color, width=0) # рисеум подложку цветом beckground
            snowf_lists[index]['x'] -= sd.random_number(-20, 20)    # меняем координаты
            snowf_lists[index]['y'] -= sd.random_number(10, 20)     # меняем координаты
        for index, count in enumerate(snowf_lists): # повторяем двумерный цикл для и рисуем снежинку со смещением
            for snowf_list in snowf_lists[index]['length']:# добиваемся эффекта красивого снегопада
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=color_list)
            # list deletion condition
            if snowf_lists[index]['y'] < sd.random_number(5, 15): # условие выполнение которого собирает снежинки в сугроб
                snowf_lists.remove(count)
                if quantity_snowflake == True:# если выполняется это условие
                        snowf_lists.clear()# освобождаем список с данными снежинки
                        s = snowf_value(amount=amount)# получаем новые
                        snowf_lists += s  # добавляем в список получаем количество снежинок равное N
        x += 1
        # condition for updating the list with data and continuing the snowfall
        if quantity_snowflake == False: # если выполняется это условие получаем снегопад
            if x % 3 == 0: # каждый третий проход
                for _ in range(4): # добавляем в список количество снежинок (N * 4)
                    s = snowf_value(amount=amount)
                    snowf_lists += s
                for _ in range(len(snowf_lists)): # проходим по длине списка
                    snowf_lists[_]['length'].clear() # удаляем список с длинной "length"
                    for length in range(1, sd.random_number(8, 30), 4):# создаём новый список длины "length"
                        snowf_lists[_]['length'].append(length) # получаем эффект таяния снежинок на лету
 
        sd.finish_drawing()
        sd.sleep(speed)
        if sd.user_want_exit():
            break
 
def snowfleaks_multicolor( amount, speed, quantity_snowflake=True): # фукция рисует разноцветные снежинки
    x, y = 0, 0                                                 # разноцветный снегопад
    snowf_lists = snowf_value(amount=amount)                    # в остальном они одинаковые
    while True:
        sd.start_drawing()
        # sd.clear_screen()
        # the loop takes data from the list, draws a white snowflake and a blue circle
        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=snowf_lists[index]['color']) # получаем разный цвет из словаря данных снежинки
 
            sd.circle(center_position=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), radius=30,
                      color=sd.background_color, width=0)
            snowf_lists[index]['x'] -= sd.random_number(-20, 20)
            snowf_lists[index]['y'] -= sd.random_number(10, 20)
        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=snowf_lists[index]['color'])
            # list deletion condition
            if snowf_lists[index]['y'] < sd.random_number(15, 25):
                snowf_lists.remove(count)
                if quantity_snowflake == True:
                        snowf_lists.clear()
                        s = snowf_value(amount=amount)
                        snowf_lists += s
        x += 1
        #condition for updating the list with data and continuing the snowfall
        if quantity_snowflake == False:
            if x % 3 == 0:
                for _ in range(2):
                    s = snowf_value(amount=amount)
                    snowf_lists += s
 
                for _ in range(len(snowf_lists)):
                    snowf_lists[_]['length'].clear()
                    for length in range(1, sd.random_number(8, 30), 4):
                        for length in range(sd.random_number(0, 600)):
                            snowf_lists[_]['length'].append(length)
 
        sd.finish_drawing()
        sd.sleep(speed)
        if sd.user_want_exit():
            break
snowfleaks((255, 255, 255,), 100, 0.2)
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
