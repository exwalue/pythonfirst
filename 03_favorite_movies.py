#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

first_comma = my_favorite_movies.index(',')
second_comma = my_favorite_movies.index(',', first_comma + 1)
third_comma = my_favorite_movies.index(',', second_comma + 1)
fourth_comma = my_favorite_movies.index(',', third_comma + 1)

# Извлекаем фильмы с помощью срезов
first_movie = my_favorite_movies[:first_comma]
last_movie = my_favorite_movies[fourth_comma + 2:]
second_movie = my_favorite_movies[first_comma + 2:second_comma]
second_from_end = my_favorite_movies[third_comma + 2:fourth_comma]

print(first_movie)
print(last_movie)
print(second_movie)
print(second_from_end)