x=3.3
print("x: ",x)
y=1.1 + 2.2
print("y: ", y)

print(x == y)

#comparar tipo string
y_str = format(y, ".2g")
print("str => ",y_str)
print(y_str == str(x))

#forma matematica

print(x,y)
tolerance = 0.001

print(abs(x-y)<tolerance)