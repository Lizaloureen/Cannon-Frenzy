import random

import pygame

from constants import *
from sprites import Target


class Level:
    def __init__(self, screen, level_number, num_targets, target_size, cannonballs_left):
        self.screen = screen
        self.level_number = level_number
        self.num_targets = num_targets
        self.target_size = target_size
        self.cannonballs_left = cannonballs_left
        self.targets = self.generate_targets()

    def generate_targets(self):
        targets = []
        for _ in range(self.num_targets):
            overlap = True
            while overlap:
                overlap = False
                x = random.randint(400, SCREEN_WIDTH - 50)
                y = random.randint(200, 400)
                new_target = Target(self.screen, x, y, self.target_size, self.target_size)
                for target in targets:
                    if target.rect.colliderect(new_target.rect):
                        overlap = True
                        break
                if not overlap:
                    targets.append(new_target)
                    break

        return targets

    def draw(self):
        for target in self.targets:
            target.draw()

    def update(self):
        # TODO: Add level-specific updates
        pass
