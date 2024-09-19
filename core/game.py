# Импорт библиотек
from tokenize import group
from venv import create
import pygame
import random

# Импорт игровых модулей
import core.borders as borders
import core.groups as groups
import core.pawn as pawn
import core.pawn_states as states
import data.simulations.sim_statistic as stat

# Импорт конфигурации
import data.settings.default as cfg


# Класс игры(сессии)
class Session():
    # Создает экземпляр объекта и определяет некоторые параметры класса
    def __init__(self, use_steps = False):
        self.use_steps = use_steps
        if self.use_steps:
            self.sim_steps = cfg.SIM_STEPS
            self.current_step = 0
        self.create_sprite_groups()
        self.create_location()
    
    # Создает группы для спрайтов(игровых объектов)
    def create_sprite_groups(self):
        groups.drawable_group = pygame.sprite.Group()
        groups.borders_group = pygame.sprite.Group()
        groups.vertical_borders_group = pygame.sprite.Group()
        groups.horizontal_borders_group = pygame.sprite.Group()
        groups.pawns_group = pygame.sprite.Group()
        groups.updatable_group = pygame.sprite.Group()
        
    # Создает игровую локацию и границы доступной области
    def create_location(self):
        self.window_size = (cfg.SIM_WINDOW_WIDTH, cfg.SIM_WINDOW_HEIGHT)
        borders.create_borders()
        self.screen = pygame.display.set_mode(self.window_size)
    
    # Создает игровые часы и устанавливает скорость симуляции (FPS)
    def create_clock(self):
        self.clock = pygame.time.Clock()
        self.tickspeed = cfg.SIM_SPEED
    
    # Проверяет состояние симуляции и отвечает за завершение игрового цикла
    def game_is_continues(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return False
        if self.use_steps and self.current_step >= self.sim_steps:
            return False 
        else:
            return True   
    
    # Если симуляция использует шаги, то добавляет единицу к current_step
    def increment_step(self):
        if self.use_steps: self.current_step += 1
        
    def tick(self):
        self.clock.tick(self.tickspeed)
    
    # Рисует все объекты, которые должны отрисовываться в процессе игры (из группы drawable_obj) и обновляет экран
    def draw_objects(self):
        self.screen.fill(pygame.Color(cfg.SCREEN_COLOR))
        groups.borders_group.draw(self.screen)
        groups.pawns_group.draw(self.screen)
        pygame.display.flip()
        
    # Обновляет все объекты, которые должны обновляться в процессе игры (из группы updatable_obj)
    def update_object(self):
        groups.pawns_group.update()
    
    # Создает пешек
    def create_pawns(self):
        for _ in range(cfg.SIM_START_PAWN_COUNT):
            pawn.Pawn(10)
            
    # Проводит необходимые действия для подготовки сессии
    def prepare_game(self):
        self.create_clock()
        self.create_pawns()
        
    def catch_statistic(self):    
        healthy_pawn = 0
        infected_pawn = 0
        dead_pawn = 0
        
        for pawn in groups.pawns_group:
            if isinstance(pawn.state, states.Healthy):
                healthy_pawn += 1
            if isinstance(pawn.state, states.Infected):
                infected_pawn += 1
            if isinstance(pawn.state, states.Dead):
                dead_pawn += 1

        stat.data.append([healthy_pawn, infected_pawn, dead_pawn])
        
    
    # Основной игровой цикл
    def simulate(self):
        pygame.init()
        self.prepare_game()
        
        while self.game_is_continues():
            self.update_object()
            self.draw_objects()
            self.tick()
            self.increment_step()
            
            self.catch_statistic()

        pygame.quit()