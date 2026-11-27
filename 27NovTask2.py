def get_name():
    name = input("Enter your name:")
    return name

def get_test_mark():
    thisMark = int(input("Enter test mark (0-100):"))
    while thisMark < 0 or thisMark > 100:
        print("Error")
        mark = int(input("Enter test mark (0-100):"))
    return mark

def display_all(aName, aMark):
    for index in range(5):
        print(aName[index] + " scored " + str(aMark[index]))



name = []
mark = []
for index in range(5):
    name.append(get_name())
    mark.append(get_test_mark())
display_all(name, mark)
