from os import system
from random import randint, choice
import pygame
from pygame_widgets import update
from pygame_widgets.button import Button


class Game():
    def __init__(self, number_of_players=1) -> None: # TODO: переделать робот/человек
        self.players = []
        self.img_players = ["X", "O"]
        if number_of_players == 1:
            player1 = Player(False, self.img_players[0])
            player2 = Player(img=self.img_players[1])
            self.players.append(player1)
            self.players.append(player2)
        elif number_of_players == 2:
            player1 = Player(False, self.img_players[0])
            player2 = Player(False, self.img_players[1])
            self.players.append(player1)
            self.players.append(player2)
        else:
            for i in range(2):
                player = Player(img=self.img_players[i-1])
                self.players.append(player)
        self.field = Field()

    def run(self) -> None:
        """Основной Цикл игры"""
        while True:
            for t in range(9):
                #self.field.draw()
                if t % 2 == 0:  # DRY в elif и else
                    #self.players[0].make_move(self.field.cells, self.field.victories)
                    if self.field.get_result():
                        #self.field.draw()
                        #input(f"{self.players[0].img} выйграли! Нажмите Enter что бы закрыть программу")
                        break
                else:
                    self.players[1].make_move(self.field.cells, self.field.victories)
                    if self.field.get_result():
                        #self.field.draw()
                        #input(f"{self.players[1].img} выйграли! Нажмите Enter что бы закрыть программу")
                        break
            #input("Ничья! Нажмите Enter что бы закрыть программу")
            break


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

    def make_move(self, field, victories, button_num) -> None:
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
            index = button_num
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
        self.game = Game()
        self.Show_XO_window()

    def Show_XO_window(self):
        pygame.init()
        win = pygame.display.set_mode((470, 470))

        # Creates the button with optional parameters
        button0 = Button(
            # Mandatory Parameters
            win,  # Surface to place button on
            0,  # X-coordinate of top left corner
            0,  # Y-coordinate of top left corner
            150,  # Width
            150,  # Height

            # Optional Parameters
            text=str(self.game.field.cells[0]),  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: self.who_moves(0)  # Function to call when clicked on
        )
        button1 = Button(win, 160, 0, 150, 150, text=str(self.game.field.cells[1]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(1))
        
        button3 = Button(win, 0, 160, 150, 150, text=str(self.game.field.cells[3]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(3))
        
        button2 = Button(win, 320, 0, 150, 150, text=str(self.game.field.cells[2]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(2))
        
        button6 = Button(win, 0, 320, 150, 150, text=str(self.game.field.cells[6]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(6))
        
        button4 = Button(win, 160, 160, 150, 150, text=str(self.game.field.cells[4]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(4))
        
        button8 = Button(win, 320, 320, 150, 150, text=str(self.game.field.cells[8]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(8))
        
        button7 = Button(win, 160, 320, 150, 150, text=str(self.game.field.cells[7]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(7))
        
        button5 = Button(win, 320, 160, 150, 150, text=str(self.game.field.cells[5]), fontSize=50, margin=20,
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), 
                          radius=20, onClick=lambda: self.who_moves(5))


        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

            win.fill((255, 255, 255))

            update(events)  # Call once every loop to allow widgets to render and listen
            pygame.display.update()

    def who_moves(self, button_num):
        pass


app = App()  # TODO: Как собрать статистику 100 игр компа с компом?
