import pygame
import random as rnd

import core.groups as groups
from core.virus import Virus
import core.model as model
from core.pawn_states import Pawn_state, Healthy, Dead, Infected

import data.settings.default as cfg

class Pawn(pygame.sprite.Sprite):
    def __init__(self, radius):
        super().__init__(groups.pawns_group)
        self.radius = radius
        self.position = self.create_random_position()
        self.speed = [rnd.randint(-cfg.PAWN_MAX_SPEED, cfg.PAWN_MAX_SPEED), rnd.randint(-cfg.PAWN_MAX_SPEED, cfg.PAWN_MAX_SPEED)]
        self.immunities = []
        self.immunity = model.cast_param(cfg.PAWN_MAX_START_IMMUNITY, 1)

        if model.calc_chanse(cfg.PAWN_SICK_ACCIDENTALLY):
            self.state = Infected(self.immunity, Virus())
        else:
            self.state = Healthy()

        self.create_pawn_sprite(self.state.color, self.position)

    def create_pawn_sprite(self, color, position):
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.rect = pygame.Rect(position[0], position[1], 2 * self.radius, 2 * self.radius)

    def create_random_position(self):
        offset = cfg.BORDER_OFFSET + cfg.BORDER_THICKNESS
        return [int(rnd.uniform(offset, cfg.SIM_WINDOW_WIDTH - offset)), int(rnd.uniform(offset, cfg.SIM_WINDOW_HEIGHT - offset))]

    def update(self):
        self.move()
        self.poll_overlapping_objects()
        self.state.progress()
        if self.state.is_healing:
            self.healing()
        if self.state.is_dead:
            self.dead()

    def poll_overlapping_objects(self):
        if pygame.sprite.spritecollideany(self, groups.borders_group): self.borders_react()
        
        if isinstance(self.state, Infected):
            collided_pawns = pygame.sprite.spritecollide(self, groups.pawns_group, False)
            for other in collided_pawns:
                if isinstance(other.state, Healthy):
                    self.try_infect(other)

    def borders_react(self):
            if pygame.sprite.spritecollideany(self, groups.vertical_borders_group):
                self.speed[0] *= -1
            if pygame.sprite.spritecollideany(self, groups.horizontal_borders_group):
                self.speed[1] *= -1

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    def try_infect(self, other):
        if self.can_infect(other):
            other.infect(self.virus)

    def can_infect(self, other):
        if not self.state.virus.stain in other.immunities:
            if model.calc_chanse(self.state.virus.contagiousness) and not model.calc_chanse(other.immunity):
                other.infect(self.state.virus)

    def infect(self, virus):
        self.state = Infected(self.immunity, virus)
        self.create_pawn_sprite(self.state.color, self.position)

    def healing(self):
        self.immunities.append(self.state.virus.stain)
        self.state = Healthy()
        self.create_pawn_sprite(self.state.color, self.position)

    def dead(self):
        self.state = Dead(self.state.virus)
        self.speed = [0, 0]
        self.create_pawn_sprite(self.state.color, self.position)