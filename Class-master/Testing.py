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

#Student information
students = {"student":
[
    {"name": "Freddy",
    "grade": "12"}, 
    {"name": "Cher",
    "grade": "12"}, 
    {"name": "Joseph",
    "grade": "12"}
]}
#Class information 
classes = {"courses":
    [
        {"subject":"Math",
        "size": 27,
        "teacher": "bob",
        "block": 1 },
        {"subject":"Math",
        "size": 27,
        "teacher": "bob",
        "block": 1 },
        {"subject":"Math",
        "size": 27,
        "teacher": "bob",
        "block": 1 },
        {"subject":"Math",
        "size": 27,
        "teacher": "bob",
        "block": 1 },
        {"subject":"Math",
        "size": 27,
        "teacher": "bob",
        "block": 1 }
    ]}

# Here is the functioning code that requests the students information and classes

input("Hello student [] which classes would you like for this semester?")


#Here is the output to the Teachers attendance and schedule

#bla bla bla bla bla bla bla 

print(classes.get("courses")[0])

