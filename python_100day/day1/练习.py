
import random
# import turtle
# turtle.pensize(4)
# turtle.pencolor('red')
#
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
#
# turtle.mainloop()

all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = ''
last_pos = len(all_chars) - 1
index = random.randint(0, last_pos)
print(all_chars)
print(last_pos)
print(index)
print(all_chars[index])
code += all_chars[index]
print(code+'s')