
# Основные параметры симуляции

# Высота игрового окна
SIM_WINDOW_HEIGHT = 1000
# Ширина игрового окна
SIM_WINDOW_WIDTH = 1500
# Скорость симуляции(FPS)
SIM_SPEED=30
# Длина симуляции(в шагах)
SIM_STEPS=2000
# Цвет экрана
SCREEN_COLOR = "white"
# Начальное количество пешек
SIM_START_PAWN_COUNT = 1000

# Основные параметры границы локации(стен)

# Отступ границы от края экрана
BORDER_OFFSET = 2.5
# Толщина границы
BORDER_THICKNESS = 5
# Цвет границы
BORDER_COLOR = "black"

# Основные параметры пешки

# Размер пешки
PAWN_RADIUS = 2.5
# Базовый цвет пешки
PAWN_BASE_COLOR = "yellow"
# Скорость пешки
PAWN_MAX_SPEED = 5
# Максимальный начальный иммунитет
PAWN_MAX_START_IMMUNITY = 0.1
# Шанс случайно заболеть
PAWN_SICK_ACCIDENTALLY = 0.005

# Основные параметры вируса(начальный штамм)

# Заразность
VIRUS_CONTAGIOUSNESS = 0.7
# Тяжесть
VIRUS_SEVERYTI = 0.02
# Летальность
VIRUS_LETHALY = 0
# Способоность к мутации
VIRUS_MUTABLE = 0.1
# Интенсивность мутаций
VIRUS_MUTATE_INTENSITY = 0.1
# Название
VIRUS_NAME = "Curse"
# Штамм
VIRUS_STAIN = ""

# Основные параметры состояний

# Здоровый

# Цвет
HEALTHY_STATE_COLOR = "green"

# Мертвый

# Цвет
DEAD_STATE_COLOR = "gray"

# Инфицированый

# Цвет
INFECTED_STATE_COLOR = "red"
# Скорость течения болезни
INFECTED_STATE_DISEASE_COEF = 0.15
# Скорость выработки иммунитета
INFECTED_STATE_IMMUNITY_COEF = 0.2