s = input("Input a string:")
d=0
l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print(f"Letters:{l}")
print(f"Digits:{d}")