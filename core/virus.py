# ������ ���������
import random as rnd
import string

# ������ �������
import core.model as model

# ������ ������������
import data.settings.default as cfg

class Virus():
    # ������� ��������� ������� � ���������� ��������� ��������� ������
    def __init__(self, ref = None):
        if ref is not None: self.create_params_by_ref(ref)
        else: self.create_params()

    # ������ ��������� ������ �� ������������ � ������������ +- 10% �� ��������
    def create_params(self):
        self.contagiousness = model.cast_param(cfg.VIRUS_CONTAGIOUSNESS, 0.05)
        self.severity = model.cast_param(cfg.VIRUS_SEVERYTI, 0.05)
        self.lethaly = model.cast_param(cfg.VIRUS_LETHALY, 0.05)
        self.mutable = model.cast_param(cfg.VIRUS_MUTABLE, 0.05)
        self.mutate_intensity = cfg.VIRUS_MUTATE_INTENSITY
        self.stain = cfg.VIRUS_STAIN

    # ������ ��������� ������ �� ����������� ���������
    def create_params_by_ref(self, ref):
        self.contagiousness = ref.contagiousness
        self.severity = ref.severity
        self.lethaly =  ref.lethaly
        self.mutable = ref.mutable
        self.stain = ref.stain
        
    # ������� ������� ������� ������
    def try_mutate(self):
        if model.calc_chanse(self.mutable):
            self.mutate()
    
    # ������� ������� ������
    def mutate(self):
        mpc = 0 # Mutated Params Count
        if model.calc_chanse(self.mutate_intensity/2):
            self.contagiousness = model.change_param(self.contagiousness, self.contagiousness, 0.2) # ��������� 0.2 .. 
            mpc += 1
        if model.calc_chanse(self.mutate_intensity):
            self.severity = model.change_param(self.severity, self.severity, 0.2) # ��������� 0.2 ..
            mpc += 1
        # ������ �������� ������ ����� ������ (��������� ����� � ���������� ���������� ����������)
        self.stain += rnd.choice(string.ascii_letters) + str(mpc) 
            
        