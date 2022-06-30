import pygame,sys
# Source : https://stackoverflow.com/questions/70297648/basic-camera-system-for-my-pygame-platformer
# Classes
class Game():
    def __init__(self):
        self.level = Level(screen)
        self.status = 'level'

    def run(self):
        if self.status == 'level':
            self.level.run()

class Level:
    def __init__(self,display_surface):
        # Basic setup
        self.setup_level()
        self.display_surface = display_surface

        # Movement
        self.x_shift = 0
        self.y_shift = 0

    def setup_level(self):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(level_data):
            for col_index,col in enumerate(row):
                x = col_index * tile_size
                y = (row_index * tile_size)# - ((len(level_data) - fov) * tile_size)
                if col == 'X':
                    tile = Tile((x,y))
                    self.tiles.add(tile)
                if col == 'P':
                    player = Player((x,y))
                    self.player.add(player)

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                player.direction.y = 0

        if player.on_ground and player.direction.y > 1 or player.direction.y < 0:
            player.on_ground = False

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right

    def run(self):
        self.vertical_movement_collision()
        self.horizontal_movement_collision()

        # Tiles
        self.tiles.update(self.x_shift, self.y_shift)
        self.player.update()
        
        map_left   = 0
        map_right  = len(level_data[0])*tile_size
        map_top    = 0
        map_bottom = len(level_data)*tile_size
        
        camera_x = -self.player.sprite.rect.centerx + self.display_surface.get_rect().centerx
        
        if self.player.sprite.rect.centerx < map_left + self.display_surface.get_rect().centerx:
            camera_x = -map_left
        if self.player.sprite.rect.centerx > map_right - self.display_surface.get_rect().centerx:
            camera_x = -(map_right - self.display_surface.get_rect().width)

        camera_y = -self.player.sprite.rect.centery + self.display_surface.get_rect().centery

        if self.player.sprite.rect.centery < map_top + self.display_surface.get_rect().centery:
            camera_y = -map_top
        if self.player.sprite.rect.centery > map_bottom - self.display_surface.get_rect().centery:
            camera_y = -(map_bottom - self.display_surface.get_rect().height)
        
        camera = (camera_x, camera_y) 
        
        for item in self.tiles:
            item.draw(self.display_surface, camera)

        self.player.sprite.draw(self.display_surface, camera)

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((tile_size,tile_size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self, x_shift, y_shift):
        self.x += x_shift
        self.y -= y_shift
        self.rect.topleft = round(self.x), round(self.y)

    def draw(self, screen, camera):
        screen.blit(self.image, self.rect.move(camera))
    
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        # Image
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        # Movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -20

        # Status
        self.on_ground = False

    def get_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jump()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.on_ground:
            self.direction.y = self.jump_speed

    def update(self):
        self.get_inputs()

    def draw(self, screen, camera):
        screen.blit(self.image, self.rect.move(camera))

# --- main ---

pygame.init()

# Settings
tile_size = 64
fov = 12
screen_width = 1200
screen_height = tile_size * fov

level_data = [
'                       ',
'                  XX   ',
'XX    XXX              ',
'                       ',
'                  XX   ',
'XX    XXX              ',
'                       ',
'                  XX   ',
'XX    XXX              ',
'XX                   XX',
'XXXX        XX         ',
'XXXX  P   XX           ',
'XX    X  XXX    XX  X  ',
'      X  XXX    XX  XX ',
'   XXXX  XXXXX  XX  XXX',
'XXXXXXX  XXXXX  XX  XXX']


# Game setup
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
game = Game()

# Main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)