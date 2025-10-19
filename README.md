# Отчёт по выполнению заданий по Python

## Студент: Покрывалов Юрий
## Группа: 606-32
## Дисциплина: ИВТ

Шпаргалка по Git

# Клонирование репозитория
git clone https://github.com/exwalue/pythonfirst.git

# Проверка статуса
git status

# Добавление файлов
git add .
git add README.md

# Создание коммита
git commit -m "Описание изменений"

# Отправка на GitHub
git push origin main

# Просмотр истории
git log

00

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря
for city1, coord1 in sites.items():
    distances[city1] = {}
    for city2, coord2 in sites.items():
        if city1 != city2:  # Не считаем расстояние до самого себя
            x1, y1 = coord1
            x2, y2 = coord2
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[city1][city2] = round(distance, 2)  # Округляем до 2 знаков

print(distances)

01

radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
pi = 3.1415926
area = pi * (radius ** 2)
print(round(area, 4))


# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
print(distance_1 <= radius)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
print(distance_2 <= radius)

02


