## Логические операторы в Python

Логические операторы в Python позволяют нам создавать условия для выполнения различных участков кода в зависимости от значений переменных и выражений. Это важный инструмент для написания более сложных и интерактивных программ.

### Основные логические операторы

В Python существуют три основных логических оператора:

1. **and** (логическое "и")
2. **or** (логическое "или")
3. **not** (логическое "не")

Эти операторы используются для объединения нескольких условий или для изменения логических значений. Рассмотрим каждый оператор более подробно с примерами кода.

### Оператор `and`

Оператор `and` возвращает `True` только в том случае, если оба операнда являются истинными. Если хотя бы один операнд является ложным, результатом будет `False`.

```python
is_raining = True
have_umbrella = False

if is_raining and have_umbrella:
    print("Можно идти на улицу, у нас есть зонт.")
else:
    print("Лучше остаться дома.")
```

В этом примере программа проверяет, идёт ли дождь и есть ли у нас зонт. Если оба условия истинны, программа разрешает выйти на улицу, иначе советует остаться дома.

### Оператор `or`

Оператор `or` возвращает `True`, если хотя бы один из операндов является истинным. Если оба операнда ложные, результатом будет `False`.

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Сегодня можно отдохнуть.")
else:
    print("Сегодня нужно работать.")
```

Здесь программа проверяет, является ли сегодняшний день выходным или праздничным. Если хотя бы одно из условий истинно, можно отдыхать.

### Оператор `not`

Оператор `not` инвертирует логическое значение операнда. Если операнд был истинным, результатом будет `False`, и наоборот.

```python
is_raining = True

if not is_raining:
    print("Сегодня солнечно!")
else:
    print("На улице дождь.")
```

Этот пример показывает, как `not` используется для проверки, что не идёт дождь.

### Оператор `xor`

Оператор `xor` (исключающее "или") в Python отсутствует как отдельный логический оператор, но его можно реализовать с помощью комбинации операторов `and`, `or` и `not`. Оператор `xor` возвращает `True`, если только одно из двух условий истинно. Если оба условия истинны или оба ложны, результатом будет `False`.

#### Реализация `xor` через логические операторы

В Python оператор `xor` можно имитировать следующим образом:

```python
a = True
b = False

result = (a and not b) or (not a and b)
print(result) # Выведет True
```

В этом примере результатом будет `True`, так как одно из условий истинно.

#### Использование оператора `xor` с булевыми значениями

Для простоты можно использовать встроенный оператор `^` (побитовый XOR) с булевыми значениями, так как он даёт тот же результат, что и логический `xor`.

```python
a = True
b = False

result = a ^ b
print(result) # Выведет True
```

Здесь также результатом будет `True`, так как `a` истинно, а `b` ложно.

#### Примеры использования оператора `xor` (его нет по умолчанию)

Пример 1: Проверка наличия одного из двух условий

```python
is_daytime = True
is_lamp_on = True

if is_daytime ^ is_lamp_on:
    print("Освещение оптимально.")
else:
    print("Освещение не оптимально.")
```

В этом примере проверяется, включён ли свет только в одном из двух случаев: либо день, либо лампа включена. Если оба условия совпадают, освещение считается неоптимальным.

Пример 2: Проверка условий для скидки

```python
has_membership = False
has_discount_coupon = True

if has_membership ^ has_discount_coupon:
    print("Скидка применима.")
else:
    print("Скидка не применима.")
```

Здесь проверяется, что у пользователя либо есть членство, либо купон на скидку, но не оба одновременно.

### Комбинирование логических операторов

Логические операторы можно комбинировать для создания более сложных условий. В таких случаях важно помнить про приоритет операций: `not` имеет самый высокий приоритет, затем `and`, и затем `or`. Для явного указания порядка выполнения условий можно использовать скобки.

```python
age = 25
is_student = False
has_discount_coupon = True

if (age < 18 or is_student) and has_discount_coupon:
    print("Скидка доступна.")
else:
    print("Скидка не доступна.")
```

Здесь проверяется, соответствует ли один из условий для получения скидки: возраст меньше 18 лет или статус студента, и при этом имеется купон на скидку.

### Полезные ссылки:

- [Официальная документация Python](https://docs.python.org/3/)
- [Онлайн интерпретатор Python](https://www.python.org/shell/)
- [Продвинутый курс по терминалу](https://www.learnshell.org/)
- @TODO добавить ссылки на наши соцсети

### Заключение

Логические операторы являются важным инструментом для написания условных выражений в Python. Они позволяют создавать программы, которые могут принимать решения на основе различных условий. В видео уроке мы рассмотрим более сложные примеры использования логических операторов и научимся комбинировать их с другими элементами языка Python (@TODO добавить ссылку на видео урок).

[Следующий урок](https://github.com/sashazenit4/easy-python/blob/master/p4_types/types.md)
