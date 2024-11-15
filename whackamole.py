import pygame
import random

# make a comment
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        row = 0
        col = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    row_position = event.pos[0]//32
                    col_position = event.pos[1]//32
                    if row_position == row and col_position == col:
                        row = random.randrange(0, 20)
                        col = random.randrange(0, 16)
                    print(event.pos)
            screen.fill("light green")
            for i in range(1, 20):
                pygame.draw.line(screen,"black",(i*32, 0),(i*32, 512))
            for i in range(1, 20):
                pygame.draw.line(screen, "black", (0, i*32), (640,i*32))
            screen.blit(mole_image, mole_image.get_rect(topleft = (row*32, col*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
