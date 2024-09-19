# Импорт библиотек
import random as rnd
import string

# Импорт модулей
import core.model as model

# Импорт конфигурации
import data.settings.default as cfg

class Virus():
    # Создает экземпляр объекта и определяет некоторые параметры класса
    def __init__(self, ref = None):
        if ref is not None: self.create_params_by_ref(ref)
        else: self.create_params()

    # Задает параметры вируса по установленым в конфигурации +- 10% от значения
    def create_params(self):
        self.contagiousness = model.cast_param(cfg.VIRUS_CONTAGIOUSNESS, 0.05)
        self.severity = model.cast_param(cfg.VIRUS_SEVERYTI, 0.05)
        self.lethaly = model.cast_param(cfg.VIRUS_LETHALY, 0.05)
        self.mutable = model.cast_param(cfg.VIRUS_MUTABLE, 0.05)
        self.mutate_intensity = cfg.VIRUS_MUTATE_INTENSITY
        self.stain = cfg.VIRUS_STAIN

    # Задает параметры вируса по переданному референсу
    def create_params_by_ref(self, ref):
        self.contagiousness = ref.contagiousness
        self.severity = ref.severity
        self.lethaly =  ref.lethaly
        self.mutable = ref.mutable
        self.stain = ref.stain
        
    # Пробуем вызвать мутацию вируса
    def try_mutate(self):
        if model.calc_chanse(self.mutable):
            self.mutate()
    
    # Процесс мутации вируса
    def mutate(self):
        mpc = 0 # Mutated Params Count
        if model.calc_chanse(self.mutate_intensity/2):
            self.contagiousness = model.change_param(self.contagiousness, self.contagiousness, 0.2) # Подобрать 0.2 .. 
            mpc += 1
        if model.calc_chanse(self.mutate_intensity):
            self.severity = model.change_param(self.severity, self.severity, 0.2) # Подобрать 0.2 ..
            mpc += 1
        # Задаем название новому штаму вируса (случайная буква и количество измененных параметров)
        self.stain += rnd.choice(string.ascii_letters) + str(mpc) 
            
        