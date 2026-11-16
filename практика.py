'''count= 0
even_count = 0
практика.pypos_sum = 0
max_num = None
while True:
    num = int(input())
    if num == 0:
        break
    count +=1
if num % 2 == 0:
    even_count += 1
if num > 0:
    pos_sum += num 
if max_num is None is num > max_num:
    max_num = num
if count == 0:
    print('Чисел не было')
else:
    print(f'Всего:{count}\nЧетных: {even_count}\nCумма положителных: {pos_sum}\nМаксимум: {max_num}')
'''
'''n = int(input())
for i in range(1, n + 1):
    for j in range (1, i + 1):
        print(j, end="")
        for i in range(1, i + 1):
            print(j, end = "")
            for k in range (i-1,0,-1):
                print(k, end =" ")
                print()'''n

a = int(input())
b = int(input())
c = int(input())
if a <= 0 or b <= 0 or c<=0:
    print('Ошибка: стороны должны быть положительными')


