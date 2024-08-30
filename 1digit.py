from machine import Pin
import time

# Configuration des broches GPIO pour chaque segment
segments = [
    Pin(13, Pin.OUT),  # Segment A
    Pin(12, Pin.OUT),  # Segment B
    Pin(14, Pin.OUT),  # Segment C
    Pin(27, Pin.OUT),  # Segment D
    Pin(26, Pin.OUT),  # Segment E
    Pin(25, Pin.OUT),  # Segment F
    Pin(33, Pin.OUT),  # Segment G
    Pin(32, Pin.OUT)   # Decimal Point (DP)
]

# Table de segments pour chaque chiffre de 0 à 9
digits = [
    [1, 1, 1, 1, 1, 1, 0, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1, 0],  # 2
    [1, 1, 1, 1, 0, 0, 1, 0],  # 3
    [0, 1, 1, 0, 0, 1, 1, 0],  # 4
    [1, 0, 1, 1, 0, 1, 1, 0],  # 5
    [1, 0, 1, 1, 1, 1, 1, 0],  # 6
    [1, 1, 1, 0, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1, 0],  # 8
    [1, 1, 1, 1, 0, 1, 1, 0],  # 9
    [1, 1, 1, 0, 1, 1, 1, 1]   # A.
]

# Fonction pour afficher un chiffre sur l'afficheur 7 segments
def display_digit(digit):
    for i in range(8):
        segments[i].value(digits[digit][i])

# Boucle principale pour afficher les chiffres de 0 à 9
while True:
    for digit in range(11):
        display_digit(digit)
        time.sleep(1)
