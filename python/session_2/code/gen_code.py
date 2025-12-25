def password_generator(length):

    """ This Function Generates a random password of given length entered by user
    ."""

    import random
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(length))
    return f"Generated password: {password}"