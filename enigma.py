class Enigma:
    def __init__(self, re, r1, r2, r3, pb, kb):
        self.re = re    # Reflector
        self.r1 = r1    # Rotor I
        self.r2 = r2    # Rotor II
        self.r3 = r3    # Rotor III
        self.pb = pb    # Plugboard
        self.kb = kb    # Keyboard

    def set_rings(self, rings):
        self.r1.set_ring(rings[0])
        self.r2.set_ring(rings[1])
        self.r3.set_ring(rings[2])

    def set_keys(self, key):
        self.r1.rotate_to_letter(key[0])
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])

    def encipher(self, letter):
        # Handle rotor stepping
        if self.r2.left[0] == self.r2.notch: 
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()

        # Pass the letter through the machine
        signal = self.kb.forward(letter)
        path = [signal, signal]
        signal = self.pb.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r1.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.re.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        # Backward pass through the rotors
        signal = self.r1.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.pb.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.kb.backward(signal)
        return path, letter