def quizzbit():
    print("Welcome to enrollment checker!")
    while True:
        begin = input("Please choose your name: ")
        if begin == "Freddy":
            print("you are enrolled in  History 101")
        elif begin == "Cher":
            print("you are enrolled in GETAJOB")
        elif begin == "Joseph":
            print('you are enrolled in MATH')
        else:
            print("please pick a enrolled student")
            print("Freddy,Cher,Joseph")
            continue
        break


