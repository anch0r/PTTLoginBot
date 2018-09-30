# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import  QApplication, QMainWindow, QFileDialog, QMessageBox
from gui import Ui_MainWindow
from Invoker import doLogin
from Status import Status
from UI_Updater import UI_ButtonUpdater, UI_TextFieldAndLabelUpdater, UI_LoadFileTextFieldAndLabelUpdater
from FileHandler import export,load

class AppWindow(QMainWindow):
    #lists to pack GUI elements
    accountList = []
    passwordList = []
    statList = []
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.setFixedSize(500,620)
        #login button click event
        self.ui.runLogin.clicked.connect(self.runLogin)

        #clear button click event
        self.ui.clear.clicked.connect(self.clearAll)

        #export button click event
        self.ui.exportButton.clicked.connect(self.exportToFile)

        #load file button click event
        self.ui.loadFileButton.clicked.connect(self.loadFile)
    
    def pack(self):
        #pack username and password fields
        self.accountList.append(self.ui.accText1)
        self.accountList.append(self.ui.accText2)
        self.accountList.append(self.ui.accText3)
        self.accountList.append(self.ui.accText4)
        self.accountList.append(self.ui.accText5)
        self.accountList.append(self.ui.accText6)
        self.accountList.append(self.ui.accText7)
        self.accountList.append(self.ui.accText8)
        self.accountList.append(self.ui.accText9)
        self.accountList.append(self.ui.accText10)

        self.passwordList.append(self.ui.passText1)
        self.passwordList.append(self.ui.passText2)
        self.passwordList.append(self.ui.passText3)
        self.passwordList.append(self.ui.passText4)
        self.passwordList.append(self.ui.passText5)
        self.passwordList.append(self.ui.passText6)
        self.passwordList.append(self.ui.passText7)
        self.passwordList.append(self.ui.passText8)
        self.passwordList.append(self.ui.passText9)
        self.passwordList.append(self.ui.passText10)
        
        #pack status labels
        self.statList.append(self.ui.statLabel1)
        self.statList.append(self.ui.statLabel2)
        self.statList.append(self.ui.statLabel3)
        self.statList.append(self.ui.statLabel4)
        self.statList.append(self.ui.statLabel5)
        self.statList.append(self.ui.statLabel6)
        self.statList.append(self.ui.statLabel7)
        self.statList.append(self.ui.statLabel8)
        self.statList.append(self.ui.statLabel9)
        self.statList.append(self.ui.statLabel10)
        
    def runLogin(self):
        #clear lists first
        self.accountList.clear()
        self.passwordList.clear()
        self.statList.clear()
       
        #update UI
        UI_ButtonUpdater(Status.STAT_RUNLOGIN_BUTTON_CLICKED, self.ui.runLogin, self.ui.clear, 
                        self.ui.exportButton, self.ui.loadFileButton)

        #pack UI components              
        self.pack()
        
        #update UI
        UI_TextFieldAndLabelUpdater(Status.STAT_RUNLOGIN_BUTTON_CLICKED, self.accountList, self.passwordList, self.statList)
        
        #login
        doLogin(self.accountList, self.passwordList, self.statList, self.ui.runLogin, self.ui.clear, 
                self.ui.exportButton, self.ui.loadFileButton)
    
    def clearAll(self):
        self.accountList.clear()
        self.passwordList.clear()
        self.statList.clear()
        
        UI_ButtonUpdater(Status.STAT_CLEAR_BUTTON_CLICKED, self.ui.runLogin, self.ui.clear,
                        self.ui.exportButton, self.ui.loadFileButton)

        self.pack()

        UI_TextFieldAndLabelUpdater(Status.STAT_CLEAR_BUTTON_CLICKED, self.accountList, self.passwordList, self.statList)

        #cleaning work done,update UI
        UI_TextFieldAndLabelUpdater(Status.STAT_WORK_DONE, self.accountList, self.passwordList, self.statList)
        UI_ButtonUpdater(Status.STAT_WORK_DONE, self.ui.runLogin, self.ui.clear,
                        self.ui.exportButton, self.ui.loadFileButton)
    
    def exportToFile(self):
        self.accountList.clear()
        self.passwordList.clear()
        self.statList.clear()

        UI_ButtonUpdater(Status.STAT_EXPORT_BUTTON_CLICKED, self.ui.runLogin, self.ui.clear,
                        self.ui.exportButton, self.ui.loadFileButton)
        self.pack()

        status_ = export(self.accountList, self.passwordList)

        if status_ == Status.STAT_EXPORT_SUCCESS:
            QMessageBox.information(self, '匯出', '匯出成功')
        if status_ == Status.STAT_FILE_IO_ERROR:
            QMessageBox.critical(self, 'Critical', '匯出失敗!')
        
        UI_ButtonUpdater(Status.STAT_WORK_DONE, self.ui.runLogin, self.ui.clear,
                        self.ui.exportButton, self.ui.loadFileButton)

    def loadFile(self):
        self.accountList.clear()
        self.passwordList.clear()
        self.statList.clear()

        loadUsernameList = []
        loadPasswordList = []

        UI_ButtonUpdater(Status.STAT_LOADFILE_BUTTON_CLICKED, self.ui.runLogin, self.ui.clear,
                        self.ui.exportButton, self.ui.loadFileButton)
        self.pack()

        fileName,fileType = QFileDialog.getOpenFileName(self, '選擇帳密檔', './', 'CSV Files (*.csv)')

        status_ = load(fileName, loadUsernameList, loadPasswordList)

        if status_ == Status.STAT_LOADFILE_SUCCESS:
            UI_LoadFileTextFieldAndLabelUpdater(status_, self.accountList, self.passwordList,
                                                self.statList, loadUsernameList, loadPasswordList)
        if status_ == Status.STAT_FILE_IO_ERROR:
           QMessageBox.critical(self, 'Critical', '讀取帳密檔失敗!')

        UI_ButtonUpdater(Status.STAT_WORK_DONE, self.ui.runLogin, self.ui.clear,
                        self.ui.exportButton, self.ui.loadFileButton)

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
