import random as rnd
import string

import core.model as model

import data.settings.default as cfg

class Virus():
    def __init__(self, ref = None):
        if ref is not None: self.create_params_by_ref(ref)
        else: self.create_params()

    def create_params(self):
        self.contagiousness = model.cast_param(cfg.VIRUS_CONTAGIOUSNESS, cfg.VIRUS_PARAMS_RANGE)
        self.severity = model.cast_param(cfg.VIRUS_SEVERITY, cfg.VIRUS_PARAMS_RANGE)
        self.lethaly = model.cast_param(cfg.VIRUS_LETHALITY, cfg.VIRUS_PARAMS_RANGE)
        self.mutable = model.cast_param(cfg.VIRUS_MUTABLE, cfg.VIRUS_PARAMS_RANGE)
        self.mutate_intensity = cfg.VIRUS_MUTATE_INTENSITY
        self.stain = cfg.VIRUS_STRAIN

    def create_params_by_ref(self, ref):
        self.contagiousness = ref.contagiousness
        self.severity = ref.severity
        self.lethaly =  ref.lethaly
        self.mutable = ref.mutable
        self.stain = ref.stain

    def try_mutate(self):
        if model.calc_chanse(self.mutable):
            self.mutate()

    def mutate(self):
        mpc = 0 # Mutated Params Count
        if model.calc_chanse(self.mutate_intensity/2):
            self.contagiousness = model.change_param(self.contagiousness, self.contagiousness, cfg.VIRUS_CONTAGIOUSNESS_MUTATE_INTESITY)
            mpc += 1
        if model.calc_chanse(self.mutate_intensity):
            self.severity = model.change_param(self.severity, self.severity, cfg.VIRUS_SEVERITY_MUTATE_INTENSITY)
            mpc += 1
        if model.calc_chanse(self.mutate_intensity):
            self.lethaly = model.change_param(self.lethaly, self.lethaly, cfg.VIRUS_LETHALITY_MUTATE_INTESITY)
            mpc += 1
        self.stain += rnd.choice(string.ascii_letters) + str(mpc) 
            
        