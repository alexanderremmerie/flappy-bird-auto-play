#!/usr/bin/env python
import pygame
import random

class FlappyBird:
    def __init__(self):

        # make a display
        self.screen = pygame.display.set_mode((800, 708))

        # make a bird
        self.bird = pygame.Rect(50, 50, 50, 50)

        # set the background
        self.background = pygame.image.load("assets/background.png").convert()

        # set the flappy bird sprites
        self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                            pygame.image.load("assets/2.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")]

        # set wallUp
        self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
        self.wallUp2 = pygame.image.load("assets/bottom.png").convert_alpha()

        # set wallDown
        self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
        self.wallDown2 = pygame.image.load("assets/top.png").convert_alpha()

        # set the gap
        self.gap = 140

        # set the distance to the wall
        self.wallx = 400
        self.wallx2 = 850

        # set the bird height
        self.birdY = 350

        # bird is not jumping
        self.jump = 0

        # set the jump speed
        self.jumpSpeed = 13

        # set gravity
        self.gravity = 3

        # bird is not dead
        self.dead = False

        # set current sprite
        self.sprite = 0

        # set current counter
        self.counter = 0

        # set first offset
        self.offset = random.randint(-110, 110)
        self.offset2 = random.randint(-110, 110)

         # distance to wall
        self.distance = 0

        # autoplay
        self.autoplay = True

    def updateWalls(self):
        self.wallx -= 2
        self.wallx2 -= 2
        if self.wallx < -90:
            self.wallx = 810
            self.counter += 1
            self.offset = random.randint(-110, 110)

        if self.wallx2 < -90:
            self.wallx2 = 810
            self.counter += 1
            self.offset2 = random.randint(-110, 110)

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY

        upRect2 = pygame.Rect(self.wallx2, 360 + self.gap - self.offset2 + 10, self.wallUp.get_width() - 10, self.wallUp.get_height())
        downRect2 = pygame.Rect(self.wallx2, 0 - self.gap - self.offset2 - 10, self.wallDown.get_width() - 10, self.wallDown.get_height())

        upRect = pygame.Rect(self.wallx, 360 + self.gap - self.offset + 10, self.wallUp.get_width() - 10, self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx, 0 - self.gap - self.offset - 10, self.wallDown.get_width() - 10, self.wallDown.get_height())

        if upRect.colliderect(self.bird):
            self.Dead()
        if downRect.colliderect(self.bird):
            self.Dead()
        if not 0 < self.bird[1] < 720:
            self.Dead()

        if upRect2.colliderect(self.bird):
                self.Dead()
        if downRect2.colliderect(self.bird):
                self.Dead()

        if self.wallx < self.wallx2:
            self.distance = self.wallx - 105

        else:
            self.distance = self.wallx2 - 105

    def Dead(self):
        if 0 == 0:
            print("dead")
            print(self.gap + self.offset + 10)
            print(708 - self.birdY)
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.wallx2 = 800
            self.offset = random.randint(-110, 110)
            self.gravity = 5

    def run(self):
        #initiate clock
        clock = pygame.time.Clock()

        #initiate font
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        font2 = pygame.font.SysFont("Arial", 30)
        #main lopp
        while True:

            #fps
            clock.tick(60)

            #look for user input
            for event in pygame.event.get():

                # see if quiting
                if event.type == pygame.QUIT:
                    sys.exit()

                # see keyboard or mouse input
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.jump = 17
                    self.gravity = 3
                    self.jumpSpeed = 13


            # game autoplay
            if self.autoplay:
                if self.wallx < self.wallx2:
                    if (708 - self.birdY) < (self.gap + self.offset + 120):

                        #jump
                        self.jump = 17
                        self.gravity = 3
                        self.jumpSpeed = 13
                else:
                    if (708 - self.birdY) < (self.gap + self.offset2 + 120):

                        # jump
                        self.jump = 17
                        self.gravity = 3
                        self.jumpSpeed = 13

            # fill in background color
            self.screen.fill((255, 255, 255))

            # display background
            self.screen.blit(self.background, (0, 0))

            # display wallUp
            self.screen.blit(self.wallUp, (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallUp2, (self.wallx2, 360 + self.gap - self.offset2))

            # display wallDown
            self.screen.blit(self.wallDown, (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(self.wallDown2, (self.wallx2, 0 - self.gap - self.offset2))

            # display current score
            self.screen.blit(font2.render(str("score: " + str(self.counter)), -1, (255, 255, 255)), (500, 10))

            # display current distance
            self.screen.blit(font2.render(str("distance to wall: " + str(self.distance)), -1, (255, 255, 255)), (500, 40))

            # display current offset

            if self.wallx < self.wallx2:
                self.screen.blit(font2.render(str("offset: " + str(self.offset)), -1, (255, 255, 255)), (500, 70))
            else:
                self.screen.blit(font2.render(str("offset: " + str(self.offset2)), -1, (255, 255, 255)), (500, 70))

            # display current birdy

            self.screen.blit(font2.render(str("bird position: " + str(int(708 - self.birdY))), -1,(255, 255, 255)), (500, 100))

            # display tower position

            self.screen.blit(font2.render(str("tower position: " + str(self.gap + self.offset + 100)), -1, (255, 255, 255)), (500, 130))

            # display autoplay

            if self.autoplay:
                self.screen.blit(font2.render("autoplay: ON", -1, (255, 255, 255)), (500, 160))
            else:
                self.screen.blit(font2.render("autoplay: OFF", -1, (255, 255, 255)), (500, 160))



            # set flappy bird sprite
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            if not self.dead:
                self.sprite = 0

            # update walls
            self.updateWalls()

            # update bird
            self.birdUpdate()

            # find information

            #display updates
            pygame.display.update()



if __name__ == "__main__":
     FlappyBird().run()
