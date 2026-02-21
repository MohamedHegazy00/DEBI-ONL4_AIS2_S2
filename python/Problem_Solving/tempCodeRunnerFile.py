def play_banjo(name):

    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
name = input("Enter your name: ")
result = play_banjo(name)
print(result)