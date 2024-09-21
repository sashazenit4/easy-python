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

game = SnakeGame(10, 10)

while not game.check_collision():
    game.draw()
    direction = input("Введите направление (UP, DOWN, LEFT, RIGHT): ").upper()
    game.change_direction(direction)
    game.update()
