def fileName():
    filename = input("Please enter .txt file: ")
    if filename.lower().endswith(".txt"):
        name_without_extension=filename[:-4]
        if name_without_extension.isnumeric():
            try:
                raise ValueError('Invalid Filename: Name is numeric.')
            except ValueError as error:
                print(error)
        else:
            try:
                with open(filename,"r") as f:
                    print(f.read())
            except FileNotFoundError:
                print("File not found. \nIf you're sure that the file exists, please provide it's path.\nFor example C:/User/Asrock/Desktop/baba.txt")
    else:
        print("Extension must be .txt")

fileName()