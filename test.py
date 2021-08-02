# from random import randint

# for _ in range(6):
#     print(f'{randint(1, 30)}', end=' ')

# print()
def out():
    l = "local to out()"
    print(f"Original value ─ {l}")

    def inner():
        nonlocal l
        l = "nonlocal"
        print(f"Local to inner ─ {l}")

    inner()
    print(f"New value in out ─ {l}")

out()
