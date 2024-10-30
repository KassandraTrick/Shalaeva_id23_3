import pygame
import json
import math
import os

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Параметры волн и поплавков
NUM_WAVES = 3
NUM_FLOATS = 5
WAVE_SPEED = 0.05
WAVE_SPACING = SCREEN_HEIGHT // (NUM_WAVES + 1)  # Расстояние между волнами

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Волны")
clock = pygame.time.Clock()

# Начальные данные (если нет JSON файла)
initial_data = {
    "waves": [{"amplitude": 20 + i * 10, "period": 100 + i * 50} for i in range(NUM_WAVES)],
    "floats": [{"mass": 5, "volume": 10, "position": 100 * i} for i in range(NUM_FLOATS)]
}

# Функция для загрузки или создания JSON файла
def load_initial_data(file_name="initial_data.json"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
    else:
        with open(file_name, "w") as file:
            json.dump(initial_data, file, indent=4)
        data = initial_data
    return data

data = load_initial_data()

# Модель волн
class Wave:
    def __init__(self, amplitude, period, phase=0, y_offset=0):
        self.amplitude = amplitude
        self.period = period
        self.phase = phase
        self.y_offset = y_offset  # Смещение волны по вертикали

    def get_y(self, x, time):
        return self.y_offset + self.amplitude * math.sin(
            2 * math.pi * (x / self.period + time * WAVE_SPEED) + self.phase)

# Модель поплавков
class Float:
    def __init__(self, mass, volume, x, wave):
        self.mass = mass
        self.volume = volume
        self.x = x
        self.y = wave.y_offset  # Поплавок на уровне своей волны
        self.wave = wave

    def update(self, time):
        # Позиция поплавка по y обновляется в зависимости от высоты волны
        wave_y = self.wave.get_y(self.x, time)

        # Рассчитываем вес поплавка, влияющий на его положение
        weight_force = self.mass * 9.81  # Сила тяжести (массa * g)
        buoyancy_force = self.volume * 9.81  # Сила Архимеда (объем * g)

        # Определяем, насколько поплавок поднимается или опускается
        net_force = buoyancy_force - weight_force

        # Изменяем позицию поплавка в зависимости от чистой силы
        self.y = wave_y + (net_force / weight_force) * 10  # Множитель для увеличения эффекта

# Создаем волны с разными уровнями
waves = [Wave(amplitude=wave["amplitude"], period=wave["period"], y_offset=WAVE_SPACING * (i + 1)) for i, wave in
         enumerate(data["waves"])]



# Создаем поплавки, распределенные по волнам
floats = [Float(mass=flt["mass"], volume=flt["volume"], x=flt["position"], wave=waves[i % len(waves)]) for i, flt in
          enumerate(data["floats"])]

# Основной цикл программы
running = True
time = 0
while running:
    screen.fill((135, 206, 235))  # Цвет фона (небесно-голубой)
    time += 1 / FPS

    # Обновляем поплавки
    for flt in floats:
        flt.update(time)

    # Отрисовываем волны
    for wave in waves:
        for x in range(0, SCREEN_WIDTH, 2):
            y = int(wave.get_y(x, time)) - 10
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 2)

    # Отрисовываем поплавки
    for flt in floats:
        pygame.draw.circle(screen, (255, 69, 0), (int(flt.x), int(flt.y)), 10)  # Оранжевые поплавки

    # Проверяем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновляем экран и ждем следующего кадра
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

