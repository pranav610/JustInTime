# This Python file uses the following encoding: utf-8
from PySide2 import QtCore


class CustomTableModel(QtCore.QAbstractTableModel):
    def __init__(self,data):
        super().__init__(self)
        self.user_data = data
        self.columns = list(self.user_data)
