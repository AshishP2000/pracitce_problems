class Father:
    fathername = ""

    def father(self):
        print(self.fathername)


class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)


class Son(Father, Mother):

    def parents(self):
        print("Father:", self.fathername)
        print("Mother:", self.mothername)


son = Son()

son.fathername = "Ishwar"
son.mothername = "Usha"

son.parents()
