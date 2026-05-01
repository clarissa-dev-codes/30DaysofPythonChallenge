age = 26
height = 5.4
complex_num = 32 + 68j

def triangle_area(base, height):
    return (base * height * 0.5)

def triangle_perimeter(sidea, sideb, sidec):
    return (sidea + sideb + sidec)

def rectangle_area(width, height):
    return (width * height)

def rectangle_perimeter(sidea, sideb):
    return (2 * (sidea + sideb))

def circle_area(radius):
    return (3.14 * radius ** 2)

def circle_perimeter(radius):
    return (2 * 3.14 * radius)

def calculate_y(x):
    return x**2 + 6*x + 9

def quad():
    for x in range (-10, 11):
        y = x**2 + 6*x + 9
        if y == 0:
            return x

user_base = int(input("Enter your base number: "))
user_height = int(input("Enter your height: "))
tri_area = triangle_area(user_base, user_height)
print (f"The area of the triangle is {tri_area}")

side_a = int(input("Enter side A: "))
side_b = int(input("Enter side B: "))
side_c = int(input("Enter side C: "))
tri_perimeter = triangle_perimeter(side_a, side_b, side_c)
print (f"The perimeter of the triangle is {tri_perimeter}")

user_width = int(input("Enter your width: "))
user_height = int(input("Enter your height: "))
rect_area = rectangle_area(user_width, user_height)
rect_perimeter = rectangle_perimeter(user_width, user_height)
print(f"The area of the rectangle is {rect_area}")
print(f"The perimeter of the rectangle is {rect_perimeter}")

user_radius = int(input("Enter your radius: "))
cir_area = circle_area(user_radius)
cir_perimeter = circle_perimeter(user_radius)
print(f"The area of the circle is {cir_area}")
print(f"The circumference of the circle is {cir_perimeter}")


x1, y1, x2, y2 = 2, 2, 6, 10
slope = (y2 - y1)/(x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

root = quad()
print(f"Slope: {slope}, Distance: {distance}, Root: {root}")


py_length = len('python')
dr_length = len('dragon')
print(py_length != dr_length)

print('on: ', ('on' in 'python') and ('on' in 'dragon'))
print('jargon: ', ('jargon' in 'I hope this course is not full of jargon'))

print('no on: ', ('on' not in 'python') and ('on' not in 'dragon'))

float_py = float(py_length)
string_py = str(float_py)

num = int(input("Please enter an int: "))
if (num % 2) == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

floor_div = 7//3
compare = int(2.7)
print(floor_div == compare)

print('10' == 10)

pi = int(float('9.8'))

print(pi == 10)

hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
print('Your weekly earning is ', (hours * rate))

years = int(input('Enter number of years you have lived: '))
life = years * 31556952
print(f'You have lived for {life} seconds.')

for n in range(1, 6):
    print(f"{n}\t1\t{n}\t{n**2}\t{n**3}")