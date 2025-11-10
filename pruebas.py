def calculate_velocity(angle, gravity = 9.8 , distance = 15):
    from math import pi, sin, cos,sqrt

    angle = angle * pi / 180
    print(m)

    vi_perfecta = sqrt( (gravity * distance)/(2*cos(angle)*sin(angle)) )

    return vi_perfecta

m = 'Jalea'
a = int(input())
b = calculate_velocity(a)
print(b)

