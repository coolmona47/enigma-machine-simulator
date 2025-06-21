import pygame
class Rotor:
    def __init__(self, wiring, notch):
        # Static alphabet as reference (left side)
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Rotor wiring (right side)
        self.right = wiring
        # Rotor notch (turnover position)
        self.notch = notch

    def forward(self, signal):
        # Forward signal translation (static to wiring)
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        # Backward signal translation (wiring to static)
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, n=1, forward=True):
        # Rotate rotor n steps forward or backward
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotate_to_letter(self, letter):
        # Rotate rotor to a specific letter
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def set_ring(self, n):
        # Adjust rotor mappings based on the ring setting
        self.rotate(n-1,forward=False)
    

        # Adjust the notch position relative to the new mapping
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch - n) % 26]




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
            
        #highlight top letter 
            if i == 0:
                pygame.draw.rect(screen,"teal",text_box ,border_radius =5 )

        #highlight turnover notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch,True, "#333333")
                pygame.draw.rect(screen, "white", text_box ,border_radius = 5)


            screen.blit(letter ,text_box)

            # right hand side
            letter = self.right[i]                       
            letter = font.render(letter,True,"grey")
            text_box = letter.get_rect(center =(x+w*3/4,y+(i+1)*h/27))
            screen.blit(letter ,text_box)


 