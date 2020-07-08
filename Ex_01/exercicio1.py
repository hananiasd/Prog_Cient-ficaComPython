from math import tan, cos, radians

x = 0.5
y0 = 1
v0 = 15
theta = 60
g = 9.81

v0 = v0 * 0.277778       #Converte km/h para m/s
theta = radians(theta)   #Converte graus para radianos

y = x*tan(theta) - 1/(2*v0) * g*x**2/((cos(theta))**2) + y0

print(y)