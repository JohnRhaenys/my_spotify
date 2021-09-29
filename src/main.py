import sys
from PyQt5 import QtWidgets
from src.core.database import data_manager
from ui.main_window.main_window import MainWindow

if __name__ == "__main__":
    data_manager.create_tables()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow(main_window)
    main_window.show()
    sys.exit(app.exec_())
