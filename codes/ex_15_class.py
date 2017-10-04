class X():
    def __init__(self,J):
        self.J = J
        print("__init__() in class X")
    def My_print_X(self):
        print(self.J)

# A = X(19)
# A.My_print_X()

class Y():
    def __init__(self,I):
        self.I = I
        print("__init__() in class Y")
    def My_print_Y(self):
        print(self.I)

# A = Y(19)
# A.My_print_Y()

class Z(X,Y):
    def __init__(self,J,I):
        self.J = J
        self.I = I
        X.__init__(self,J)
        Y.__init__(self,I)
        print("__init__() in class Z")

A = Z(19,1)
A.My_print_X()
A.My_print_Y()

class super_Z(X,Y):
    def __init__(self,J):
        super(super_Z,self).__init__(J)#真的不是很懂super的机制
        print("__init__() in class Z")

B = super_Z(5)
