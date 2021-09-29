from PyQt5.QtWidgets import QMessageBox


class DialogBox:
    def __init__(self, icon, title, message):

        msg = QMessageBox()

        if icon == 'information' or icon == 'success':
            msg.setIcon(QMessageBox.Information)
        elif icon == 'danger':
            msg.setIcon(QMessageBox.Critical)

        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle("Info")
        msg.exec_()
