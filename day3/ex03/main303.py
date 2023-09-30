from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
print(v1 + 5)
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
print(v2 * 5)
print("---")
v3 = calculator([10.0, 15.0, 20.0])
print(v3 - 5)
print(v3 / 5)
print("---")
try:
    v2 / 0
except ZeroDivisionError as e:
    print(e)
