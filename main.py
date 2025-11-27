import pygame
import sys
import subprocess

pygame.init()
pygame.mixer.init()

# fenetre
width, height = 800, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("tic-tac")

# ressources
background = pygame.image.load("./assets/tic_tac_toe.webp")
background = pygame.transform.scale(background, (width, height))

pygame.mixer.music.load("./assets/Vangelis-Conquest_of_paradise.mp3")
pygame.mixer.music.play(-1)

# couleurs
white = (255, 255, 255)
translucent_blue = (0, 80, 200, 180)
hover_blue = (0, 140, 255, 220)
shadow_color = (0, 0, 0)

# polices
try:
    font_title = pygame.font.Font("assets/Minecraft.ttf", 72)
    font_button = pygame.font.Font("assets/Minecraft.ttf", 36)
except:
    font_title = pygame.font.SysFont(None, 72)
    font_button = pygame.font.SysFont(None, 36)


class Button:
    def __init__(self, text, center_y, action):
        self.text = text
        self.center_y = center_y
        self.action = action
        self.width, self.height = 320, 90  # largeur, hauteur
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (width // 2, center_y)

    def draw(self, win, mouse_pos):
        is_hover = self.rect.collidepoint(mouse_pos)
        color = hover_blue if is_hover else translucent_blue

        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, (0, 0, self.width, self.height), border_radius=16)
        win.blit(button_surface, self.rect)

        # texte
        text_surf = font_button.render(self.text, True, white)
        text_rect = text_surf.get_rect(center=self.rect.center)

        # ombre
        shadow_surf = font_button.render(self.text, True, shadow_color)
        shadow_rect = shadow_surf.get_rect(center=(self.rect.centerx + 3, self.rect.centery + 3))

        win.blit(shadow_surf, shadow_rect)
        win.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# liste des boutons
buttons = [
    Button("Nouvelle partie", 260, "new"),
    Button("Options", 340, "options"),
    Button("Quitter", 420, "quit"),
]

running = True
clock = pygame.time.Clock()

# boucle pour la souris
while running:
    clock.tick(60)
    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    # titre
    title = font_title.render("tic-tac-toe", True, white)
    title_rect = title.get_rect(center=(width // 2, 120))

    shadow_title = font_title.render("Mon jeu", True, shadow_color)
    shadow_rect = shadow_title.get_rect(center=(width // 2 + 4, 120 + 4))

    screen.blit(shadow_title, shadow_rect)
    screen.blit(title, title_rect)

    # dessiner les boutons
    for btn in buttons:
        btn.draw(screen, mouse_pos)

    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # condition pour les boutons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for btn in buttons:
                if btn.is_clicked(event.pos):
                    pygame.time.delay(150)

                    # condition nouvelle partie
                    if btn.action == "new":
                        print("Nouvelle partie")
                        pygame.quit()
                        subprocess.run(["python", "new_game.py"])
                        sys.exit()

                    # condition options
                    elif btn.action == "options":
                        # TODO : ici on va supprimer tout les elements créée et utilisé pour le menu 
                        print("Options")
                        screen.fill("white")

                    # condition quitter
                    elif btn.action == "quit":
                        running = False

    # on lance le jeu
    pygame.display.flip()

# on arrête le jeu
pygame.quit()
