import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

global flag
flag = True

# HUD functions
def draw_player_health(surf, x, y):
    BAR_LENGTH = 890
    BAR_HEIGHT = 50
    fill =  BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    col = BLACK
    
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)
    lvl_obj=pg.font.Font("C:\Windows\Fonts\segoeprb.ttf",25)
    inv_obj=pg.font.Font("C:\Windows\Fonts\segoeprb.ttf",20)
    # Render the objects
    if KEY['level'] == 1 : 
        lvl = "Level : 1"
        rk = "Red Key  : " + str(KEY['key_red'])
        bk = "Blue Key : " + str(KEY['key_blue'])
        gk = "Green Key  : " + str(KEY['key_green'])
        yk = "Yellow Key : " + str(KEY['key_yello'])
        fi = "Fire Immunity    : "  + str(KEY['fire'])
        wi = "Water Immunity : "  + str(KEY['water'])
        cc = "Chips Collected   : "  + str(KEY['chip'])
        cr = "Chips Remaining : " + str(TOTAL_CHIP-KEY['chip'])
    elif KEY['level'] == 2 : 
        lvl = "Level : 2"
        rk = "Red Key  : "  + str(KEY['key_red'])
        bk = "Blue Key : " + str(KEY['key_blue'])
        gk = "Green Key  : " + str(KEY['key_green'])
        yk = "Yellow Key : " + str(KEY['key_yello'])
        fi = "Fire Immunity    : "  + str(KEY['fire'])
        wi = "Water Immunity : "  + str(KEY['water'])
        cc = "Chips Collected   : "  + str(KEY['chip'])
        cr = "Chips Remaining : " + str(TOTAL_CHIP-KEY['chip'])
    elif KEY['level'] == 3 : 
        lvl = "Level : 3"
        rk = "Red Key  : " + str(KEY['key_red'])
        bk = "Blue Key : " + str(KEY['key_blue'])
        gk = "Green Key  : " + str(KEY['key_green'])
        yk = "Yellow Key : " + str(KEY['key_yello'])
        fi = "Fire Immunity    : "  + str(KEY['fire'])
        wi = "Water Immunity : "  + str(KEY['water'])
        cc = "Chips Collected   : "  + str(KEY['chip'])
        cr = "Chips Remaining : " + str(TOTAL_CHIP-KEY['chip'])
    # red keys
    red_obj=inv_obj.render(rk,True,RED)
    surf.blit(red_obj,(15,1))
    # blue keys
    blue_obj=inv_obj.render(bk,True,CYAN)
    surf.blit(blue_obj,(15,21))
    # green keys
    green_obj=inv_obj.render(gk,True,GREEN)
    surf.blit(green_obj,(170,1))
    # Yellow keys
    yello_obj=inv_obj.render(yk,True,YELLOW)
    surf.blit(yello_obj,(170,21))
    # FIRE imunity
    fi_obj=inv_obj.render(fi,True,ORANGE)
    surf.blit(fi_obj,(350,1))
    # WATER imunity
    wi_obj=inv_obj.render(wi,True,DARK_BLUE)
    surf.blit(wi_obj,(350,21))
    # Total chips
    cc_obj=inv_obj.render(cc,True,PURPLE)
    surf.blit(cc_obj,(650,1))
    # Chips collected
    cr_obj=inv_obj.render(cr,True,PURPLE)
    surf.blit(cr_obj,(650,21))
    # level number
    text_obj=lvl_obj.render(lvl,True,RED)
    surf.blit(text_obj,(900,5))

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data(KEY['level'])

    def load_data(self,level):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.player_life = 5
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
        self.gun_flashes = []
        for img in MUZZLE_FLASHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()



    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'map1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'zombie':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name in ['thief']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['weee']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_red']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_blue']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_green']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_yello']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_red']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_blue']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_green']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_yello']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['exit']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['exit_check']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['chip']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['fire']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['water']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['fire_im']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['water_im']:
                Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False

    def new_2(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'map2.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'zombie':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name in ['thief']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['weee']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_red']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_blue']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_green']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_yello']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_red']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_blue']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_green']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_yello']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['exit']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['exit_check']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['chip']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['fire']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['water']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['fire_im']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['water_im']:
                Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
    
    
    def new_3(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'map3.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'zombie':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name in ['key_red']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['thief']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['weee']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_blue']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_green']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['key_yello']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_red']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_blue']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_green']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['gate_yello']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['exit']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['exit_check']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['chip']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['fire']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['water']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['fire_im']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['water_im']:
                Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
    
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()


    
    def update(self):
        # update portion of the game loop
        global flag
        self.all_sprites.update()
        self.camera.update(self.player)
        # player hits items
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'exit':
                if KEY['level'] < 3:
                    KEY['level'] = KEY['level'] + 1
                    KEY['key_red'] = 0
                    KEY['key_blue'] = 0
                    KEY['key_green'] = 0
                    KEY['key_yello'] = 0
                    KEY['exit_status'] = True
                else:
                    self.quit()
            
            if hit.type == 'thief':
                KEY['key_red'] = 0
                KEY['key_blue'] = 0
                KEY['key_green'] = 0
                KEY['key_yello'] = 0
                KEY['fire'] = False
                KEY['water'] = False
                hit.kill()
                self.player.update_key(hit.type) 
            if hit.type == 'weee':
                self.player.pos += vec(30, 0).rotate(-self.player.rot) 
                self.player.update_key(hit.type) 
            if hit.type == 'chip':
                hit.kill()
                self.player.update_key(hit.type)
            if hit.type == 'key_red':
                hit.kill()
                self.player.update_key(hit.type)
            if hit.type == 'key_blue':
                hit.kill()
                self.player.update_key(hit.type)
            if hit.type == 'key_green':
                hit.kill()
                self.player.update_key(hit.type)
            if hit.type == 'key_yello':
                hit.kill()
                self.player.update_key(hit.type)
            if hit.type == 'fire_im':
                hit.kill()
                self.player.update_key(hit.type)
            if hit.type == 'fire':
                if (KEY['fire'] == True):
                    continue
                else:
                    self.quit()       
            if hit.type == 'water_im':
                hit.kill()
                self.player.update_key(hit.type)
            if hit.type == 'water':
                if (KEY['water'] == True):
                    continue
                else:
                    self.quit()
            if hit.type == 'gate_red':
                if KEY['key_red'] > 0 :
                    KEY['key_red'] -= 1
                    hit.kill()
                    self.player.update_key(hit.type)
                else:
                    if self.player.rot>45 and self.player.rot<135:
                        self.player.rot = 90
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>135 and self.player.rot<225:
                        self.player.rot = 180
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>225 and self.player.rot<315:
                        self.player.rot = 270
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    else:
                        self.player.rot = 0
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    self.player.update_key(hit.type)
            if hit.type == 'gate_blue':
                if KEY['key_blue'] > 0 :
                    KEY['key_blue'] -= 1
                    hit.kill()
                    self.player.update_key(hit.type)
                else:
                    if self.player.rot>45 and self.player.rot<135:
                        self.player.rot = 90
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>135 and self.player.rot<225:
                        self.player.rot = 180
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>225 and self.player.rot<315:
                        self.player.rot = 270
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    else:
                        self.player.rot = 0
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    self.player.update_key(hit.type)
            if hit.type == 'gate_green':
                if KEY['key_green'] > 0 :
                    KEY['key_green'] -= 1
                    hit.kill()
                    self.player.update_key(hit.type)
                else:
                    if self.player.rot>45 and self.player.rot<135:
                        self.player.rot = 90
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>135 and self.player.rot<225:
                        self.player.rot = 180
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>225 and self.player.rot<315:
                        self.player.rot = 270
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    else:
                        self.player.rot = 0
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    self.player.update_key(hit.type)
            if hit.type == 'gate_yello':
                if KEY['key_yello'] > 0 :
                    KEY['key_yello'] -= 1
                    hit.kill()
                    self.player.update_key(hit.type)
                else:
                    if self.player.rot>45 and self.player.rot<135:
                        self.player.rot = 90
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>135 and self.player.rot<225:
                        self.player.rot = 180
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>225 and self.player.rot<315:
                        self.player.rot = 270
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    else:
                        self.player.rot = 0
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    self.player.update_key(hit.type)
            '''TOTAL_CHIP'''      
            if hit.type == 'exit_check':
                if KEY['chip'] == TOTAL_CHIP  :
                    hit.kill()
                    self.player.update_key(hit.type)
                else:
                    if self.player.rot>45 and self.player.rot<135:
                        self.player.rot = 90
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>135 and self.player.rot<225:
                        self.player.rot = 180
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    elif self.player.rot>225 and self.player.rot<315:
                        self.player.rot = 270
                        self.player.pos += vec(20, 0).rotate(self.player.rot)
                    else:
                        self.player.rot = 0
                        self.player.pos -= vec(20, 0).rotate(self.player.rot)
                    self.player.update_key(hit.type)
        
        #print(KEY['level'],KEY['chip'],KEY['exit_status'])
        if KEY['level'] == 2 and KEY['chip'] == TOTAL_CHIP and KEY['exit_status'] == True:
            KEY['chip'] = 0
            KEY['exit_status'] = False
            self.new_2()
        elif KEY['level'] >2  and KEY['chip'] == TOTAL_CHIP and KEY['exit_status'] == True:
            print(KEY['level'])
            KEY['chip'] = 0
            KEY['exit_status'] = False
            self.new_3()
            
        # mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullets hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)

        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # HUD functions
        draw_player_health(self.screen, 5, 5)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
        g.new()
        g.run()
