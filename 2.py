'''
#2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
Дужак Андрій 122Г
'''

import timeit #імпорт таймера
def amount(a): #рекурсія
    if a < 10:
        return a
    else:
        return a % 10 + amount(a//10)
def Digital_sqrt(a):
    if a < 10:
        return a
    else:
        return Digital_sqrt(amount(a))
y = int(input('введіть число під корінь : '))# введеня даних
print("Рекурсивний розв'язок:")
print(Digital_sqrt(y))
time1 = timeit.timeit(number = 10000)# таймер
print("Час розв'язкання методом рекурсії: ", time1)
def digit_sqrt(a):#ітерація
    digit = 0     #лічильник
    count = 0     #лічильник
    for i in range(len(a)):
        digit += int(a[i-1])
    if int(digit)>9:
        digit=str(digit)
        for j in range(len(digit)):
            count +=int(digit[j-1])
        return count
    else:
        return digit
x = input('введіть число під корінь : ')# введеня даних
print("Ітераційний розв'язок:")
print(digit_sqrt(x))
time2 = timeit.timeit(number=10000)# таймер
print("Час розв'язання методом ітерацій: ", time2)



'''
Для даної задачі кращим буде розвязання за допомогою рекурсії. Програма наочно і
компактно представляє обчисленне, працює швидше і викликає саму себе. Тобто
рекурсія буде кращим вибором для вирішення

'''





