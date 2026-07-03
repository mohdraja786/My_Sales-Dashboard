# Yeh rahi meri seekhne wali cheezon ki list
my_skills = ["Python", "Data Analysis", "AI"]

# Ab main loop chala kar check karunga ki AI list mein hai ya nahi
for skill in my_skills:
    if skill == "AI":
        print("I am becoming an AI expert!")
    else:
        print(f"Abhi main {skill} seekh raha hoon.")
def check_skill(skill_name):
        if skill_name == "AI":
            return "I am becoming an AI expert!"
        else:
            return f"Abhi main {skill_name} seekh raha hoon."

# Ab hum is function ko call karenge
skills = ["Python", "Data Analysis", "AI"]

for s in skills:
    print(check_skill(s))