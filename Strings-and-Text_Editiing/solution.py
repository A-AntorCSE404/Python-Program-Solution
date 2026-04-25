import pyperclip

S = input()
T = input()
C = input()

# Part A
print(S.upper())
print(S.lower())

clean = S.strip("#$@")
print(clean)

low_clean = clean.lower()

print(low_clean.startswith("get"))
print(low_clean.endswith("http/1.1"))

words = clean.split()
print("|".join(words))

# Part B
print(T.isupper())
print(T.islower())
print(T.isalpha())
print(T.isalnum())
print(T.isdecimal())
print(T.isspace())
print(T.istitle())

# Part C
print(ord(C))

# Part D
pyperclip.copy(clean)
print(pyperclip.paste())
