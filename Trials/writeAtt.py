class Deneme:
    def __init__(self):
        self.a=1
        self.b=4

D=Deneme()

x="a"
print(getattr(D,x))