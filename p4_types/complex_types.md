## Сложные типы данных в Python

Сложные типы данных в Python позволяют хранить и манипулировать коллекциями объектов. Они предоставляют гибкость для работы с данными, начиная от списков до словарей, обеспечивая более мощные инструменты для разработки программ. В этой части мы рассмотрим основные сложные типы данных, такие как списки, кортежи и словари, с примерами кода.

### Основные сложные типы данных

1. **Списки (`list`)**
2. **Кортежи (`tuple`)**
3. **Словари (`dict`)**
4. **Множества (`set`)**

### Списки (`list`)

Списки — это упорядоченные изменяемые коллекции объектов. Они могут содержать объекты разных типов и поддерживают различные методы для работы с элементами.

```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True, 3.14]

print(type(numbers))  # <class 'list'>
```

**Основные операции со списками:**

```python
# Доступ к элементам по индексу
print(fruits[0])  # apple

# Изменение элемента
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Добавление элемента в конец
fruits.append("orange")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'orange']

# Удаление элемента по значению
fruits.remove("cherry")
print(fruits)  # ['apple', 'blueberry', 'orange']

# Срезы
print(numbers[1:4])  # [2, 3, 4]

# Объединение списков
more_fruits = ["grape", "melon"]
all_fruits = fruits + more_fruits
print(all_fruits)  # ['apple', 'blueberry', 'orange', 'grape', 'melon']
```

**Перебор элементов списка:**

```python
for fruit in fruits:
    print(fruit)
```

**Методы работы со списками:**

```python
# Длина списка
print(len(fruits))  # 3

# Проверка наличия элемента
print("apple" in fruits)  # True

# Очистка списка
fruits.clear()
print(fruits)  # []
```

### Кортежи (`tuple`)

Кортежи похожи на списки, но в отличие от них, они неизменяемы (immutable). Это делает их полезными для хранения данных, которые не должны изменяться.

```python
coordinates = (10.0, 20.0)
person = ("John", 25, "Engineer")

print(type(coordinates))  # <class 'tuple'>
```

**Операции с кортежами:**

```python
# Доступ к элементам
print(coordinates[0])  # 10.0

# Нельзя изменять элементы кортежа
# coordinates[0] = 15  # Ошибка: кортежи неизменяемы

# Можно использовать срезы
print(person[1:])  # (25, 'Engineer')

# Распаковка кортежей
name, age, job = person
print(name)  # John
print(age)   # 25
print(job)   # Engineer
```

**Методы работы с кортежами:**

```python
# Подсчёт количества элементов
print(person.count("John"))  # 1

# Нахождение индекса элемента
print(person.index("Engineer"))  # 2
```

### Словари (`dict`)

Словари — это неупорядоченные изменяемые коллекции пар ключ-значение. Они позволяют быстро находить значения по ключам.

```python
person = {
    "name": "Alice",
    "age": 30,
    "job": "Developer"
}

print(type(person))  # <class 'dict'>
```

**Операции со словарями:**

```python
# Доступ к значению по ключу
print(person["name"])  # Alice

# Изменение значения
person["age"] = 31
print(person["age"])  # 31

# Добавление новой пары ключ-значение
person["city"] = "New York"
print(person)  # {'name': 'Alice', 'age': 31, 'job': 'Developer', 'city': 'New York'}

# Удаление пары по ключу
del person["job"]
print(person)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Перебор ключей и значений
for key, value in person.items():
    print(f"{key}: {value}")
```

**Методы работы со словарями:**

```python
# Проверка наличия ключа
print("name" in person)  # True

# Получение всех ключей
print(person.keys())  # dict_keys(['name', 'age', 'city'])

# Получение всех значений
print(person.values())  # dict_values(['Alice', 31, 'New York'])

# Очистка словаря
person.clear()
print(person)  # {}
```

### Множества (`set`)

Множества — это неупорядоченные коллекции уникальных элементов. Они полезны для проверки наличия элементов и выполнения операций над множествами.

```python
unique_numbers = {1, 2, 3, 4, 4, 5}
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

**Основные операции с множествами:**

```python
# Добавление элемента
unique_numbers.add(6)
print(unique_numbers)  # {1, 2, 3, 4, 5, 6}

# Удаление элемента
unique_numbers.remove(3)
print(unique_numbers)  # {1, 2, 4, 5, 6}

# Объединение множеств
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # {1, 2, 3, 4, 5}

# Пересечение множеств
intersection_set = set1 & set2
print(intersection_set)  # {3}
```

### Примеры использования сложных типов данных

#### Пример 1: Подсчёт частоты элементов в списке

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)  # {1: 1, 2: 2, 3: 3, 4: 4}
```

#### Пример 2: Распаковка и обмен значениями с кортежами

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

#### Пример 3: Применение операций над множествами

```python
students_A = {"Alice", "Bob", "Charlie"}
students_B = {"Bob", "Diana", "Eve"}

# Студенты, которые учатся в обеих группах
common_students = students_A & students_B
print(common_students)  # {'Bob'}

# Все студенты из обеих групп
all_students = students_A | students_B
print(all_students)  # {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
```

### Полезные ссылки

- [Официальная документация Python](https://docs.python.org/3/)
- [Онлайн интерпретатор Python](https://www.python.org/shell/)
- [Учебник по Python](https://pythonworld.ru/)

### Заключение

Сложные типы данных, такие как списки, кортежи, словари и множества, предоставляют богатый набор возможностей для работы с коллекциями данных в Python. Они играют важную роль в программировании, делая код более гибким и эффективным. В следующем уроке мы углубимся в работу с функциями и генераторами в Python. 

Следующий урок (@TODO добавить ссылку на следующий урок)
