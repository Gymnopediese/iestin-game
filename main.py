import pygame, sys
from pygame.locals import QUIT
pygame.init()
display = pygame.display.set_mode((800, 800))
pygame.display.set_caption('parabola')

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((800, 800))


class PhysicObject:
    position = [0, 0]
    vitesse = [0, 0]
    acceleration = [0, 0]
    render = 1
    radius = 1
    sprite = None
    # initialise l'object
    def __init__(self, sprite_path, radius, pos_x, pos_y, speed_x=0.0, speed_y=0.0, acc_x=0.0, acc_y=1.0, render=1):
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.position = [pos_x, pos_y]
        self.vitesse = [speed_x, speed_y]
        self.acceleration = [acc_x, acc_y]
        self.render = render
        self.radius = radius

    # fait faire un pas à l'object phisique
    def step(self, screen):
        # ajoute la vitesse a la position
        self.position[0] += self.vitesse[0] / self.render
        self.position[1] += self.vitesse[1] / self.render

        # ajoute l'acceleration a la vitesse
        self.vitesse[0] += self.acceleration[0] / self.render
        self.vitesse[1] += self.acceleration[1] / self.render
        screen.blit(self.sprite, self.position)

    # put le sprite sur le screen
    def put_sprite(self, screen):
        pos = [self.position[0] - self.sprite.get_size()[0] / 2, self.position[1] - self.sprite.get_size()[1] / 2]
        screen.blit(self.sprite, pos)

    # fait faire un pas à l'object en respectant le sol, retourn true si le sol a ete touché
    def step_and_collid(self, screen, display = True, Y_FLOOR = 200):
        # ajoute la vitesse a la position
        self.position[0] += self.vitesse[0] / self.render
        self.vitesse[0] += self.acceleration[0] / self.render
        self.vitesse[0] /= 1.01
        if self.position[1] + self.vitesse[1] / self.render < Y_FLOOR:
            self.position[1] += self.vitesse[1] / self.render
            self.vitesse[1] += self.acceleration[1] / self.render
            self.vitesse[1] /= 1.01
            if display:
                self.put_sprite(screen)
            return False  # pas eu de collision avec le sol
        if display:
            self.put_sprite(screen)
        return True  # une colision

    def distance(self, object):
        return ((self.position[0] - object.position[0]) ** 2 + (self.position[1] - object.position[1]) ** 2) ** (1 / 2) - object.radius - self.radius

    def is_colliding(self, objects, exeption = None):
        if objects is None:
            return False
        for object in objects:
            if exeption != object and object != self and self.distance(object) < 0:
                return object
        return None

class Tank(PhysicObject):
    projectile = None
    hp = 100
    nom = ""
    pwr = 0

    def __init__(self, name, sprite_path, pos_x, pos_y, pwr):
        self.name = name
        self.pwr = pwr
        PhysicObject.__init__(self, sprite_path, 10, pos_x, pos_y, 0, 0, 0, 1, 10)
        self.projectile = None
        self.hp = 100


    def is_dead(self):
        return self.hp <= 0

    def shoot(self):
        self.projectile = PhysicObject(
            "projectilk.png",
            10,
            self.position[0],
            self.position[1],
            -(pygame.mouse.get_pos()[0] - self.position[0]) / 8,
            -(pygame.mouse.get_pos()[1] - self.position[1]) / 8,
            0,
            1,
            2,
        )

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("im dead")

    def step_shoot(self, screen, all_tanks):
        if self.projectile is not None:
            if self.projectile.step_and_collid(screen):
                self.projectile = None
                return True
            tank_ennemi = self.projectile.is_colliding(all_tanks, self)
            if tank_ennemi != None:
                self.projectile = None
                tank_ennemi.take_damage(self.pwr)
                return True
            return False




# use the principles of physics, espacialy projectil's physics to draw a parable
def draw_parabol(origin):
    # definit un PhysicObject pour le projectil
    projectile = PhysicObject(
        "projectilk.png",
        10,
        origin[0],
        origin[1],
        -(pygame.mouse.get_pos()[0] - origin[0]) / 8,
        -(pygame.mouse.get_pos()[1] - origin[1]) / 8,
        0,
        1,
        2,
    )
    # suivre ses 20 premiere trajectoir et y dessiné des point tant que le sol n'est pas touché
    for i in range(20):
        # dessione un cerle a la trajectoire
        pygame.draw.circle(surface, (255, 0, 0), projectile.position, 1)
        if projectile.step_and_collid(display, False):
            break


import time
def main():
    tank = Tank("mouton", "mouton.png", 100, 100, 100)
    tank2 = Tank("mouton2", "mouton2.jpg", 300, 100, 100)
    all_player = [tank, tank2]
    current_player = 0
    player_time = time.time()
    print(time.time())
    print(time.time())
    print(time.time())
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # event pour le test peu etre changé
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    if all_player[current_player].position[1] >= 199:
                        all_player[current_player].vitesse[1] = -10
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    all_player[current_player].vitesse[0] = -10
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    all_player[current_player].vitesse[0] = 10
                if keys[pygame.K_e]:
                    all_player[current_player].shoot()

        # clean le canvas
        surface.fill((0, 0, 0))
        # dessine le sol
        pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(0, 200, 400, 100))
        # dessine la ligne
        pygame.draw.line(surface, (255, 255, 0), all_player[current_player].position,
                         pygame.mouse.get_pos())

        # dessine la parabole
        draw_parabol(all_player[current_player].position)
        # fait prendre un step au tank
        for player in all_player:
            player.step_and_collid(display)
        if all_player[current_player].step_shoot(display, all_player):
            current_player = (current_player + 1) % 2
            player_time = time.time()

        if time.time() - player_time >= 10:
            current_player = (current_player + 1) % 2
            player_time = time.time()
        pygame.display.update()



if __name__ == '__main__':
    main()
