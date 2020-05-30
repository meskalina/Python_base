from random import *


class HumanCard:
    def __init__(self):
        self.nums = sample(range(1, 91), 15)
        shuffle(self.nums)
        self.card = [sorted(self.nums[:5]), sorted(self.nums[5:10]), sorted(self.nums[10:15])]

    def __str__(self):
        return f'----- Ваша карточка ------\n' + \
               '\n'.join(['\t'.join([str(j) for j in i]) for i in self.card]) + f'\n{"-" * 27}'

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return item


class ComputerCard(HumanCard):
    def __str__(self):
        return f'----- Карточка компьютера ------\n' + \
               '\n'.join(['\t'.join([str(j) for j in i]) for i in self.card]) + f'\n{"-" * 27}'


class Game:
    def __init__(self, human, computer):
        self.card1 = human
        self.card2 = computer
        self.kegs = sample(range(1, 91), 90)
        self.keg = 0

    def kegs_generator(self):
        self.keg = self.kegs.pop(self.kegs.index(choice(self.kegs)))
        return f'Новый бочонок: {self.keg} (осталось {len(self.kegs)})'

    def find_index_human(self):
        if self.keg in self.card1[0]:
            return 0
        elif self.keg in self.card1[1]:
            return 1
        elif self.keg in self.card1[2]:
            return 2

    def find_index_computer(self):
        if self.keg in self.card2[0]:
            return 0
        elif self.keg in self.card2[1]:
            return 1
        elif self.keg in self.card2[2]:
            return 2

    def change(self, scroll):
        if self.keg in scroll:
            index_removed = scroll.index(self.keg)
            scroll.remove(self.keg)
            scroll.insert(index_removed, 'x')

    def game(self):
        while len(self.kegs) <= 90:
            print(Game.kegs_generator(self))
            print(self.card1)
            print(self.card2)
            print(f'Зачеркнуть цифру? (y/n)')
            if input('Ваш ответ (y/n): ').lower() == 'y' and self.keg not in self.card1[0] and self.keg not in self.card1[1] and self.keg not in self.card1[2]:
                print('Вы проиграли')
                break
            elif input('Ваш ответ (y/n): ').lower() == 'y' and (self.keg in self.card1[0] or self.keg in self.card1[1] or self.keg in self.card1[2]):
                Game.change(self, self.card1[Game.find_index_human(self)])
                Game.change(self, self.card2[Game.find_index_computer(self)])
                #
                continue
            elif input('Ваш ответ (y/n): ').lower() == 'n' and (self.keg in self.card1[0] or self.keg in self.card1[1] or self.keg in self.card1[2]):
                print('Вы проиграли')
                break
            elif input('Ваш ответ (y/n): ').lower() == 'n' and (self.keg not in self.card1[0] and self.keg not in self.card1[1] and self.keg not in self.card1[2]):
                continue
            else:
                print('Введите (y/n)')


human = HumanCard()
computer = ComputerCard()
Game(human, computer).game()
