a = 78
print("Здравствуйте, как вас зовут?")
b = input()
print(f"очень приятно, {b}! Меня зовут Марк")
print("Сколько вам лет?")
c = int(input())
if a > c:
    print(f"Да, {b}, я старше вас на {(a-c)} лет")
else:
    print(f"Да, {b}, я младше вас на {(c-a)} лет")
print("вам нравится программировать?")
d = input()
if d == "да":
    print("Превосходно! У вас получится написать много хороших программ")
else:
    print("А жаль((")