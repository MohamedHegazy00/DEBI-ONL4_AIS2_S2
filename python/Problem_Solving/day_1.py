#Problem 1

def reverse_words(s):

    return " ".join(s.split(" ")[::-1])


text = "The greatest victory is that which requires no battle"
result = reverse_words(text)

print(result) 

#=============================================================================================================
#Problem 2

def play_banjo(name):

    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
name = input("Enter your name: ")
result = play_banjo(name)
print(result)
