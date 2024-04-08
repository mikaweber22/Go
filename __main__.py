import pygame
import einstellungen

spiel_läuft = True

def main():
    # Pygame Starten
    print("starte Go")
    global spiel_läuft

    pygame.init()
    bildschirm = pygame.display.set_mode((einstellungen.BILDSCHIRM_BREITE, einstellungen.BILDSCHRIM_HÖHE))
    bildschirm.fill(einstellungen.BILDSCHIRM_FARBE)
    while spiel_läuft:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_läuft = False
    

if __name__ == "__main__":
    main()
pygame.quit()
quit() 