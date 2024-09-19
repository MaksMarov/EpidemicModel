import pygame

import core.groups as groups

import data.settings.default as cfg


def create_borders():
    Border([cfg.BORDER_OFFSET, cfg.BORDER_OFFSET, cfg.SIM_WINDOW_WIDTH - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS, cfg.BORDER_OFFSET])
    Border([cfg.BORDER_OFFSET, cfg.SIM_WINDOW_HEIGHT - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS, cfg.SIM_WINDOW_WIDTH - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS, cfg.SIM_WINDOW_HEIGHT - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS])
    Border([cfg.SIM_WINDOW_WIDTH - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS, cfg.BORDER_OFFSET, cfg.SIM_WINDOW_WIDTH - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS, cfg.SIM_WINDOW_HEIGHT - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS])
    Border([cfg.BORDER_OFFSET, cfg.BORDER_OFFSET, cfg.BORDER_OFFSET, cfg.SIM_WINDOW_HEIGHT - cfg.BORDER_OFFSET - cfg.BORDER_THICKNESS])

def get_len_or_default(first_point, second_point, default = cfg.BORDER_THICKNESS):
    if first_point != second_point:
        return second_point - first_point
    else:
        return default       

class Border(pygame.sprite.Sprite):
    def __init__(self, cords):
        super().__init__(groups.borders_group)
        self.create_border(cords)
        if cords[0] == cords[2]:
            self.add(groups.vertical_borders_group)
        else:
            self.add(groups.horizontal_borders_group)

    def create_border(self, cords):
        self.image = pygame.Surface([get_len_or_default(cords[0], cords[2]), get_len_or_default(cords[1], cords[3])])
        self.color = pygame.Color(cfg.BORDER_COLOR)
        self.rect = pygame.Rect(cords[0], cords[1], get_len_or_default(cords[0], cords[2]), get_len_or_default(cords[1], cords[3]))