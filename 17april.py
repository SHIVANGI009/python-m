age=21
print(f"my age is {age}")

#call by value & call by reference
a=10
print(id(a))
b=a
print(id(b))
print(a)
print(b)
a=80
b=a
print("a: ",id(a),"b: ",id(b))
b=20
print(id(b),"a: ",id(a))
# operators
# symbols => operator 

# Arithmetic
# logical
# assignment
# comparison
# memberhsip
# bitiwise
# identity

a=5
b=2
c=6
d=2
e=4
f=7
g=9
h=a+b*c**d-e//f+g 
print(h)
#5+72-4//7+9
#5+72+9
#4//7=0
a=20
b=70
print(a==200 or b>a)
