## ООП в Python: Приватные и Публичные Свойства и Методы. Класс для игры "Змейка"

В предыдущем уроке мы познакомились с основными принципами объектно-ориентированного программирования (ООП). Теперь давайте посмотрим, как эти принципы применяются в Python, и создадим класс для простой игры "Змейка". Мы также рассмотрим, как работают приватные и публичные свойства и методы.

### 1. Основы ООП в Python

Класс — это шаблон для создания объектов. В Python классы создаются с помощью ключевого слова `class`. Объекты — это экземпляры класса, которые имеют свои свойства и методы.

#### Пример создания класса:

```python
class Snake:
    def __init__(self, name, length):
        self.name = name  # Публичное свойство
        self.length = length  # Публичное свойство

    def move(self):
        print(f"Змейка {self.name} движется.")
```

Здесь мы создали класс `Snake` с публичными свойствами `name` и `length`, а также методом `move()`.

### 2. Публичные и Приватные Свойства и Методы

В Python свойства и методы могут быть **публичными** (доступны извне) или **приватными** (скрыты от внешнего доступа).

- **Публичные свойства и методы**: доступны вне класса и могут быть изменены или вызваны напрямую.
- **Приватные свойства и методы**: начинаются с двойного подчеркивания `__` и не могут быть вызваны напрямую за пределами класса.

#### Пример с публичными и приватными свойствами:

```python
class Snake:
    def __init__(self, name, length):
        self.name = name  # Публичное свойство
        self.length = length  # Публичное свойство
        self.__speed = 5  # Приватное свойство

    def move(self):
        print(f"Змейка {self.name} движется со скоростью {self.__speed}.")

    def __slither(self):
        print(f"Змейка {self.name} тихо ползёт.")  # Приватный метод

    def change_speed(self, new_speed):
        self.__speed = new_speed
        print(f"Скорость змейки изменена на {self.__speed}.")
```

Здесь:
- `name` и `length` — публичные свойства, доступные извне.
- `__speed` — приватное свойство, доступное только внутри класса.
- `move()` — публичный метод, который можно вызвать снаружи.
- `__slither()` — приватный метод, который нельзя вызывать извне.

Попробуем вызвать приватный метод снаружи:

```python
snake = Snake("Python", 10)
snake.move()  # Работает
# snake.__slither()  # Ошибка, приватный метод нельзя вызвать извне
```

### 3. Описание класса для игры "Змейка"

Теперь создадим класс `SnakeGame`, который будет управлять логикой игры "Змейка" в консоли. Класс будет включать:
- Позицию змейки
- Управление движением
- Отображение на экране

#### Начальная версия класса "Змейка":

```python
import random

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]  # Начальная позиция змейки
        self.direction = 'UP'  # Направление движения
        self.food = self._place_food()  # Еда в случайном месте
    
    # Метод для движения змейки
    def move(self):
        head_x, head_y = self.snake[0]
        
        if self.direction == 'UP':
            head_y -= 1
        elif self.direction == 'DOWN':
            head_y += 1
        elif self.direction == 'LEFT':
            head_x -= 1
        elif self.direction == 'RIGHT':
            head_x += 1
        
        # Обновление позиции змейки
        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]
    
    # Метод для изменения направления движения
    def change_direction(self, new_direction):
        if new_direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            self.direction = new_direction
    
    # Метод для проверки столкновений
    def check_collision(self):
        head_x, head_y = self.snake[0]
        
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            return True  # Столкновение со стеной
        
        if (head_x, head_y) in self.snake[1:]:
            return True  # Столкновение с самим собой
        
        return False
    
    # Метод для размещения еды на поле
    def _place_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    # Метод для отрисовки игрового поля
    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.snake:
                    print('S', end=' ')  # Тело змейки
                elif (x, y) == self.food:
                    print('F', end=' ')  # Еда
                else:
                    print('.', end=' ')  # Пустое поле
            print()  # Перенос строки
    
    # Метод для обновления игры (движение змейки и проверка еды)
    def update(self):
        self.move()
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])  # Змейка растёт
            self.food = self._place_food()  # Перемещаем еду
```

### Описание методов:
- **`__init__(self, width, height)`** — Инициализирует игровое поле, начальную позицию змейки и размещает еду.
- **`move(self)`** — Обновляет позицию змейки в зависимости от текущего направления.
- **`change_direction(self, new_direction)`** — Изменяет направление движения змейки.
- **`check_collision(self)`** — Проверяет столкновение змейки со стенами или своим телом.
- **`_place_food(self)`** — Находит случайное место для еды, не занятое змейкой.
- **`draw(self)`** — Отображает текущее состояние игрового поля.
- **`update(self)`** — Обновляет игру: движет змейку и проверяет, съедена ли еда.

### Пример игры в консоли:

```python
game = SnakeGame(10, 10)

while not game.check_collision():
    game.draw()
    direction = input("Введите направление (UP, DOWN, LEFT, RIGHT): ").upper()
    game.change_direction(direction)
    game.update()
```

### Полезные ссылки:

- [Официальная документация Python по классам](https://docs.python.org/3/tutorial/classes.html)
- @TODO добавить ссылки на наши соцсети

### Заключение

Мы рассмотрели основы ООП в Python, изучили публичные и приватные свойства и методы, а также создали класс для игры "Змейка". В этом классе мы применили основные концепции ООП: инкапсуляцию данных (приватные методы), абстракцию (простая логика управления), и возможность расширения класса (например, для добавления новых возможностей в игру). В следующем уроке мы углубимся в наследование и полиморфизм на примерах. 


[Следующий урок](https://github.com/sashazenit4/easy-python/blob/master/p9_python_oop/poly-and-inheritance.md)
