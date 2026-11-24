import os

text = "Unforgettable"
try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
except OSError:
    pass
print(text)








