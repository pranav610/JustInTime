# IMPORTS FOR GUI
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
import databaseOperations
from PySide2.QtGui import QBrush,QColor

# IMPORTS FOR DATABASE MODEL
import databaseOperations
from Database import *


class CustomTableModel(QtCore.QAbstractTableModel):
    """
    Class to create custom table model 
    """
    def __init__(self,table):
        QtCore.QAbstractTableModel.__init__(self)
        self.table_name = table.name
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        self.columns = table.headers 
        self.column_names = table.column_names
    
        
    def flags(self, index):
        """
        Will set the flags for the table cells
        @param index: index of the cell
        make first column non editable
        """
        # print(index.column())
        if index.column() > 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        # elif index.column() == 1:
        #     return QtCore.Qt.DecorationRole
        else:
            return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):
        """
        Will count number of rows in the table
        @param args:    
        @return: row count
        """
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        """
        Will count number of columns in the table
        @param args:
        @return: column count
        """
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """
        Will set the header data for the table
        @param section: section of the table
        @param orientation: orientation of the table
        @param role: role of the table
        @return: header data
        """
        
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            # print(self.columns[section])
            return self.columns[section]

    def data(self, index, role):
        """
        Will return the data in the table cells
        @param index: index of the cell
        @param role: role of the cell
        @return: data in the cell
        """
        row = self.user_data[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter 

        try:
            if role == QtCore.Qt.DisplayRole:
                if(row[index.column()]!= None):
                    return (row[index.column()])
                else:
                    return ""
        except KeyError:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        """
        Will set the data in the table cells
        @param index: index of the cell
        @param value: value to be set in the cell
        @param role: role of the cell
        @return: True if data is set
        """
        if index.isValid():
            selected_row = self.user_data[index.row()]
            selected_column = self.columns[index.column()]
            new_data = list(selected_row)
            new_data[index.column()] = value
            self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
            # if new_data[0] != "":
            ok = databaseOperations.update_existing(new_data[0], new_data[1:],self.column_names,self.table_name)
            self.user_data = databaseOperations.get_multiple_data(self.table_name)
            if ok:
                return True
        return False

    def insertRows(self):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = []
        for key in self.columns:
         if not key =='id_':
            empty_data.append("")
        document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        row_count += 1
        new_data = databaseOperations.get_single_data(row_count,self.table_name)
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        self.endInsertRows()
        return True

    def insertRows_vendor_part(self,details):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = []
        if len(details) == 1: #Vendor
            for key in self.columns:
             if not key =='id_':
                if key =="Vendor Name":
                    empty_data.append(str(details[0]))
                else:
                    empty_data.append("")
            print(empty_data)
            document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        else:
            for key in self.columns:
             if not key == 'id_':
                if key =="Part Name":
                    empty_data.append(str(details[0]))
                elif key == "Vehicle Type":
                    empty_data.append(str(details[1]))
                else:
                    empty_data.append("")
            document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        row_count += 1
        new_data = databaseOperations.get_single_data(row_count,self.table_name)
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        self.endInsertRows()
        return True

    def removeRows(self, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        if isinstance(position,int):
            document_id = self.user_data[position][0]
            databaseOperations.remove_data(document_id,self.table_name)
        elif isinstance(position,QtCore.QModelIndex):
            row_id = position.row()
            document_id = self.user_data[row_id][0]
            databaseOperations.remove_data(document_id,self.table_name)

        elif isinstance(position,list):
            for data in self.user_data:
                k = 0
                for i in range(len(position)):
                    if data[i+1] == position[i].data():
                        k+=1

                if(k == len(position)):           
                    rowid = data[0]
                    databaseOperations.remove_data(rowid,self.table_name)

        else:
            return False
        
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True


    def removeRows_fromList(self,details,position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)

        if len(details) == 1: #Vendor
            databaseOperations.remove_data_from_list(details,[position[0],position[1]],self.table_name)
        else:
            databaseOperations.remove_data_from_list(details,[position[0]],self.table_name)
        
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True

    def removeRows_vendor_part(self,details):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)

        if len(details) == 1: #Vendor
            databaseOperations.remove_data_vendor_part(details,self.table_name)
        else:
            databaseOperations.remove_data_vendor_part(details,self.table_name)
        
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True

class CustomTableModelThreshold(QtCore.QAbstractTableModel):
    """
    Custom Table Model 
    """
    def __init__(self,table):
        QtCore.QAbstractTableModel.__init__(self)
        self.table_name = table.name
        self.user_data = databaseOperations.get_multiple_data(self.table_name)

        self.columns = table.headers 
        self.column_names = table.column_names
    
        
    def flags(self, index):
        """
        Will make the table editable
        @param index: index of the cell
        @return: flags of the cell
        """
        # print(index.column())
        if index.column() > 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        # elif index.column() == 1:
        #     return QtCore.Qt.DecorationRole
        else:
            return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):
        """
        Will return the number of rows in the table
        @param args:
        @param kwargs:
        @return: number of rows in the table
        """
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        """
        Will set the number of columns in the table
        @param args:
        @param kwargs:
        @return: number of columns in the table
        """
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """
        Will set the header of the table
        @param section: section of the table
        @param orientation: orientation of the table
        @param role: role of the table
        @return: header of the table
        """
        
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            # print(self.columns[section])
            return self.columns[section]

    def data(self, index, role):
        """
        Will define the data of the table
        @param index: index of the cell
        @param role: role of the cell
        @return: data of the cell
        """
        row = self.user_data[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.BackgroundRole:
            if databaseOperations.get_stocksum([self.user_data[index.row()][2],self.user_data[index.row()][3]]) < databaseOperations.get_threshold([self.user_data[index.row()][2],self.user_data[index.row()][3]]):
                return QBrush(QColor(QtCore.Qt.red))


        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter 

        try:
            if role == QtCore.Qt.DisplayRole:
                if(row[index.column()]!= None):
                    return (row[index.column()])
                else:
                    return ""
        except KeyError:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        """
        Will edit data in table cells
        @param index: index of the cell
        @param value: value of the cell
        @param role: role of the cell
        @return: True if successful
        """
        if index.isValid():
            selected_row = self.user_data[index.row()]
            selected_column = self.columns[index.column()]
            new_data = list(selected_row)
            new_data[index.column()] = value
            self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
            # if new_data[0] != "":
            ok = databaseOperations.update_existing(new_data[0], new_data[1:],self.column_names,self.table_name)
            self.user_data = databaseOperations.get_multiple_data(self.table_name)
            if ok:
                return True
        return False

    def insertRows(self):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = []
        for key in self.columns:
         if not key =='id_':
            empty_data.append("")
        document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        row_count += 1
        new_data = databaseOperations.get_single_data(row_count,self.table_name)
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        self.endInsertRows()
        return True

    def insertRows_vendor_part(self,details):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = []
        if len(details) == 1: #Vendor
            for key in self.columns:
             if not key =='id_':
                if key =="Vendor Name":
                    empty_data.append(str(details[0]))
                else:
                    empty_data.append("")
            print(empty_data)
            document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        else:
            for key in self.columns:
             if not key == 'id_':
                if key =="Part Name":
                    empty_data.append(str(details[0]))
                elif key == "Vehicle Type":
                    empty_data.append(str(details[1]))
                else:
                    empty_data.append("")
            document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        row_count += 1
        new_data = databaseOperations.get_single_data(row_count,self.table_name)
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        self.endInsertRows()
        return True

    def removeRows(self, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        if isinstance(position,int):
            document_id = self.user_data[position][0]
            databaseOperations.remove_data(document_id,self.table_name)
        elif isinstance(position,QtCore.QModelIndex):
            row_id = position.row()
            document_id = self.user_data[row_id][0]
            databaseOperations.remove_data(document_id,self.table_name)

        elif isinstance(position,list):
            for data in self.user_data:
                k = 0
                for i in range(len(position)):
                    if data[i+1] == position[i].data():
                        k+=1

                if(k == len(position)):           
                    rowid = data[0]
                    databaseOperations.remove_data(rowid,self.table_name)

        else:
            return False
        
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True


    def removeRows_fromList(self,details,position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)

        if len(details) == 1: #Vendor
            databaseOperations.remove_data_from_list(details,[position[0],position[1]],self.table_name)
        else:
            databaseOperations.remove_data_from_list(details,[position[0]],self.table_name)
        
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True

    def removeRows_vendor_part(self,details):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)

        if len(details) == 1: #Vendor
            databaseOperations.remove_data_vendor_part(details,self.table_name)
        else:
            databaseOperations.remove_data_vendor_part(details,self.table_name)
        
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True

class CustomTableModelUserData(QtCore.QAbstractTableModel):
    """
    Custom Table Model for User Data
    """
    def __init__(self, data,headers,column_names,table_name):
        QtCore.QAbstractTableModel.__init__(self)
        self.user_data = data
        self.columns = headers 
        self.column_names = column_names
        self.table_name = table_name
        
    def flags(self, index):
        """
        This function is used to set the flags for the table view
        @param index: index of the table
        @return: flags
        """
        # print(index.column())
        if index.column() > 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        # elif index.column() == 1:
        #     return QtCore.Qt.DecorationRole
        else:
            return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):
        """
        Will set row counts
        @param args:
        @param kwargs:
        """
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            # print(self.columns[section])
            return self.columns[section]

    def data(self, index, role):
        row = self.user_data[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter 

        try:
            if role == QtCore.Qt.DisplayRole:
                if(row[index.column()]!= None):
                    return (row[index.column()])
                else:
                    return ""
        except KeyError:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            selected_row = self.user_data[index.row()]
            selected_column = self.columns[index.column()]
            new_data = list(selected_row)
            new_data[index.column()] = value
            self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
            ok = databaseOperations.update_existing(new_data[0], new_data[1:],self.column_names,self.table_name)
            self.user_data = databaseOperations.get_multiple_data(self.table_name)
            if ok:
                return True
        return False

    def insertRows(self,invoice_number):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = []
        for key in self.columns:
         if not key =='id_':
            empty_data.append("")
        document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        row_count += 1
        new_data = databaseOperations.get_single_data(row_count,self.table_name)
        self.user_data = databaseOperations.get_multiple_data_invoice(invoice_number,self.table_name)
        self.endInsertRows()
        return True

    def removeRows(self,invoice_number, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        row_id = position.row()
        document_id = self.user_data[row_id][0]
        # print("To be deleted: {}".format(document_id))
        databaseOperations.remove_data(document_id,self.table_name)
        self.user_data = databaseOperations.get_multiple_data_invoice(invoice_number,self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True

class CustomTableModelNoDatabase(QtCore.QAbstractTableModel):
    def __init__(self, data,headers,column_names,table_name):
        QtCore.QAbstractTableModel.__init__(self)
        self.user_data = data
        self.columns = headers 
        self.column_names = column_names
        self.table_name = table_name

    def add_data(self,data):
        self.user_data.append(data)
        
    def flags(self, index):
        # print(index.column())
        if index.column() > 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        # elif index.column() == 1:
        #     return QtCore.Qt.DecorationRole
        else:
            return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            # print(self.columns[section])
            return self.columns[section]

    def data(self, index, role):
        row = self.user_data[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter 

        try:
            if role == QtCore.Qt.DisplayRole:
                if(row[index.column()]!= None):
                    return (row[index.column()])
                else:
                    return ""
        except KeyError:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            selected_row = self.user_data[index.row()]
            selected_column = self.columns[index.column()]
            new_data = list(selected_row)
            new_data[index.column()] = value
            # self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
            # ok = databaseOperations.update_existing(new_data[0], new_data[1:],self.column_names,self.table_name)
            # self.user_data = databaseOperations.get_multiple_data(self.table_name)
            ok = True
            if ok:
                return True
        return False

    def insertRows(self,invoice_number):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = []
        for key in self.columns:
         if not key =='id_':
            empty_data.append("")
        # document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        row_count += 1
        # new_data = databaseOperations.get_single_data(row_count,self.table_name)
        self.user_data.append(new_data)
        self.endInsertRows()
        return True

    

    def removeRows(self,invoice_number, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        row_id = position.row()
        document_id = self.user_data[row_id][0]
        # print("To be deleted: {}".format(document_id))
        # databaseOperations.remove_data(document_id,self.table_name)
        self.user_data.pop(row_id)
        # print(self.user_data)
        self.endRemoveRows()
        return True


class CustomTableModelNoHeaders(QtCore.QAbstractTableModel):
    def __init__(self,data,headers):
        QtCore.QAbstractTableModel.__init__(self)
        self.user_data = data
        self.columns = headers

    
        
    def flags(self, index):
        """
        Make table editable.
        make first column non editable
        @param index: index of the cell
        @return: flags
        """
        # print(index.column())
        if index.column() > 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        # elif index.column() == 1:
        #     return QtCore.Qt.DecorationRole
        else:
            return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):  
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            # print(self.columns[section])
            return self.columns[section]

    def data(self, index, role):
        row = self.user_data[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter 

        try:
            if role == QtCore.Qt.DisplayRole:
                if(row[index.column()]!= None):
                    return (row[index.column()])
                else:
                    return ""
        except KeyError:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            selected_row = self.user_data[index.row()]
            selected_column = self.columns[index.column()]
            new_data = list(selected_row)
            new_data[index.column()] = value
            self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
            # if new_data[0] != "":
            ok = databaseOperations.update_existing(new_data[0], new_data[1:],self.column_names,self.table_name)
            self.user_data = databaseOperations.get_multiple_data(self.table_name)
            if ok:
                return True
        return False

    def insertRows(self):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = []
        for key in self.columns:
         if not key =='id_':
            empty_data.append("")
        document_id = databaseOperations.insert_data(empty_data,self.column_names,self.table_name)
        row_count += 1
        new_data = databaseOperations.get_single_data(row_count,self.table_name)
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        self.endInsertRows()
        return True

    def removeRows(self, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        if isinstance(position,int):
            document_id = self.user_data[position][0]
        else:
            row_id = position.row()
            document_id = self.user_data[row_id][0]
        # print("To be deleted: {}".format(document_id))
        print(document_id)
        databaseOperations.remove_data(document_id,self.table_name)
        self.user_data = databaseOperations.get_multiple_data(self.table_name)
        # print(self.user_data)
        self.endRemoveRows()
        return True


class ProfilePictureDelegate(QtWidgets.QStyledItemDelegate):
    """
    This will open QFileDialog to select image
    """
    def __init__(self):
        QtWidgets.QStyledItemDelegate.__init__(self)

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QFileDialog()
        return editor

    def setModelData(self, editor, model, index):
        selected_file =editor.selectedFiles()[0]
        image = open(selected_file, 'rb').read()
        model.setData(index, image)


class InLineEditDelegate(QtWidgets.QItemDelegate):
    def createEditor(self, parent, option, index):
        return super(InLineEditDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        text = index.data(QtCore.Qt.EditRole) or index.data(QtCore.Qt.DisplayRole)
        editor.setText(str(text))