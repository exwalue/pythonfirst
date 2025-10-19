#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:
my_family = ['Папа', 'Мама', 'Брат', 'Дедушка', 'Бабушка']

my_family_height = [
    ['Папа', 180],
    ['Мама', 165], 
    ['Брат', 175],
    ['Дедушка', 170],
    ['Бабушка', 160]
]

# Рост отца
print(f'Рост отца - {my_family_height[0][1]} см')

# Общий рост семьи
total_height = sum(member[1] for member in my_family_height)
print(f'Общий рост моей семьи - {total_height} см')