import random
import time

print("=== TOTALLY SAFE FUSION REACTOR v1.0 ===")
print("(Warranty void if you read this message)\n")

temperature = 0  # millions of degrees
excuses = [
    "The plasma is feeling shy today.",
    "A magnet had a bad day.",
    "Someone left the fridge open. The fridge is the sun.",
    "Have you tried turning the star off and on again?",
    "The deuterium and tritium are not on speaking terms.",
]

while temperature < 150:
    temperature += random.randint(10, 40)
    print(f"Heating plasma... {temperature} million degrees")
    time.sleep(0.5)
    if random.random() < 0.3:
        print("  WARNING:", random.choice(excuses))
        temperature -= 20
        time.sleep(0.5)

print("\nIGNITION!!! We made a tiny sun in a jar!")
time.sleep(1)
print("Energy produced: 0.0001 watts")
print("Energy spent to get here: your entire electricity bill")
print("Fusion is only 30 years away. (It has been 30 years away since 1955.)")
