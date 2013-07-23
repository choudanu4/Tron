#Ultratron
import random, math
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
    def update(self):
        """Kills object if it hits edge of the screen"""

        if self.bottom > games.screen.height:
            self.die()
        if self.top < 0:
            self.die()
        if self.left < 0:
            self.die()
        if self.right > games.screen.width:
            self.die()
    def die(self):
        """destroy self"""
        self.destroy()

class Collider(Wrapper):
    """A Wrapper that can blow up with other stuffs"""
    def update(self):
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """Destroy self and leave explosion behind."""
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()

class Explosion(games.Animation):
    """Explosion animation. """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()
        
class Ship(Collider):
    """A moving tron-bot"""
    images = ["green_tron.bmp", "red_tron.bmp", "yellow_tron.bmp", "blue_tron.bmp"]
    sound = games.load_sound("thrust.wav")
    velocity_x = 0
    velocity_y = 0

    def __init__(self, game, player_number, x, y):
        """chooses ship color"""
        self.color = games.load_image(images[player_number])
        super(Ship, self).__init__(image = self.color, x = x, y = y)
        self.game = game

    def update(self):
        """Move tron around and invoke a light trail"""
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_UP):
            self.velocity_y = -1
            self.velocity_x = 0
        if games.keyboard.is_pressed(games.K_DOWN):
            self.velocity_y = 1
            self.velocity_x = 0
        if games.keyboard.is_pressed(games.K_LEFT):
            self.velocity_x = -1
            self.velocity_y = 0
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.velocity_x = 1
            self.velocity_y = 0
        self.dx = self.velocity_x
        self.dy = self.velocity_y

class Player(Ship):
    """each player's ship"""
    def __init__(self):
        super(Player, self).__init__(player_number)
        score = 0
        color = ""
        alive = True
        
class Game(object):
    """the game itself"""
    level = 0
    def _init__(self):
        """Initialize Game object. """
        # set level
        self.level = 0
        #load sound for level advance
        self.sound = games.load_sound("level.wav")
        for player in number_of_players:
            self.ship = Ship(game = self,
                             x = games.screen.width/2,
                             y = games.screen.height/2)
            games.screen.add(self.ship)

    def play(self):
        """Play the game."""
        #begin theme music
        games.music.load("theme.mid")
        games.music.play(-1)
        #advance to level 1
        self.advance()
        # start play
        games.screen.mainloop()

    def advance(self):
        """Advances to next round"""
        self.level += 1
        level_message = games.Message(value = "Round " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)
        if self.level > 1:
            self.sound.play()

    def end(self):
        """End the game"""
        end_message = something
        
def main():
    tron = Game()
    tron.play()

number_of_players = input("How many players?")
main()

    
