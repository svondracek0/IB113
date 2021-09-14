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
