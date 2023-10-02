
def getBoolInput(prompt: str, default: bool = True) -> bool:
    while True:
        boolean = input(prompt + f"{'(Y/n)' if default else '(y/N)'} ")
        if boolean.lower() == "y":
            return True
        elif boolean.lower() == "n":
            return False
        elif boolean == "":
            return default
        else:
            print("Please enter in a valid option (y/n)")