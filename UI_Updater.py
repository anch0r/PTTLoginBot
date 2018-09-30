# -*- coding: utf-8 -*-
from Status import Status

def UI_TextFieldAndLabelUpdater(status_, accTextField, passTextField, statusLabel):
    if status_ == Status.STAT_RUNLOGIN_BUTTON_CLICKED:
        #working,set text fields ineditable
        for i in range(10):
            accTextField[i].setReadOnly(True)
            passTextField[i].setReadOnly(True)
    if status_ == Status.STAT_CLEAR_BUTTON_CLICKED:
        #clear all text fields & status labels
        for i in range(10):
            accTextField[i].setReadOnly(True)
            passTextField[i].setReadOnly(True)
            accTextField[i].setPlainText('')
            passTextField[i].setPlainText('')
            accTextField[i].setReadOnly(False)
            passTextField[i].setReadOnly(False)
            statusLabel[i].setText('N/A')
            statusLabel[i].repaint()
    if status_ == Status.STAT_CONNECTING:
        statusLabel.setText('連線中')
        statusLabel.repaint()
    if status_ == Status.STAT_LOGIN_SUCCESS:
        statusLabel.setText('成功!')
        statusLabel.repaint()
    if status_ == Status.STAT_LOGIN_FAILED:
        statusLabel.setText('帳密錯誤')
        statusLabel.repaint()
    if status_ == Status.STAT_OS_ERROR:
        statusLabel.setText('系統錯誤')
        statusLabel.repaint()
    if status_ == Status.STAT_SERVER_OVERLOAD:
        statusLabel.setText('系統過載')
        statusLabel.repaint()
    if status_ == Status.STAT_WORK_DONE:
        #word done,set text fields editable
        for i in range(10):
            accTextField[i].setReadOnly(False)
            passTextField[i].setReadOnly(False)

def UI_LoadFileTextFieldAndLabelUpdater(status_, accTextField, passTextField, statusLabel, loadUsernameList, loadPasswordList):
    if status_ == Status.STAT_LOADFILE_SUCCESS:
        #file loaded,clean text fields & reset status labels first
        UI_TextFieldAndLabelUpdater(Status.STAT_CLEAR_BUTTON_CLICKED, accTextField, passTextField, statusLabel)
        UI_TextFieldAndLabelUpdater(Status.STAT_WORK_DONE, accTextField, passTextField, statusLabel)
        for i in range(len(loadUsernameList)):
            accTextField[i].setPlainText(loadUsernameList[i])
            passTextField[i].setPlainText(loadPasswordList[i])



def UI_ButtonUpdater(status_, runLoginButton, clearButton, exportButton, loadFileButton):
    if status_ == Status.STAT_RUNLOGIN_BUTTON_CLICKED or Status.STAT_CLEAR_BUTTON_CLICKED \
                  or Status.STAT_EXPORT_BUTTON_CLICKED or Status.STAT_LOADFILE_BUTTON_CLICKED:
        #disable buttons to prevent click spam
        runLoginButton.setEnabled(False)
        clearButton.setEnabled(False)
        exportButton.setEnabled(False)
        loadFileButton.setEnabled(False)
    if status_ == Status.STAT_WORK_DONE:
        #work done,enable buttons
        runLoginButton.setEnabled(True)
        clearButton.setEnabled(True)
        exportButton.setEnabled(True)
        loadFileButton.setEnabled(True)