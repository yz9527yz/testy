def Test():
    pass


try:
    test = Test()
    name = test.name  # not sure if we can get its name
except AttributeError:
    name = 'default'