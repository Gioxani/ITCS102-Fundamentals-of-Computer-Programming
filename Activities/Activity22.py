
# LEVEL #4

Front_Kick = ["Basic Kick", "Beginner", "Leg"]
Roundhouse_Kick = ["Basic Kick", "Beginner", "Leg"]
Side_Kick = ["Basic Kick", "Intermediate", "Leg"]

Jab = ["Basic Punch", "Beginner", "Hand"]
Cross = ["Basic Punch", "Beginner", "Hand"]
Hook = ["Basic Punch", "Intermediate", "Hand"]

Low_Block = ["Defense", "Beginner", "Arm"]
High_Block = ["Defense", "Beginner", "Arm"]
Inside_Block = ["Defense", "Intermediate", "Arm"]

# LEVEL #3
# Taekwondo Techniques
Taekwondo = {
    "Front Kick": Front_Kick,
    "Roundhouse Kick": Roundhouse_Kick,
    "Side Kick": Side_Kick
}

# Boxing Techniques
Boxing = {
    "Jab": Jab,
    "Cross": Cross,
    "Hook": Hook
}

# Karate Techniques
Karate = {
    "Low Block": Low_Block,
    "High Block": High_Block,
    "Inside Block": Inside_Block
}

# LEVEL #2
# Martial Arts
Martial_Arts = {
    "Taekwondo": Taekwondo,
    "Boxing": Boxing,
    "Karate": Karate
}

# LEVEL #1
martial_arts = {
    "Martial Arts": Martial_Arts
}

print("=== 1. Going Down one level at a time ===")
print(martial_arts["Martial Arts"]["Taekwondo"]["Front Kick"][0])

print()
print("=== 2. Going Down two levels at a time ===")
for category in martial_arts:
    print(category)

print()
print("=== 3. Going Down three levels at a time ===")
for category, styles in martial_arts.items():
    print(category)
    for style in styles:
        print("  ", style)

print()
print("=== 4. Going Down four levels at a time ===")
for category, styles in martial_arts.items():
    print(category)
    for style, techniques in styles.items():
        print("  ", style)
        for technique, info in techniques.items():
            print("    ", technique)
            print("      ", info[0])
            print("      Level:", info[1])
            print("      Body Part:", info[2])

