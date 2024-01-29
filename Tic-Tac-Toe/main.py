import Board


def main():

    app = Board.QtWidgets.QApplication([])
    window = Board.Board()
    Board.sys.exit(app.exec())


if __name__ == '__main__':
    main()