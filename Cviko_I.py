# Cviko I/ Zaklady

print("Hello World")


#
def fn_class(x):
    if x == 0:
        print("x je 0")
    elif x % 2 == 0: # == ma nejnizsi prioritu, neni potreba tolik zavorek
        print("x je sude")
    else:
        print("x je liche")


fn_class(2)

def fn_series(min = 1, max = 50):
    for i in range(min, max + 1):
        if i % 5 == 0:
            print(i, end = "")

fn_series(1, 50)


