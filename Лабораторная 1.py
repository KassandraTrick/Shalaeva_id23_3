import tkinter as tk
import math


class MovingPointApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Движущаяся точка по окружности")

        # Задаем размер окна
        self.canvas_size = 600
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        # Параметры окружности и точки
        self.center_x = self.canvas_size // 2
        self.center_y = self.canvas_size // 2
        self.radius = 200
        self.angle = 0  # Текущий угол в радианах
        self.speed = 0.05 #  Изменяем скорость движения (угол в радианах за шаг)

        # Рисуем окружность
        self.canvas.create_oval(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            outline="black"
        )

        # Создаем точку
        self.point = self.canvas.create_oval(
            self.center_x - 5, self.center_y - 5,
            self.center_x + 5, self.center_y + 5,
            fill="red"
        )

        # Запускаем анимацию
        self.update_point()

    def update_point(self):
        # Вычисляем координаты точки на окружности
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)

        # Перемещаем точку на новые координаты
        self.canvas.coords(self.point,
                           x - 5, y - 5,
                           x + 5, y + 5)

        # Обновляем угол для следующего положения
        self.angle += self.speed
        if self.angle >= 2 * math.pi:  # Если угол превышает 360 градусов
            self.angle -= 2 * math.pi  # Сбрасываем угол

        # Повторяем обновление через 50 мс
        self.root.after(50, self.update_point)


if __name__ == "__main__":
    root = tk.Tk()
    app = MovingPointApp(root)
    root.mainloop()