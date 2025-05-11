with open("words.txt", "rb+") as f:

    f.seek(18)
    print(f.read(5).decode("ascii"))
