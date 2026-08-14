import car as c

c1 = c.Car()
m1 = c.Motorcycle(False)

c1.start()
c1.increase_speed(100)
print(c1.speed)

print(m1.started)
