## Популярные методы на типах данных в Python

Python предоставляет большое количество встроенных методов для работы с различными типами данных, такими как строки, списки, кортежи, словари и множества. Эти методы помогают решать повседневные задачи, делая код более лаконичным и читаемым. В этой статье мы рассмотрим наиболее часто используемые методы для каждого типа данных.

### 1. Строки (`str`)

Строки в Python — это неизменяемые последовательности символов. Для работы с ними существует множество методов, которые упрощают манипуляции с текстом.

#### Основные методы работы со строками:

- **`str.upper()`** — Преобразует строку к верхнему регистру.
  
  ```python
  text = "hello"
  print(text.upper())  # HELLO
  ```

- **`str.lower()`** — Преобразует строку к нижнему регистру.
  
  ```python
  text = "HELLO"
  print(text.lower())  # hello
  ```

- **`str.replace(old, new)`** — Заменяет все вхождения подстроки `old` на `new`.
  
  ```python
  text = "I love apples"
  print(text.replace("apples", "bananas"))  # I love bananas
  ```

- **`str.split(separator)`** — Разбивает строку на части, возвращая список строк.
  
  ```python
  text = "apple, banana, cherry"
  fruits = text.split(", ")
  print(fruits)  # ['apple', 'banana', 'cherry']
  ```

- **`str.join(iterable)`** — Соединяет элементы из итерируемого объекта (например, списка) в строку с указанным разделителем.
  
  ```python
  fruits = ["apple", "banana", "cherry"]
  result = ", ".join(fruits)
  print(result)  # apple, banana, cherry
  ```

- **`str.strip()`** — Удаляет начальные и конечные пробелы (или указанные символы).
  
  ```python
  text = "  hello  "
  print(text.strip())  # "hello"
  ```

- **`str.find(sub)`** — Возвращает индекс первого вхождения подстроки `sub`, или -1, если подстрока не найдена.
  
  ```python
  text = "hello world"
  print(text.find("world"))  # 6
  ```

### 2. Списки (`list`)

Списки — это изменяемые последовательности объектов. Python предоставляет множество методов для добавления, удаления и сортировки элементов списка.

#### Основные методы работы со списками:

- **`list.append(item)`** — Добавляет элемент в конец списка.
  
  ```python
  fruits = ["apple", "banana"]
  fruits.append("cherry")
  print(fruits)  # ['apple', 'banana', 'cherry']
  ```

- **`list.insert(index, item)`** — Вставляет элемент в список по указанному индексу.
  
  ```python
  fruits = ["apple", "banana"]
  fruits.insert(1, "cherry")
  print(fruits)  # ['apple', 'cherry', 'banana']
  ```

- **`list.remove(item)`** — Удаляет первое вхождение элемента.
  
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.remove("banana")
  print(fruits)  # ['apple', 'cherry']
  ```

- **`list.pop(index)`** — Удаляет элемент по указанному индексу и возвращает его. Если индекс не указан, удаляет последний элемент.
  
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruit = fruits.pop()
  print(fruit)  # cherry
  print(fruits)  # ['apple', 'banana']
  ```

- **`list.sort()`** — Сортирует список по возрастанию.
  
  ```python
  numbers = [3, 1, 2]
  numbers.sort()
  print(numbers)  # [1, 2, 3]
  ```

- **`list.reverse()`** — Переворачивает порядок элементов в списке.
  
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.reverse()
  print(fruits)  # ['cherry', 'banana', 'apple']
  ```

- **`list.extend(iterable)`** — Расширяет список элементами из итерируемого объекта (списка, кортежа и т.д.).
  
  ```python
  fruits = ["apple", "banana"]
  more_fruits = ["cherry", "orange"]
  fruits.extend(more_fruits)
  print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
  ```

### 3. Кортежи (`tuple`)

Кортежи — это неизменяемые последовательности объектов. Методов у кортежей немного, так как они не могут изменяться.

#### Основные методы работы с кортежами:

- **`tuple.count(item)`** — Возвращает количество вхождений элемента в кортеже.
  
  ```python
  fruits = ("apple", "banana", "apple")
  print(fruits.count("apple"))  # 2
  ```

- **`tuple.index(item)`** — Возвращает индекс первого вхождения элемента.
  
  ```python
  fruits = ("apple", "banana", "cherry")
  print(fruits.index("banana"))  # 1
  ```

### 4. Словари (`dict`)

Словари хранят пары ключ-значение. Методы словарей позволяют эффективно управлять и извлекать данные.

#### Основные методы работы со словарями:

- **`dict.get(key, default)`** — Возвращает значение по ключу, если ключ существует, иначе возвращает значение по умолчанию.
  
  ```python
  person = {"name": "Alice", "age": 25}
  print(person.get("name"))  # Alice
  print(person.get("job", "Unknown"))  # Unknown
  ```

- **`dict.update(other_dict)`** — Обновляет словарь элементами из другого словаря.
  
  ```python
  person = {"name": "Alice", "age": 25}
  additional_info = {"job": "Developer"}
  person.update(additional_info)
  print(person)  # {'name': 'Alice', 'age': 25, 'job': 'Developer'}
  ```

- **`dict.pop(key)`** — Удаляет элемент с указанным ключом и возвращает его значение.
  
  ```python
  person = {"name": "Alice", "age": 25}
  age = person.pop("age")
  print(age)  # 25
  print(person)  # {'name': 'Alice'}
  ```

- **`dict.keys()`** — Возвращает все ключи словаря.
  
  ```python
  person = {"name": "Alice", "age": 25}
  print(person.keys())  # dict_keys(['name', 'age'])
  ```

- **`dict.values()`** — Возвращает все значения словаря.
  
  ```python
  person = {"name": "Alice", "age": 25}
  print(person.values())  # dict_values(['Alice', 25])
  ```

- **`dict.items()`** — Возвращает пары ключ-значение в виде кортежей.
  
  ```python
  person = {"name": "Alice", "age": 25}
  print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
  ```

### 5. Множества (`set`)

Множества содержат уникальные элементы и предоставляют методы для выполнения операций над множествами.

#### Основные методы работы с множествами:

- **`set.add(item)`** — Добавляет элемент в множество.
  
  ```python
  numbers = {1, 2, 3}
  numbers.add(4)
  print(numbers)  # {1, 2, 3, 4}
  ```

- **`set.remove(item)`** — Удаляет элемент из множества. Вызывает ошибку, если элемент не найден.
  
  ```python
  numbers = {1, 2, 3}
  numbers.remove(2)
  print(numbers)  # {1, 3}
  ```

- **`set.discard(item)`** — Удаляет элемент из множества. Не вызывает ошибку, если элемент не найден.
  
  ```python
  numbers = {1, 2, 3}
  numbers.discard(4)
  print(numbers)  # {1, 2, 3}
  ```

- **`set.union(other_set)`** — Возвращает объединение множеств.
  
  ```python
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  result = set1.union(set2)
  print(result)  # {1, 2, 3, 4, 5}
  ```

- **`set.intersection(other_set)`** — Возвращает пересечение множеств.
  
  ```python
  set1 =

 {1, 2, 3}
  set2 = {2, 3, 4}
  result = set1.intersection(set2)
  print(result)  # {2, 3}
  ```

- **`set.difference(other_set)`** — Возвращает разность множеств (элементы, присутствующие в первом множестве, но отсутствующие во втором).
  
  ```python
  set1 = {1, 2, 3}
  set2 = {2, 3, 4}
  result = set1.difference(set2)
  print(result)  # {1}
  ```

### Полезные ссылки:

- [Официальная документация Python по встроенным типам данных](https://docs.python.org/3/library/stdtypes.html)
- @TODO добавить ссылки на наши соцсети

### Заключение

В этой статье мы рассмотрели основные методы работы с различными типами данных в Python. Эти методы делают код более эффективным и упрощают решение типичных задач. В следующем уроке мы рассмотрим пользовательские функции и как их использовать для улучшения кода.

[Следующий урок](https://github.com/sashazenit4/easy-python/blob/master/p7_functions/def.md)
