# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов
# класса Building total (по примеру класса Lemming из урока)
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию


# Посчитаем здания
class Buiding: # новый класс Building с атрибутом total
    total = 40
    pass

    def __init__(self):
        self.total = 'Building'

    def __str__(self):  # метод преобразовать объкт в строку и вывести его на экран
        return '{}'.format(self.total)


Building_total = Buiding()
for house in range(1, 41):  # последовательность чего либо от и до
    print('{}'.format(house)) # что бы был виден номер дня нужны {} !!!
    print(Building_total)




