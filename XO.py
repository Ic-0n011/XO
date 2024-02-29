from os import system
from random import randint, choice


class Game():
    def __init__(self, number_of_players) -> None: # TODO: переделать робот/человек 
        p1 = True  # Зачем дефолты, для трех игроков?
        p2 = True
        if number_of_players == 2:
            p1 = False  # Это не ПЭодин, а is_automatic
            p2 = False
        elif number_of_players == 1:
            if randint(1, 2) == 1:
                p1 = False
            else:
                p2 = False
        self.player_1 = Player(p1, "X")
        self.player_2 = Player(p2, "O")
        self.field = Field()

    def run(self) -> None:
        """Основной Цикл игры"""
        moves = 1
        while True:
            self.field.draw()
            if moves > 9:
                #input("Ничья! Нажмите Enter что бы закрыть программу")
                qwer = "?"
                break
            elif moves % 2 == 0:  # DRY в elif и else
                self.player_2.make_move(self.field.cells, self.field.victories)
                if self.field.get_result():
                    self.field.draw()
                    #input("Нолики выйграли! Нажмите Enter что бы закрыть программу")  # Хардкод: если создать игрока '+', то все равно будут нолики
                    break
            else:
                self.player_1.make_move(self.field.cells, self.field.victories)
                if self.field.get_result():
                    self.field.draw()
                    #input("Крестики выйграли! Нажмите Enter что бы закрыть программу")
                    break
            moves += 1


class Field():
    def __init__(self) -> None:
        """Класс поле, хранит в себе клетки и 8 выйгрышных позиций"""
        self.cells = [i for i in range(1, 10)]
        self.victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],  # TODO: написать функцию которая генерирует ВСЕ выйгрышные варианты
                          [1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def draw(self) -> None:
        # рисует поле
        system("cls")
        for i in range(0, 8, 3):
            print(f"{self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} ")
            print("—   —   —")

    def get_result(self) -> bool:
        # проверяет есть ли выйгрышная ситуация на поле
        for i in self.victories:
            if self.cells[i[0]] == "X" and self.cells[i[1]] == "X" and self.cells[i[2]] == "X":
                return True
            if self.cells[i[0]] == "O" and self.cells[i[1]] == "O" and self.cells[i[2]] == "O":
                return True
        return False


class Player():
    def __init__(self, is_automatic=True, img=None) -> None:  # FIXME: Что будет, если не дать игроку img?
        self.is_automatic = is_automatic
        self.img = img

    def make_move(self, field, victories) -> None:
        if self.is_automatic:
            """
            РОБОТ - проверка нескольких вариантов
            1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
            2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
            3) если 1 фигура своя и 0 чужих - ставим
            4) центр пуст, то занимаем центр
            5) если центр занят, то занимаем первую ячейку
            6) если ни один из параметров не подошел
            """
            step = self.check_line(2, 0, field, victories)
            step =  self.check_line(0, 2, field, victories, step)
            step =  self.check_line(1,0, field, victories, step)
            if not step:
                if isinstance(field[4], int):
                    step = 5
                elif isinstance(field[0], int):
                    step = 1
                else:
                    step = choice(list(filter(lambda x: isinstance(x, int) and x > 0, field)))
            index = (step - 1)
        else:
            # ЧЕЛОВЕК - цикл в котором игрок выбирает ход
            while True:
                try:
                    step = int(input(f'Введите номер клетки {self.img}: '))
                except ValueError:
                    print("Ошибка! Номер клетки должен быть целым числом!")
                    continue
                if 0 > step > 9:
                    print("Ошибка! Номер клетки должен быть целым числом!")
                    continue
                index = step - 1
                if not isinstance(field[index], int):
                    print("Ошибка! Эта клетка занята!")
                    continue
                break
        field[index] = self.img

    def check_line(self, sum_O, sum_X, field, victories, step=None) -> int | None:
        # Нет докстроки
        step = step
        if not step:
            for line in victories:
                o = 0
                x = 0
                for j in range(0,3):
                    if field[line[j]] == "O":
                        o = o + 1
                    if field[line[j]] == "X":
                        x = x + 1
                if o == sum_O and x == sum_X:
                    for j in range(0,3):
                        if field[line[j]] != "O" and field[line[j]] != "X":
                            step = field[line[j]]
        return step


class App():
    def __init__(self) -> None:
        self.new_game()
        self.game = Game(0)
        self.game.run()

    def new_game(self):
        while True:
            print("ВЫБЕРИТЕ КОЛЛИЧЕСТВО ИГРОКОВ")
            print("0 - робот против робота; 1 - игрок против робота; , 2 -игрок против игрока;")
            number_of_players = input("Напишите целое число колличества игроков: ")
            try:
                number_of_players = int(number_of_players)
            except ValueError:
                print("Ошибка! Наипишите целое число от 0 до 2!")
            if number_of_players == 0 or number_of_players == 1 or number_of_players == 2:
                self.number_of_players = number_of_players
                break
            else:
                print("Ошибка! Число игроков не допустимо, всего игроков может быть от 0 до 2!")


App()  # TODO: Как собрать статистику 100 игр компа с компом?