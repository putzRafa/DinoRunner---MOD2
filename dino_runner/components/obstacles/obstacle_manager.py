import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import EXPLODE
from dino_runner.utils.constants import DEATH_SOUND

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death_sound = DEATH_SOUND
        self.death_sound.set_volume(0.4)

    def update(self, game):
        obstacle_type = [Cactus(), Bird()]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.death_sound.play()
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)
                    self.display_explosion(game.screen, obstacle.rect.center, game)  # Exibe a explosão apenas quando o poder está ativado

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def display_explosion(self, screen, position, game):
        if game.player.has_power_up:  # Verifica se o jogador tem o poder ativado
            screen.blit(EXPLODE, position)
            pygame.display.flip()
            pygame.time.delay(100)
