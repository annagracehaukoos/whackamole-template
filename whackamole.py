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
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
            screen.fill("light green")
            for i in range(1, 20):
                pygame.draw.line(screen,"black",(i*32, 0),(i*32, 512))
            for i in range(1, 20):
                pygame.draw.line(screen, "black", (0, i*32), (640,i*32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
