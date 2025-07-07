class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

    def get_geade(self):
        if self.score >= 90:
            return "A"
        elif self.score>=60:
            return  "B"
        else:
            return  "C"


storm = Student('Storm Spirit',100)
# print(storm.name)
# print(storm.score)
# print(storm.name,storm.score)
storm.print_score()
print(storm.get_geade())
#print(storm.name)
