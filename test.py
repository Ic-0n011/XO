import pygame
from pygame_widgets import update
from pygame_widgets.button import Button

# Set up Pygame
def Show_XO_window():
    pygame.init()
    win = pygame.display.set_mode((470, 470))

    # Creates the button with optional parameters
    button = Button(
        # Mandatory Parameters
        win,  # Surface to place button on
        0,  # X-coordinate of top left corner
        0,  # Y-coordinate of top left corner
        150,  # Width
        150,  # Height

        # Optional Parameters
        text='Hello',  # Text to display
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: print('Click')  # Function to call when clicked on
    )
    button1 = Button(win, 160, 0, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))
    button2 = Button(win, 0, 160, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))
    button3 = Button(win, 320, 0, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))
    button4 = Button(win, 0, 320, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))
    button5 = Button(win, 160, 160, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))
    button6 = Button(win, 320, 320, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))
    button7 = Button(win, 160, 320, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))
    button8 = Button(win, 320, 160, 150, 150, text='Hello', fontSize=50, margin=20, inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick=lambda: print('Click'))


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

Show_XO_window()