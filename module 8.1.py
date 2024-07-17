def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError as exc:
        return (str(a)+str(b))
    else:
        return result

a_ = input('Введите значение: ')
b_ = input('Введите значение: ')

try:
    a = float(a_)
except:
    a = a_
try:
    b = float(b_)
except:
    b = b_
finally:
    print(add_everything_up(a, b))
    
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
