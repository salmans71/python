def smartdiv(func):
    def inner(x,y):
        if x<y:
            x , y = y , x
        return func(x,y)
    return inner
@smartdiv
def div(a,b):
    print(a/b)
div(2,4)
