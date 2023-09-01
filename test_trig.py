import costom_trig as trig

# test at x = 0
x = 0
print(f"cos(0) = {trig.cos(x)}")
print(f"sin(0) = {trig.sin(x)}")
print(f"tan(0) = {trig.tan(x)}")

#assert trig.sin(0) == 0.5, "sin(x) doesn't work"

# test at x = 90
x = 90
print(f"cos(90) = {trig.cos(x)}")
print(f"sin(90) = {trig.sin(x)}")
print(f"tan(90) = {trig.tan(x)}")