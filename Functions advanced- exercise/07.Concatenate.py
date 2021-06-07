def concatenate(*args):
    text = ""
    for (i) in args:
        text+=str(i)
    return text
print(concatenate("Soft", "Uni", "Is", "Great", "!"))