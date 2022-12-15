import math

user = 'True'
while user == 'True':
    e = input('Do you want to calculate for Trigonometric or Hyperbolic functions? (Enter: trig, hyper):')
    e = e.lower()
    if e == 'trig':
        print('Calculation of Trigonometric values..')
        a = input('Which Trignomentric value do you want to calculate? (Enter: sin, cos, tan, sec, cosec, cot):')
        a = a.lower()
        if a == 'sin':
            b = input("Would you like to enter the the angle's value in Degree or Radians? (Enter: deg, rad):")
            b = b.lower()
            if b == 'deg':
                c = float(input('Enter the value of the angle in degrees:'))
                d = math.radians(c)
                print('sin(', c, ')=', math.sin(d))
            else:
                c = float(input('Enter the value of the angle in radians:'))
                print('sin(', c, ')=', math.sin(c))
        elif a == 'cos':
            b = input("Would you like to enter the the angle's value in Degree or Radians? (Enter: deg, rad):")
            b = b.lower()
            if b == 'deg':
                c = float(input('Enter the value of the angle in degrees:'))
                d = math.radians(c)
                print('cos(', c, ')=', math.cos(d))
            else:
                c = float(input('Enter the value of the angle in radians:'))
                print('cos(', c, ')=', math.cos(c))
        elif a == 'tan':

            b = input("Would you like to enter the the angle's value in Degree or Radians? (Enter: deg, rad):")
            b = b.lower()
            if b == 'deg':
                c = float(input('Enter the value of the angle in degrees:'))
                d = math.radians(c)
                print('tan(', c, ')=', math.tan(d))
            else:
                c = float(input('Enter the value of the angle in radians:'))
                print('tan(', c, ')=', math.tan(c))
        elif a == 'sec':
            b = input("Would you like to enter the the angle's value in Degree or Radians? (Enter: deg, rad):")
            b = b.lower()
            if b == 'deg':
                c = float(input('Enter the value of the angle in degrees:'))
                d = math.radians(c)
                print('sec(', c, ')=', (math.sin(d) ** -1))
            else:
                c = float(input('Enter the value of the angle in radians:'))
                print('sec(', c, ')=', math.sin(c) ** -1)
        elif a == 'cosec':
            b = input("Would you like to enter the the angle's value in Degree or Radians? (Enter: deg, rad):")
            b = b.lower()
            if b == 'deg':
                c = float(input('Enter the value of the angle in degrees:'))
                d = math.radians(c)
                print('cosec(', c, ')=', (math.cos(d) ** -1))
            else:
                c = float(input('Enter the value of the angle in radians:'))
                print('cosec(', c, ')=', math.cos(c) ** -1)
        elif a == 'cot':
            b = input("Would you like to enter the the angle's value in Degree or Radians? (Enter: deg, rad):")
            b = b.lower()
            if b == 'deg':
                c = float(input('Enter the value of the angle in degrees:'))
                d = math.radians(c)
                print('cot(', c, ')=', (math.tan(d) ** -1))
            else:
                c = float(input('Enter the value of the angle in radians:'))
                print('cot(', c, ')=', math.tan(c) ** -1)
    elif e == 'hyper':
        print('Calculating Hyperbolic values...')
        a = input('Which Hyperbolic value do you want to calculate? (Enter: sinh, cosh, tanh, asinh, acosh, atanh):')
        a = a.lower()
        if a == 'sinh':
            b = float(input('Enter value to be calculated:'))
            print('sinh(', b, ')=', math.sinh(b))
        elif a == 'cosh':
            b = float(input('Enter value to be calculated:'))
            print('cosh(', b, ')=', math.cosh(b))
        elif a == 'tanh':
            b = float(input('Enter value to be calculated:'))
            print('tanh(', b, ')=', math.tanh(b))
        elif a == 'asinh':
            b = float(input('Enter value to be calculated:'))
            print('asinh(', b, ')=', math.asinh(b))
        elif a == 'acosh':
            b = float(input('Enter value to be calculated:'))
            print('acosh(', b, ')=', math.acosh(b))
        elif a == 'atanh':
            b = float(input('Enter value to be calculated:'))
            print('atanh(', b, ')=', math.atanh(b))
    else:
        print("Enter a valid value")
    i = input('Do you want to calculate for another value? (Enter: "yes" or "no"):')
    i = i.lower()
    if i == 'yes' or i == 'y':
        continue
    else:
        user = 'False'
