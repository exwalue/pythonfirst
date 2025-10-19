# Отчёт по выполнению заданий по Python

## Студент: Покрывалов Юрий
## Группа: 606-32
## Дисциплина: ИВТ


Шпаргалка по Git

Клонирование репозитория
git clone https://github.com/exwalue/pythonfirst.git

Проверка статуса
git status

Добавление файлов
git add .
git add README.md

Создание коммита
git commit -m "Описание изменений"

Отправка на GitHub
git push origin main

Просмотр истории
git log

# 00

```python
for city1, coord1 in sites.items():
    distances[city1] = {}
    for city2, coord2 in sites.items():
        if city1 != city2:  # Не считаем расстояние до самого себя
            x1, y1 = coord1
            x2, y2 = coord2
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[city1][city2] = round(distance, 2)  # Округляем до 2 знаков

print(distances)
```
<img width="963" height="43" alt="lab1" src="https://github.com/user-attachments/assets/19fda7bb-5136-4b08-852d-10cab60c5830" />

# 01
```python
# Площадь круга
pi = 3.1415926
area = pi * (radius ** 2)
print(round(area, 4))

# Проверка точки 1
point_1 = (23, 34)
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
print(distance_1 <= radius)

# Проверка точки 2
point_2 = (30, 30)
distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
print(distance_2 <= radius)
```
 <img width="89" height="71" alt="lab2" src="https://github.com/user-attachments/assets/0eecd694-9a4e-438b-b4d0-5cd550c5e069" />

# 02
<img width="480" height="570" alt="lab3" src="https://github.com/user-attachments/assets/950a5042-fd6c-4df1-9a25-ade4f4fb835c" />

# 03
<img width="718" height="601" alt="lab4" src="https://github.com/user-attachments/assets/915d9e34-ef0d-4bbb-984b-7d03a3aa0016" />

# 04
<img width="538" height="817" alt="lab5" src="https://github.com/user-attachments/assets/e0cc70a8-b1c5-4935-a0e8-b3259f83ba69" />

# 05
<img width="753" height="904" alt="6" src="https://github.com/user-attachments/assets/edec7e2a-523e-4c96-8068-afaa049f2457" />

# 06
<img width="1372" height="901" alt="7" src="https://github.com/user-attachments/assets/c3267ecd-f2f9-4e65-8e2f-a45a5dc964ec" />

# 07
<img width="724" height="800" alt="8" src="https://github.com/user-attachments/assets/6ac1074a-1fbe-4fd5-8de4-58332903eefa" />

# 08
<img width="897" height="935" alt="9" src="https://github.com/user-attachments/assets/5b69c83c-c6c5-4700-a8d7-93bcca45fb61" />

# 09
<img width="892" height="930" alt="10" src="https://github.com/user-attachments/assets/e7d83b21-4e4c-4667-b701-c4f81fbd4eab" />

# 10
<img width="1043" height="914" alt="11" src="https://github.com/user-attachments/assets/d4d3bd01-c935-4d0f-a8b5-d1a93dab9011" />
