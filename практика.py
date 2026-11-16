'''a = int(input())
b = int(input())
c = int(input())

if a <= 0 or b <= 0 or c <= 0:
    print('Ошибка: стороны должны быть положительными')
elif a + b <= c or a + c <= b or b + c <= a:
    print('Такого треугольника не существует')
else:
    if a == b == c:
        t = 'Равносторонний'
    elif a == b or b == c or a == c:
        t = 'Равнобедренный'
    else:
        t = 'Разносторонний'

    s = sorted([a, b, c])
    if s[2] ** 2 == s[0] ** 2 + s[1] ** 2:
        print(f'{t}\nОн прямоугольный')
    else:
        print(t)'''

'''a = 0
b = 0
c = 0
d = 0

while True:
    x = int(input())
    if x == 0:
        break
    if a == 0 or x > d:
        d = x
    a += 1
    if x % 2 == 0:
        b += 1
    if x > 0:
        c += x

if a == 0:
    print('Чисел не было')
else:
    print(f'Всего введено: {a}\nЧетных: {b}\nСумма положительных: {c}\nНаибольшее: {d}')
'''

'''n = int(input())
s = 0
v = ''

for i in range(1, n + 1):
    for j in range(1, i + 1):
        v += str(j)
        s += j
    v += '\n'

print(f'{v}Сумма всех выведенных чисел: {s}')'''


'''nums = [12, -3, 7, 0, -8, 15, 4, -1, 9]

p = []
for x in nums:
    if x > 0:
        p.append(x)

sr = sum(p) / len(p)
d = sorted(nums)
c = nums.copy()

nums.insert(1, 100)
u = nums.pop()

print(f'Положительные: {p}\nСреднее: {sr:.2f}\nКопия по убыванию: {d}\nИсходный: {c}\nУдаленный элемент: {u}\nПолучившийся список: {nums}')
'''
'''def to_fahrenheit(c):
    return c * 9 / 5 + 32

def feeling(c):
    if c < 0:
        return 'мороз'
    elif c < 10:
        return 'холодно'
    elif c < 25:
        return 'тепло'
    else:
        return 'жарко'

n = int(input())
k = 0
z = ''

for i in range(1, n + 1):
    t = f(input())
    f = to_fahrenheit(t)
    s = feeling(t)
    z += f'День {i}: {t} C = {f:.1f} F, {s}\n'
    if s == 'жарко':
        k += 1

print(f'{z}Жарких дней: {k}')'''