#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут

# Находим время для каждой песни
halo_time = 0
enjoy_silence_time = 0
clean_time = 0

for song in violator_songs_list:
    if song[0] == 'Halo':
        halo_time = song[1]
    elif song[0] == 'Enjoy the Silence':
        enjoy_silence_time = song[1]
    elif song[0] == 'Clean':
        clean_time = song[1]

total_time_1 = halo_time + enjoy_silence_time + clean_time
print(f'Три песни звучат {round(total_time_1, 2)} минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# Получаем время из словаря по ключам
total_time_2 = (violator_songs_dict['Sweetest Perfection'] + 
                violator_songs_dict['Policy of Truth'] + 
                violator_songs_dict['Blue Dress'])

print(f'А другие три песни звучат {round(total_time_2, 2)} минут')
