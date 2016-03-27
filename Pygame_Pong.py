# Ben Sklar
# Pygame Pong
# 2-person Pong.
# Keeps Score, Has Game Over Mechanism when a player reaches a score of 5.
# Orange flipper uses Up key or Down key to move up or down (Player 1).
# Blue flipper uses W key or S key to move up or down (Player 2).
# There is a bug in certain version's of Python that
# the refresh rate and FPS cause the ball (Stu's head) to go through the flipper
# and glitch up. There is nothing I can do about this.
# I tried to change the sprites, and do oher things, but ultimately this bug is because
# of Python and Pygame, and lack of refresh rate and low FPS.
# The ball can also get caught in a corner. This is another bug I cannot actually do anything about.
# I could make the game harder and more fun if I could improve the FPS
# rate and the speed of the dx/dy, but again I cannot do so with the current
# state of Pygame and the amount of "lag" and lack of refresh rate it has.


# Importing of necessary things.
from livewires import games, color
import random

# Initialize the game.
games.init(screen_width = 400, screen_height = 480, fps = 500)

class Flipper1(games.Sprite):
    """ An Orange "flipper" controlled by the Up and Down keys. """
    image = games.load_image("Flipper1.bmp")

    def __init__(self):
        """ Initialize right Flipper object and create a Text object for score. """
        super(Flipper1, self).__init__(image = Flipper1.image,
                                  x = 0,
                                  y = 240
                                  )
        self.score1 = games.Text(value = 0, size = 50, color = color.white,
                                top = 5, right = games.screen.width - 250)
        games.screen.add(self.score1)
 
    def update(self):
        """ Move up and down as the keyboard is pressed up and down. """
        if games.keyboard.is_pressed(games.K_s):
            if self.bottom < games.screen.height:
                self.y += 75
        
        if games.keyboard.is_pressed(games.K_w):
            if self.top > 0:
                self.y -= 75

        # Keeps flipper on screen.
        # More of a fail-safe. This is not 100% necessary since x begins at 0, but useful to have this code.
        if self.left < 0:
            self.left = 0
            
        self.check_collide()

    def check_collide(self):
        """ Check for collision with ball. """
        for ball in self.overlapping_sprites:
            ball.ball_collide()


class Flipper2(games.Sprite):
    """ A Blue "flipper" controlled by the W and S keys. """
    image = games.load_image("Flipper2.bmp")

    def __init__(self):
        """ Initialize left Flipper object and create a Text object for score. """
        super(Flipper2, self).__init__(image = Flipper2.image,
                                  x = games.screen.width,
                                  y = 240
                                  )
        self.score2 = games.Text(value = 0, size = 50, color = color.white,
                                top = 5, left = 250)
        games.screen.add(self.score2)

    def update(self):
        """ Move up with W key, move down with S key. """
        if games.keyboard.is_pressed(games.K_DOWN):
            if self.bottom < games.screen.height:
                self.y += 75
        
        if games.keyboard.is_pressed(games.K_UP):
            if self.top > 0:
                self.y -= 75

        # Keeps flipper on screen.
        # More of a fail-safe. This is not 100% necessary since x begins at the end of the screen-width, but useful to have this code.
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_collide()

    def check_collide(self):
        """ Check for collision with ball. """
        for ball in self.overlapping_sprites:
            ball.ball_collide()


class Ball(games.Sprite):
    """ A ball that is Stu's head. """
    image = games.load_image("the_one_and_only_professor_stu.bmp")

    def __init__(self, score1, score2):
        """ Initialize a Ball object that is Stu's head. """
        # The ball is initialized at a random y value between the range of 50-250.
        # This makes the game not exactly the same every time the ball is re-initialized.
        # Can add to the fun factor.
        super(Ball, self).__init__(image = Ball.image,
                                    x = games.screen.width/2,
                                    y = random.randrange(50, 251),
                                    dx = 10,
                                    dy = 10)
        self.score1 = score1
        self.score2 = score2

    def ball_collide(self):
        """ When a flipper collides with the ball, the ball bounces off and becomes faster. It won't get inordinately fast though. """
        self.dx = -self.dx
        # Ball increases speed after collision.
        self.dy = self.dy*1.2
        self.dx = self.dx*1.2
        # Caps the speed of the ball, so that it won't get faster than what Pygame can handle.
        if self.dy > 14:
            self.dy = 14
        if self.dx > 14:
            self.dx = 14


    def update(self):
        """ Instances on what to do when the ball goes past a Flipper or hits the top or bottom of the screen. """
        
        # Dependent on Flipper1.
        # This determines whether or not to  destroy the ball, and create a new one, or destroy the ball and end the game.
        # Game will end when player using Flipper1 hits the score of 5.
        if self.right > games.screen.width + 15:
            if self.score1.value == 4:
                self.end_game1()
                self.score1.value = 5
            elif self.score1.value < 5:
                self.score1.value += 1
                self.destroy()
                the_ball = Ball(self.score1, self.score2)
                games.screen.add(the_ball)


        # Dependent on Flipper2.
        # This determines whether or not to  destroy the ball, and create a new one, or destroy the ball and end the game.
        # Game will end when player using Flipper2 hits the score of 5.
        if self.left < -15:
            if self.score2.value == 4:
                self.end_game2()
                self.score2.value = 5
            elif self.score2.value < 5:
                self.score2.value += 1
                self.destroy()
                the_ball = Ball(self.score1, self.score2)
                games.screen.add(the_ball)

        # If ball hits the top of the screen, it bounces off.
        if self.bottom > self.top < 0:
            self.dy = -self.dy

        # If ball hits the bottom of the screen, it bounces off.
        if self.bottom > games.screen.height:
            self.dy = -self.dy


    # Function to destroy the ball.
    def ball_destroy(self):
        """ Destroy self. """
        self.destroy()

    def end_game1(self):
        """ End the game. """
        # If Flipper2 gets to 5 points, this is what occurs.
        # An end-message showing the correct winner will display, and the game will end and quit.
        end_message = games.Message(value = "Game Over - Blue wins",
                                    size = 40,
                                    color = color.green,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 15,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        #games.screen.quit()


    def end_game2(self):
        """ End the game. """
        # If Flipper1 gets to 5 points, this is what occurs.
        # An end-message showing the correct winner will display, and the game will end and quit.
        end_message = games.Message(value = "Game Over - Orange wins",
                                    size = 40,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 15,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        #games.screen.quit()


def main():
    # Creates Background.
    wall_image = games.load_image("Skyscrapers.png", transparent = False)
    games.screen.background = wall_image

    # Creates Flipper1.
    the_flipper1 = Flipper1()
    games.screen.add(the_flipper1)

    # Creates Flipper2.
    the_flipper2 = Flipper2()
    games.screen.add(the_flipper2)

    # Creates the ball.
    the_ball = Ball(the_flipper1.score1, the_flipper2.score2)
    games.screen.add(the_ball)

    # Mouse should not be visable, but this actually is glitchy in python. Doesn't always work - python / windows error.
    games.mouse.is_visible = False

    # Mouse not locked on the screen.
    games.screen.event_grab = False
    games.screen.mainloop()

# Main
main()

# Game will exit upon a player winning, or if of course you press the Escape key.
