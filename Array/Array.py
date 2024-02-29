car=["Shivam", "Mishra","Kolkata"]; 


car.append("kol")


car.remove("Kolkata")
print(car)

# unpacking array element if  unpacking element is less then values in array then gives valueError

x,*y=car
print(len(car))

print(x)


print(y)



tuuu=("apple","banana","cherry")

t=tuuu*20

print(t)
