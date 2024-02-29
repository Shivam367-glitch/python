x = 300

def myfunc():
  global y
  y=500
  x = 200
  print(x)

myfunc()

print(x)
print(y)