import pygame  # Импорт библиотеки Pygame для работы с графикой и событиями
import pygame_gui  # Импорт библиотеки для работы с графическим интерфейсом (UI)
import math  # Импорт библиотеки для математических операций

# Screen parameters
SCREEN_WIDTH = 800  # Устанавливаем ширину экрана
SCREEN_HEIGHT = 600  # Устанавливаем высоту экрана
FPS = 60  # Частота кадров в секунду (скорость обновления экрана)

# Physical constants
GRAVITY = 9.81  # Ускорение свободного падения на Земле (м/с^2)

# Wave and float parameters
WAVE_SPEED = 0.05  # Скорость изменения волны, на которую влияет время

# Initialize Pygame
pygame.init()  # Инициализируем Pygame
pygame.font.init()  # Инициализируем шрифты Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создаем окно с указанными размерами
pygame.display.set_caption("Волны")  # Устанавливаем заголовок окна
clock = pygame.time.Clock()  # Создаем объект для отслеживания времени (FPS)

# Initialize pygame_gui
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))  # Инициализируем менеджер интерфейса для UI

# Wave class
class Wave:
    def __init__(self, amplitude, period, y_offset=0):  # Конструктор класса для волны
        self.amplitude = amplitude  # Амплитуда волны
        self.period = period  # Период волны
        self.y_offset = y_offset  # Вертикальное смещение волны

    def get_y(self, x, time):  # Метод для расчета вертикальной позиции волны на заданной горизонтальной позиции x и времени
        return self.y_offset + self.amplitude * math.sin(2 * math.pi * (x / self.period + time * WAVE_SPEED))  # Возвращаем значение y для данной волны

# Float class
class Float:
    def __init__(self, mass, volume, x, wave):  # Конструктор класса поплавка
        self.mass = mass  # Масса поплавка
        self.volume = volume  # Объем поплавка
        self.x = x  # Горизонтальная позиция поплавка
        self.y = wave.y_offset  # Вертикальная позиция поплавка (сначала равна смещению волны)
        self.wave = wave  # Привязка поплавка к волне
        self.radius = max(5, int(self.volume * 10))  # Радиус поплавка зависит от его объема (не менее 5)

    def update(self, time):  # Метод для обновления позиции поплавка в зависимости от времени
        wave_y = self.wave.get_y(self.x, time)  # Получаем вертикальную позицию волны для текущей горизонтальной позиции
        weight_force = self.mass * GRAVITY  # Рассчитываем силу тяжести на поплавок
        buoyancy_force = self.volume * GRAVITY  # Рассчитываем силу Архимеда на поплавок
        net_force = buoyancy_force - weight_force  # Суммарная сила

        if net_force >= 0:  # Если сила Архимеда больше или равна силе тяжести
            self.y = wave_y - abs(net_force) * 0.5  # Поплавок будет подниматься над волной
        else:  # Если сила тяжести больше
            self.y = wave_y + abs(net_force) * 0.5  # Поплавок будет опускаться ниже волны

    def is_clicked(self, mouse_pos):  # Метод для проверки, был ли клик по поплавку
        return math.hypot(mouse_pos[0] - self.x, mouse_pos[1] - self.y) <= self.radius  # Проверка, находится ли мышь внутри поплавка

# Initialize data
waves = []  # Список волн
floats = []  # Список поплавков

# UI elements for wave sliders
wave_amplitude_sliders = []  # Список слайдеров для амплитуды волн
wave_period_sliders = []  # Список слайдеров для периода волн
wave_slider_objects = []  # Список для хранения слайдеров и их ассоциированных волн

def create_wave_sliders(wave, index):  # Функция для создания слайдеров для каждой волны
    amplitude_slider = pygame_gui.elements.UIHorizontalSlider(  # Создание слайдера для амплитуды
        pygame.Rect((20, 10 + index * 40), (250, 15)),
        start_value=wave.amplitude,
        value_range=(10, 100),
        manager=manager
    )
    period_slider = pygame_gui.elements.UIHorizontalSlider(  # Создание слайдера для периода
        pygame.Rect((300, 10 + index * 40), (250, 15)),
        start_value=wave.period,
        value_range=(50, 400),
        manager=manager
    )

    # Сохраняем слайдеры с ассоциированной волной
    wave_slider_objects.append({
        'wave': wave,
        'amplitude_slider': amplitude_slider,
        'period_slider': period_slider
    })

# Create buttons for adding and removing waves
add_wave_button = pygame_gui.elements.UIButton(  # Создание кнопки для добавления новой волны
    relative_rect=pygame.Rect(20, 550, 150, 30),
    text='Добавить волну',
    manager=manager
)

remove_wave_button = pygame_gui.elements.UIButton(  # Создание кнопки для удаления последней волны
    relative_rect=pygame.Rect(200, 550, 150, 30),
    text='Удалить волну',
    manager=manager
)

# Create an edit panel for floats
float_edit_panel = None  # Панель редактирования поплавков
selected_float = None  # Выбранный поплавок

def create_float_edit_panel(flt):  # Функция для создания панели редактирования поплавка
    global float_edit_panel, selected_float
    selected_float = flt  # Устанавливаем выбранный поплавок
    float_edit_panel = pygame_gui.elements.UIWindow(  # Создаем окно для редактирования поплавка
        rect=pygame.Rect((200, 150), (400, 300)),
        manager=manager,
        window_display_title="Редактировать параметры поплавка"
    )

    mass_slider = pygame_gui.elements.UIHorizontalSlider(  # Создание слайдера для массы поплавка
        pygame.Rect((50, 50), (300, 50)),
        start_value=flt.mass,
        value_range=(0.1, 10.0),
        manager=manager,
        container=float_edit_panel
    )
    volume_slider = pygame_gui.elements.UIHorizontalSlider(  # Создание слайдера для объема поплавка
        pygame.Rect((50, 150), (300, 50)),
        start_value=flt.volume,
        value_range=(0.1, 5.0),
        manager=manager,
        container=float_edit_panel
    )

    mass_label = pygame_gui.elements.UILabel(  # Подпись для слайдера массы
        pygame.Rect((50, 20), (300, 30)),
        text=f"Масса: {flt.mass:.1f}",
        manager=manager,
        container=float_edit_panel
    )
    volume_label = pygame_gui.elements.UILabel(  # Подпись для слайдера объема
        pygame.Rect((50, 120), (300, 30)),
        text=f"Объем: {flt.volume:.1f}",
        manager=manager,
        container=float_edit_panel
    )

    return mass_slider, volume_slider, mass_label, volume_label  # Возвращаем созданные элементы для дальнейшего использования

# Main loop
running = True  # Флаг для основной петли игры
time = 0  # Время игры
while running:  # Основной цикл игры
    screen.fill((135, 206, 235))  # Закрашиваем экран в цвет неба
    time += 1 / FPS  # Увеличиваем время на основе частоты кадров
    delta_time = clock.tick(FPS) / 1000.0  # Получаем время, прошедшее с последнего кадра

    # Update all floats
    for flt in floats:  # Обновляем все поплавки
        flt.update(time)

    # Draw waves and floats
    for wave in waves:  # Рисуем все волны
        for x in range(0, SCREEN_WIDTH, 2):  # Проходим по всем горизонтальным точкам экрана
            y = int(wave.get_y(x, time)) - 10  # Получаем вертикальную позицию волны
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 2)  # Рисуем маленький круг для волны

    for flt in floats:  # Рисуем все поплавки
        pygame.draw.circle(screen, (255, 69, 0), (int(flt.x), int(flt.y)), flt.radius)  # Рисуем поплавок как круг

    for event in pygame.event.get():  # Обрабатываем все события
        if event.type == pygame.QUIT:  # Если окно закрывается
            running = False  # Завершаем программу
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Если кликнута левая кнопка мыши
            if add_wave_button.rect.collidepoint(event.pos):  # Если клик на кнопку добавления волны
                y_offset = len(waves) * 100 + 50  # Сдвигаем новую волну по вертикали
                wave = Wave(amplitude=50, period=200, y_offset=y_offset)  # Создаем новую волну
                waves.append(wave)  # Добавляем волну в список
                floats.extend([Float(mass=1.0, volume=1.0, x=100 + i * 100, wave=wave) for i in range(5)])  # Добавляем поплавки для этой волны
                create_wave_sliders(wave, len(waves) - 1)  # Создаем слайдеры для этой волны

            elif remove_wave_button.rect.collidepoint(event.pos) and waves:  # Если клик на кнопку удаления волны
                last_wave = waves.pop()  # Удаляем последнюю волну
                floats = [flt for flt in floats if flt.wave != last_wave]  # Удаляем поплавки, привязанные к этой волне

                # Удаляем слайдеры, связанные с удаленной волной
                wave_slider_objects_to_remove = [obj for obj in wave_slider_objects if obj['wave'] == last_wave]
                for obj in wave_slider_objects_to_remove:
                    obj['amplitude_slider'].kill()  # Удаляем слайдеры
                    obj['period_slider'].kill()
                wave_slider_objects = [obj for obj in wave_slider_objects if obj['wave'] != last_wave]  # Обновляем список слайдеров

                # Обновляем позиции оставшихся слайдеров
                for i, obj in enumerate(wave_slider_objects):
                    obj['amplitude_slider'].rect.y = 10 + i * 40
                    obj['period_slider'].rect.y = 10 + i * 40

            # Проверяем, был ли клик по поплавку
            for flt in floats:
                if flt.is_clicked(event.pos):  # Если поплавок был кликнут
                    sliders = create_float_edit_panel(flt)  # Открываем панель редактирования для поплавка

        manager.process_events(event)  # Обрабатываем события интерфейса

    # Update wave parameters from sliders
    for i, wave in enumerate(waves):  # Обновляем параметры волн из слайдеров
        wave.amplitude = wave_slider_objects[i]['amplitude_slider'].get_current_value()
        wave.period = wave_slider_objects[i]['period_slider'].get_current_value()

    # Update float parameters from sliders
    if float_edit_panel:  # Если панель редактирования поплавка открыта
        sliders[2].set_text(f"Масса: {sliders[0].get_current_value():.1f}")  # Обновляем текст метки массы
        sliders[3].set_text(f"Объем: {sliders[1].get_current_value():.1f}")  # Обновляем текст метки объема
        selected_float.mass = sliders[0].get_current_value()  # Обновляем массу поплавка
        selected_float.volume = sliders[1].get_current_value()  # Обновляем объем поплавка
        selected_float.radius = max(5, int(selected_float.volume * 10))  # Обновляем радиус поплавка в зависимости от объема

    # Обновление интерфейса и отображение
    manager.update(delta_time)  # Обновляем все элементы интерфейса
    manager.draw_ui(screen)  # Отображаем интерфейс
    pygame.display.flip()  # Обновляем экран

pygame.quit()  # Завершаем работу с Pygame
