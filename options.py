# options.py
import pygame

white = (255, 255, 255)
gray = (40, 40, 40)

def run_options(screen, clock, font_title):
    running = True
    width, height = screen.get_size()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # on ferme complètement le jeu
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # on quitte l'écran d'options et on revient au menu
                    running = False

        screen.fill(white)
        txt = font_title.render("OPTIONS", True, white)
        rect = txt.get_rect(center=(width // 2, height // 2 - 40))
        screen.blit(txt, rect)

        info = font_title.render("ESC pour retour", True, white)
        info_rect = info.get_rect(center=(width // 2, height // 2 + 40))
        screen.blit(info, info_rect)

        pygame.display.flip()
        clock.tick(60)
