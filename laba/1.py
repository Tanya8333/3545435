'''for i in range(1,21):
    print(i, end = ' ')'''


'''a=int(input())
for i in range(1,11):
    print(f'{a} * {i} = {a *i}')'''


'''a = int(input())
total = 0
for i in range(1, a+1):
    total+=i
print(total)'''

'''tak = str(input())
b = 0
for i in tak:
    if i == 'a' or i =='A':
        b +=1
print(b)'''

'''a = int(input())
b = '*'
for i in range(1,a + 1):
    print(f'{b*i}')'''

'''a = int(input())
b = 1
for i in range(1, a + 1):
    b *=i
print(b)
'''

'''a = input()
for i in range (len(a) -1, -1, -1):
    print(a [i], end='')'''


'''n = int(input())
if n >=2:
    for i in range(2, n+1, 2):
        if n % 2 ==0:
            print(i,end= ' ') '''    

'''count = int(input())
i = 0
total = 0
while i < count:
    n = int(input())
    total+=1
    i += 1
print('Колличество оценок:', count)
print('Среднее значение', total/count)'''

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    print("Это не квадратное уравнение")
else:
    D = b**2 - 4*a*c
    if D < 0:
        print("Действительных корней нет")
    elif D == 0:
        x = -b / (2*a)
        print(f"x = {round(x, 2)}")
    else:
        x1 = (-b - D**0.5) / (2*a)
        x2 = (-b + D**0.5) / (2*a)
        if x1 > x2:
            print(f"x1 = {round(x2, 2)}, x2 = {round(x1, 2)}")

c2, c3, c4, c5 = 0, 0, 0, 0
total = 0
while True:
    grade = int(input())
    if grade == 0:
        break
    if grade < 2 or grade > 5:
        print("Неверная оценка")
        continue
    total += 1
    if grade == 2:
        c2 += 1
    elif grade == 3:
        c3 += 1
    elif grade == 4:
        c4 += 1
    elif grade == 5:
        c5 += 1
if total == 0:
    print("Оценок не было")
else:
    print(f"Двоек: {c2}\nТроек: {c3}\nЧетвёрок: {c4}\nПятёрок: {c5}\nПроцент пятёрок: {round(c5 / total * 100, 2)}%")

''''''
n = int(input())
original_n = n
count = 0
sum_digits = 0
reversed_n = 0
while n > 0:
    digit = n % 10
    print(digit)
    count += 1
    print(count)
    sum_digits += digit
    print(sum_digits)
    reversed_n = reversed_n * 10 + digit
    print(reversed_n)
    n = n // 10
    print(n)
print(f'n: {original_n}\nЦифр: {count}\nСумма цифр: {sum_digits}\nНаоборот: {reversed_n}')
if original_n == reversed_n:
    print("Палиндром: да")
else:
    print("Палиндром: нет")
'''

'''n = int(input("n: "))
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()
'''
'''
n = int(input("n: "))
pairs_count = 0
for p in range(2, n - 1):
    is_p_prime = True
    for d in range(2, int(p**0.5) + 1):
        if p % d == 0:
            is_p_prime = False
            break
    q = p + 2
    is_q_prime = True
    for d in range(2, int(q**0.5) + 1):
        if q % d == 0:
            is_q_prime = False
            break
    if is_p_prime and is_q_prime:
        print((p, q))
        pairs_count += 1
print(f"Пар: {pairs_count}")


text = input("Числа: ") #1 2 3 4 5
numbers = []
for s in text.split():   #[1], [2], [3], [4], [5]
    numbers.append(int(s))

total = sum(numbers)
avg = total / len(numbers)
print(f"Сумма: {total}")
print(f"Среднее: {round(avg, 2)}")

above_avg = []
for x in numbers:
    if x > avg:
        above_avg.append(x)
print(f"Больше среднего: {above_avg}")

max_index = numbers.index(max(numbers))
print(f"Индекс максимума: {max_index}")
print(f"Наоборот: {numbers[::-1]}")





