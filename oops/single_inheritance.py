# Single inheritance
class Bird:
    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("swim faster")


class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def who_is_this(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
# peggy.who_is_this()
# peggy.swim()
# peggy.run()
