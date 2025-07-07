

class Animals(object):
    def run(self):
        print("Animals can run")


class Dog(Animals):
    def run(self):
        print('Dog can run')

    def cry(self):
        print("汪汪汪")

class Cat(Animals):
    def cry(self):
        print("喵喵喵")
if __name__ == '__main__':

    Dog().run()
    Dog().cry()
    Cat().run()
    Cat().cry()