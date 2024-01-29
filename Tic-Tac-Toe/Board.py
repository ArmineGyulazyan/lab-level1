import sys
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
import Player


class Board(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.player = Player.Player('X')

        #Creating main window
        self.setWindowTitle('Tic-Tac-Toe')
        self.setGeometry(100, 100, 300, 300)

        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)

        #Creating main container, that will hold other layouts
        self.container_layout = QtWidgets.QVBoxLayout(self.main_widget)

        self.create_board_components()
        self.other_design_components()
        self.show()
        
    def create_board_components(self):
        '''
        This function creates the board with GridLayout
        layout manager that consists of buttons
        '''

        self.board = QtWidgets.QGridLayout()
        self.container_layout.addLayout(self.board)

        self.play_buttons = [[QtWidgets.QPushButton('', font=QtGui.QFont('Times New Roman',26)) for _ in range(3)]for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.play_buttons[i][j].setFixedSize(110,110)
                self.board.addWidget(self.play_buttons[i][j],i,j)
                self.play_buttons[i][j].clicked.connect(self.on_button_click)

    def other_design_components(self):
        '''
        This function creates other design components such as
        the second layout that contains the label that shows player's turn and who won
        and the restart button
        '''
        self.down_layout = QtWidgets.QVBoxLayout()
        self.container_layout.addLayout(self.down_layout)
        self.turn_label = QtWidgets.QLabel("It's X-s turn",alignment=QtCore.Qt.AlignmentFlag.AlignCenter,font=QtGui.QFont('Times New Roman',18))
        self.down_layout.addWidget(self.turn_label)

        restart_game = QtWidgets.QPushButton('Restart Game',font=QtGui.QFont('Times New Roman',18))
        self.down_layout.addWidget(restart_game,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        restart_game.clicked.connect(self.restart_game)

    def winner_check(self):
        '''
        This function checks for the winner of the game,
        at first it checks by rows, then columns and then the two diagonals
        :return Player object or None
        '''
        for i in range(3):
            if self.play_buttons[i][0].text() != '' and self.play_buttons[i][0].text() == self.play_buttons[i][1].text() == self.play_buttons[i][2].text():
                return self.player

            if self.play_buttons[0][i].text() != '' and self.play_buttons[0][i].text() == self.play_buttons[1][i].text() == self.play_buttons[2][i].text():
                return self.player

            if self.play_buttons[0][i].text() != '' and self.play_buttons[0][i].text() == self.play_buttons[1][i].text() == self.play_buttons[2][i].text():
                return self.player

        if self.play_buttons[0][0].text() != '' and self.play_buttons[0][0].text() == self.play_buttons[1][1].text() == self.play_buttons[2][2].text():
            return self.player

        if self.play_buttons[0][2].text() != '' and self.play_buttons[0][2].text() == self.play_buttons[1][1].text() == self.play_buttons[2][0].text():
            return self.player

        return None

    def on_button_click(self):
        '''
        This function is called when the player clicks on the button.
        At first it increments the quantity of players moves, then fixes the button that was clicked,
        then checks it was an 'X' or 'O' and after every move it checks for the winner by calling the winner_check function.
        '''
        self.player.move_times += 1

        clicked_button = self.sender()
        clicked_button.setEnabled(False)

        if self.player.turn == 'X':
            clicked_button.setText('X')
            self.player.turn = 'O'
            self.turn_label.setText("It's O's turn")
        else:
            clicked_button.setText('O')
            self.player.turn = 'X'
            self.turn_label.setText("It's X's turn")

        winner = self.winner_check()
        if winner:
            if self.player.turn == 'X':
                self.turn_label.setText("O Won!!!")
            else:
                self.turn_label.setText("X Won!!!")
            for buttons in self.play_buttons:
                for push in buttons:
                    push.setEnabled(False)

    def restart_game(self):
        '''
        This function is called when the player clicks on the 'Restart Game' button,
        it sets the player turn to None and the times a playaer has made a move to 0 then changes the label
        and sets the text on buttons to empty strings.
        '''

        self.player.turn = None
        self.player.move_times = 0
        self.turn_label.setText("It's X's turn")
        for buttons in self.play_buttons:
            for push in buttons:
                push.setText('')
                push.setEnabled(True)




