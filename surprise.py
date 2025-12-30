import time
import sys

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Surprise messages (English)
messages = [
    "💖 Surprise loading...",
    "🌸 Just one moment...",
    "✨ Something special for you...",
    "",
    "Dear ❤️",
    "Do you know?",
    "Your smile makes all my sadness disappear 😊",
    "Even your anger looks cute to me 😄",
    "I just want to make you smile, always 💕",
    "",
    "I care for you more than you know 💝",
    "Always yours ❤️",
    ""
]

for msg in messages:
    slow_print(msg, 0.04)
    time.sleep(0.7)

# Heart animation frames
hearts = [
"""
   **   **
 ****** ******
**************
 ************
  **********
    ******
      **
""",
"""
   **   **
 ****** ******
**************
 ************
  **********
    ******
""",
"""
   **   **
 ****** ******
**************
 ************
  **********
"""
]

print("\nSending you my heart...\n")
time.sleep(1)

for _ in range(3):
    for heart in hearts:
        print(heart)
        time.sleep(0.4)
        print("\033c", end="")  # clear screen (works in most terminals)

print("❤️ Love you forever ❤️")

