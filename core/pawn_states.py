from abc import ABC, abstractclassmethod

from core.virus import Virus
import core.model as model

import data.settings.default as cfg

class Pawn_state(ABC):
    def __init__(self):
        super().__init__()
        self.is_dead = False
        self.is_healing = False

    @abstractclassmethod
    def progress(): pass
    
class Healthy(Pawn_state):
    def __init__(self):
        super().__init__()
        self.color = cfg.HEALTHY_STATE_COLOR
    
    def progress(self):
        pass
    
class Dead(Pawn_state):
    def __init__(self, reason_virus):
        super().__init__()
        self.color = cfg.DEAD_STATE_COLOR
        self.virus = reason_virus

    def progress(self):
        pass
    
class Infected(Pawn_state):
    def __init__(self, immunity, reason_virus):
        super().__init__()
        self.color = cfg.INFECTED_STATE_COLOR
        self.virus = reason_virus
        self.immunity = immunity
        self.disease = 0

    def progress(self):
        self.progress_desease()
        self.try_heal()
        self.try_instant_death()
        self.virus.try_mutate()

    def progress_desease(self):
        self.disease = model.change_param(self.disease, self.virus.severity, cfg.INFECTED_STATE_DISEASE_COEF)
        self.immunity = model.change_param(self.immunity, self.virus.severity, cfg.INFECTED_STATE_IMMUNITY_COEF)
        if self.disease >= 0.7 and model.calc_chanse(self.disease):
            self.is_dead = True

    def try_heal(self):
        if self.immunity > 0.7 and model.calc_chanse(self.immunity):
            self.is_healing = True

    def try_instant_death(self):
        if model.calc_chanse(self.virus.lethaly):
            self.is_dead = True