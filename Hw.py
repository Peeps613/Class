print(int((1+1)**2/4))

x = "dogs"
y = "cats" 
var = "I am not {} of {}. but those {} those are the {}!".format("fond",y,x,"beastest")
print (var)

#num = 4 
#num/0 

#people who like brow puppos

var = input("do you like dogs? T/f:")


if var =="T":
    pupper = input("do you like brown dogs? T/F: ")
    if pupper == "T":
        print("woof Woof")
    else:
        print("lame")
else:  
    print("lame")

age =21

if age >18:
    print("adult")
else:
    print("kiddo")

counter = 0
while counter <= 3:
    print("no end in sight!")
    counter = counter + 1


for num in [1, 2, 3]:
    print("I love the number ",num)

def demo(x):
    y = x+3
    return y

q = demo(7)
#print(demo(q))