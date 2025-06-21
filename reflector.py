import pygame

class Reflector:
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, signal):
        # Reflect the signal (convert position to letter, map through wiring, return position)
        letter = self.right[signal]  # Find the letter in the reflector's wiring
        reflected_signal = self.left.find(letter)  # Get the position of the reflected letter
        return reflected_signal 

    def draw(self , screen ,x,y,w,h,font): 

        #rectangle 
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen,"white",r,width=2, border_radius=15  )
    
        #letters 
        for i in range(26):
           

            #left hand side
            letter = self.left[i]                       
            letter = font.render(letter,True,"grey")
            text_box = letter.get_rect(center =(x+w/4,y+(i+1)*h/27))
            screen.blit(letter ,text_box)

       

            # right hand side
            letter = self.right[i]                       
            letter = font.render(letter,True,"grey")
            text_box = letter.get_rect(center =(x+w*3/4,y+(i+1)*h/27))
            screen.blit(letter ,text_box)
