from random import *


class HumanCard:
    def __init__(self):
        self.nums = sample(range(1, 91), 15)
        shuffle(self.nums)
        self.card = []
        for i in sorted(self.nums[:5]):
            self.card.append(i)
        for i in sorted(self.nums[5:10]):
            self.card.append(i)
        for i in sorted(self.nums[10:15]):
            self.card.append(i)

    def __str__(self):
        return f'----- Ваша карточка ------\n' + \
               '\t'.join([str(i) for i in self.card[:5]]) + '\n' + \
               '\t'.join([str(i) for i in self.card[5:10]]) + '\n' + \
               '\t'.join([str(i) for i in self.card[10:15]]) + '\n' + \
               f'{"-" * 26}'


class ComputerCard(HumanCard):
    def __str__(self):
        return f'--- Карточка компьютера ---\n' + \
               '\t'.join([str(i) for i in self.card[:5]]) + '\n' + \
               '\t'.join([str(i) for i in self.card[5:10]]) + '\n' + \
               '\t'.join([str(i) for i in self.card[10:15]]) + '\n' + \
               f'{"-" * 26}'


class Game:
    def __init__(self, _human, _computer):
        self.card1 = _human
        self.card2 = _computer
        self.kegs = sample(range(1, 91), 90)

    def kegs_generator(self):
        self.keg = self.kegs.pop(self.kegs.index(choice(self.kegs)))
        return f'\nНовый бочонок: {self.keg} (осталось {len(self.kegs)})'

    def change(self, scroll):
        if self.keg in scroll:
            index_removed = scroll.index(self.keg)
            scroll.remove(self.keg)
            scroll.insert(index_removed, 'X')

    def change_in_comp(self):
        if self.keg in self.card2.card:
            Game.change(self, self.card2.card)

    def game(self):
        while len(self.kegs) > 0:
            print(Game.kegs_generator(self))
            print(self.card1)
            print(self.card2)
            print(f'Зачеркнуть цифру? (y/n)')
            user_answer = input('Ваш ответ (y/n): ').lower()
            if user_answer == 'y' and self.keg not in self.card1.card:
                print('Вы проиграли')
                break
            elif user_answer == 'y' and self.keg in self.card1.card:
                Game.change(self, self.card1.card)
                Game.change_in_comp(self)
                if self.card2.card.count('X') == 15:
                    Game.change_in_comp(self)
                    print('Компьютер выиграл. Вы проиграли.')
                    break
                if self.card1.card.count('X') == 15:
                    Game.change_in_comp(self)
                    print('Вы выиграли.')
                    break
                if self.card1.card.count('X') == 15 and self.card2.card.count('X') == 15:
                    Game.change(self, self.card1.card)
                    Game.change_in_comp(self)
                    print('Ничья')
                    break
                continue
            elif user_answer == 'n' and self.keg in self.card1.card:
                print('Вы проиграли')
                break
            elif user_answer == 'n' and self.keg not in self.card1.card:
                Game.change_in_comp(self)
                if self.card2.card.count('X') == 15:
                    print('Компьютер выиграл. Вы проиграли.')
                    break
                continue


if __name__ == '__main__':
    human = HumanCard()
    computer = ComputerCard()
    Game(human, computer).game()
