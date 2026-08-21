import time

def color_profiler():
    # Banner Header
    print("=" * 55)
    print(" 🎨  A E S T H E T I C   C O L O R   P R O F I L E R  🎨 ")
    print("=" * 55)
    print("\nWelcome! Let's build your custom visual aesthetic profile.\n")

    # Question 1: Primary Color
    primary_color = input("➢ Enter your primary favorite color: ").strip().title()

    # Question 2: Accent Color Option
    add_accent = input("\n➢ Would you like to add a secondary accent color? (yes/no): ").strip().lower()
    
    accent_color = None
    if add_accent in ['yes', 'y']:
        accent_color = input("  ➔ Enter your secondary accent color: ").strip().title()

    # Question 3: Vibe Selection
    print("\n➢ Select your preferred visual vibe:")
    print("  [1] Dark & Mysterious ⚔️")
    print("  [2] Vibrant & Energetic ⚡")
    print("  [3] Calm & Minimalist 🌊")
    
    vibe_choice = input("  ➔ Choose your aesthetic number (1-3): ").strip()

    vibes = {
        "1": "Dark & Mysterious ⚔️",
        "2": "Vibrant & Energetic ⚡",
        "3": "Calm & Minimalist 🌊"
    }
    selected_vibe = vibes.get(vibe_choice, "Unique & Unconventional ✨")

    # Simulated Loading Effect
    print("\n" + "." * 55)
    print("Analyzing your color combo and generating profile...")
    time.sleep(1)
    print("." * 55 + "\n")

    # Output Results
    print("✨ YOUR AESTHETIC PROFILE RESULT ✨")
    print("—" * 40)
    print(f"❖ Primary Color  : {primary_color}")
    
    if accent_color:
        print(f"❖ Accent Color   : {accent_color}")
        print(f"❖ Perfect Palette : {primary_color} × {accent_color}")
    else:
        print(f"❖ Signature Mode : Pure {primary_color}")
        
    print(f"❖ Visual Aura    : {selected_vibe}")
    print('T I chose it.🧠 🤍Its one of the most $beautiful colors ever🤍')
    print("—" * 40)
    print("\nThank you for running the profiler! Share your results. 🚀")

if __name__ == "__main__":
    color_profiler()
