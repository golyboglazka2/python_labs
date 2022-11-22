#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код

months = 10
infl = 1.03
total_educational_grant = educational_grant * months
total_expenses = 0

while months > 0:
    expenses *= (1 if months == 10 else infl)
    total_expenses += expenses

    months -= 1
    #print(months, total_expenses)

print('Студенту надо поросить', (int(total_expenses - total_educational_grant)),'рублей')