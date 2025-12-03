import random

slowa = {
    "1": "Trawa",
    "2": "drzwi",
    "3": "chleb",
    "4": "rybka",
    "5": "wiatr",
    "6": "kwiat",
    "7": "nocny",
    "8": "słoik",
    "9": "kotek",
    "10": "morze",
}

rand = random.randrange(1, 10)

chosen = slowa.get(f"{rand}")

sliced = []

for i in range(5):
    slicedi = chosen[f"{i}"]
    sliced.append(slicedi)
    print(f"{slicedi}")

print(f"{chosen}")