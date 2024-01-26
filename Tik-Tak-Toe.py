# Zaimportowałem bibliotekę TKinter i random utworzyłem okno graficzne i uruchomiłem kod.
from tkinter import *
import random
root = Tk()
root.title('Criss-cross')
game_run = True
field = []
cross_count = 0

# Ta funkcja jest potrzebna do aktualizacji tabeli dla gry i jej edycji. Ustawia kolor tła i zmienia tekst na przyciskach.
def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run #Funkcja 'global' jest potrzebna, aby zmienna była dostępna dla całego kodu, a nie tylko odczytywana w samej funkcji
    game_run = True
    global cross_count
    cross_count = 0

# Ta funkcja jest potrzebna do rejestrowania moich ruchów i służy do rozpoczęcia gry.
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

#Ta funkcja jest potrzebna do sprawdzenia komórek pod kątem wyniku gry
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

#Jeśli funkcja znajdzie wiersz z tymi samymi znakami, pokoloruje je inaczej i zakończy grę
def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

#Funkcja sprawdza, czy gracz może wygrać następną turę i w jakich przypadkach
def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

#Ta funkcja jest odpowiedzialna za działanie ruchów komputera. Działa ona na podstawie pracy poprzedniej funkcji can_win.
# Jeśli nie ma ruchu, w którym gracz może wygrać w następnym ruchu, to 0 jest po prostu umieszczane w losowym miejscu
def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

#Pisklę to tylko ustawienia samego okna. Jego charakterystyka, że tak powiem
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=8, height=5,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
