naam = "Mohammad Raja"  # String
umar = 28               # Integer
height = 5.9           # Float
is_learner = True      # Boolean

print(f"Mera naam {naam} hai aur main {umar} saal ka hoon.")
score = 85
if score > 50:
    print("Pass ho gaye!")
else:
    print("Phir se koshish karo.")
    # List (Multiple items)
skills = ["Python", "Data Analysis", "AI"]
print(skills[0])  # Output: Python

# Dictionary (Key-Value pair)
student = {"naam": "Mohammad Raja", "age": 28}
print(student["naam"])
for skill in skills:
    print(f"Main seekh raha hoon: {skill}")
def greet(name):
        return f"Hello, {name}!"

print(greet("Mohammad Raja"))