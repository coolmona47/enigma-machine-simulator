# enigma-machine-simulator
A Python implementation of the WWII Enigma encryption machine with Pygame visualization
# 🔐 Enigma Machine Simulator (WWII Cipher Emulator)

A fully functional Enigma Machine simulator built using **Python** and **Pygame**, replicating the encryption process of the famous World War II cipher machine.

This project allows users to interactively type letters, visualize the internal signal flow through the rotors, reflector, and plugboard — just like in the real Enigma Machine.

---

## 🚀 Features

- 🧠 Accurate rotor stepping logic  
- 🌀 Customizable rotors, reflectors, plugboard, and ring settings  
- 🎮 Real-time interactive interface using **Pygame**  
- 🌈 Signal path visualization with colors:
  - Green: Forward signal through rotors
  - Yellow: Reflection
  - Red: Return path

---

## 📂 Folder Structure

enigma-simulator/
│
├── main.py # Entry point for the simulator
├── enigma.py # Enigma machine class and logic
├── rotor.py # Rotor definitions and behavior
├── plugboard.py # Plugboard logic
├── reflector.py # Reflector logic
├── keyboard.py # Input-output lampboard logic
├── assets/ # Fonts and graphics
└── README.md # You're reading this!   

## 🛠️ Getting Started

### ✅ 1. Requirements

- Python 3.7 or above  
- [Pygame](https://www.pygame.org/wiki/GettingStarted)

### 💻 2. Install Python & Pygame (Windows/Linux/macOS)

If you're using **Sublime Text**, make sure your system Python is properly set up:

#### ➤ Check Python Version

Open terminal / command prompt:
bash

➤ Install Pygame
Now install Pygame via pip:

bash

pip install pygame
If using multiple Python versions, try:

bash

python3 -m pip install pygame
How to Run (in Sublime Text)
Open the main.py file in Sublime Text

Press Ctrl + B (or Cmd + B on Mac) to run the simulator

A new Pygame window will appear

Start typing letters (A–Z) on your keyboard — encrypted output lights up like the original machine

Inside main.py, you can customize the Enigma machine setup:

python

from enigma import Enigma
from rotor import Rotor_I, Rotor_II, Rotor_III
from reflector import Reflector_B
from plugboard import Plugboard

# Plugboard settings: swap letter pairs
plugboard = Plugboard(["AB", "CD", "EF"])

# Initialize Enigma with 3 rotors and reflector
enigma = Enigma(
    Reflector_B,
    Rotor_I, Rotor_II, Rotor_III,
    plugboard,
    key="CAT",       # Initial rotor positions
    rings=(1, 1, 1)  # Ring settings
)


Example Use
Input: HELLO

Output (lights shown): WZPBT

Internal: Each key press moves the rotors and encrypts differently.

🧠 Learning Outcomes
🔐 Cryptography fundamentals (substitution, permutation, key space)

🧩 How real Enigma encryption worked

💡 GUI programming in Python using Pygame

🧱 Object-oriented design and modular coding


## 🧑‍💻 Credits

Originally created by the YouTube channel [Coding Cassowary](https://youtu.be/sbm2dmkmqgQ?si=kpSg9b-j3QeLtvd5)  
Adapted and documented by [mohan kumar]  
Inspired by historical Enigma machine design and educational simulations.

MIT License. Feel free to use, modify, and learn!



