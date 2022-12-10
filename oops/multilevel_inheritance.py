class GrandFather:

    def __init__(self,grandfather):
        self.grandfather = grandfather

class Father(GrandFather):

    def __init__(self,fathername,grandfather):
        self.fathername = fathername

        GrandFather.__init__(self,grandfather)

class Son(Father):

    def __init__(self,sonname,fathername,grandfather):
        self.sonname = sonname

        Father.__init__(self,fathername,grandfather)

    def print_name(self):
        print("Grandfather name:",self.grandfather)
        print("Father name:",self.fathername)
        print("Son name:",self.sonname)

son = Son("Ashish","Ishwar","Govind")

son.print_name()