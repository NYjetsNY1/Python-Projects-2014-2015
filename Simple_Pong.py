# Ben Sklar
# Includes All Extensions
# Keeps Score, Has Game Over Mechanism
# Simple Game of Pong


from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 500)


class Flipper(games.Sprite):
    """ A "flipper" controlled by the mouse. """
    image = games.load_image("BMP.png")

    def __init__(self):
        """ Initialize Flipper object and create Text object for score. """
        super(Flipper, self).__init__(image = Flipper.image,
                                  x = games.mouse.x,
                                  y = 515
                                  )
        
        self.score = games.Text(value = 0, size = 50, color = color.white,
                                top = 5, right = games.screen.width - 10)
        
        games.screen.add(self.score)
 
    def update(self):
        """ Move to mouse position x only. """
        self.x = games.mouse.x

        # Keeps flipper on screen even if mouse is not.
        if self.left < 0:
            self.left = 0

        # Keeps flipper on screen even if mouse is not.
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_collide()

    def check_collide(self):
        """ Check for collision with ball. """
        for ball in self.overlapping_sprites:
            self.score.value += 1
            self.score.right = games.screen.width - 10 
            ball.ball_collide()


class Ball(games.Sprite):
    """ A ball. """
    image = games.load_image("ball.bmp")

    def __init__(self):
        """ Initialize a Ball object. """
        super(Ball, self).__init__(image = Ball.image,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    dx = 15,
                                    dy = 15)

    def ball_collide(self):
        """ Collide with the ball and move accordingly. """
        self.dy = -self.dy

        
    def update(self):
        """ Reverse a velocity component if edge of screen reached. """
        # Ignores the bottom of the screen. If the flipper does not collide, then it's over.
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        # If ball hits top, bounces off.
        if self.bottom > self.top < 0:
            self.dy = -self.dy

        # If ball hits bottom, game over.
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def ball_caught(self):
        """ Destroy self if caught. """
        self.destroy()

    def end_game(self):
        """ End the game. """
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 20,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        #games.screen.quit()


def main():
    # Creates background.
    wall_image = games.load_image("Gotham2.png", transparent = False)
    games.screen.background = wall_image

    # Creates flipper.
    the_flipper = Flipper()
    games.screen.add(the_flipper)

    # Creates the ball.
    the_ball = Ball()
    games.screen.add(the_ball)

    # Mouse should not be visable, but this actually is glitchy in python. Doesn't always work - python / windows error.
    games.mouse.is_visible = False

    # Mouse not locked on screen.
    games.screen.event_grab = False
    games.screen.mainloop()

# Main
main()
