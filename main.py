import pygame
from rotor import Rotor
from plugboard import Plugboard
from reflector import Reflector
from keyboard import Keyboard
from enigma import Enigma
from draw import draw

# Set up pygame 
pygame.init() 
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

# Create fonts
MONO = pygame.font.SysFont("freemono", 25)
BOLD = pygame.font.SysFont("freemono", 25, bold=True)

# Global variables    
WIDTH = 1600
HEIGHT = 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Initialize the display
MARGINS = {"top": 200, "bottom": 100, "left": 100, "right": 100}
GAP = 100
INPUT = ""
OUTPUT = ""
PATH = []

# Create Rotor instances with corrected wiring and notches
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")  # Rotor I
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")  # Rotor II
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")  # Rotor III
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")  # Rotor IV
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")  # Rotor V

# Create Reflector instances
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")  # Reflector A
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")  # Reflector B
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")  # Reflector C

# Create Keyboard and Plugboard instances 
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])
ENIGMA = Enigma(B, I, II, III, PB, KB)

# Set ring values
ENIGMA.set_rings((1, 1, 1))

# Set message key
ENIGMA.set_keys("CAT")

# Main loop
animating = True 
while animating:
    # Background color 
    SCREEN.fill("#333333") 

    # Render text input at the top-center
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center=(WIDTH / 2, MARGINS["top"] / 2))
    SCREEN.blit(text, text_box)
    
    # Render OUTPUT at the top-center as well (just below the input)
    text = MONO.render(OUTPUT, True, "white")  # White text
    text_box = text.get_rect(center=(WIDTH / 2, MARGINS["top"] / 2 + 25))  # Slightly below input
    SCREEN.blit(text, text_box)
    
    # Draw the Enigma machine (already implemented in your draw function)
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)
    
    # Update the screen  
    pygame.display.flip()

    # Track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                II.rotate()  # Rotate rotor
            elif event.key == pygame.K_SPACE:
                INPUT += " "
                OUTPUT += " "    
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()  # Convert letter to uppercase if needed
                    INPUT += letter  # Append the letter to the input
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT += cipher  # Output is the enciphered lette