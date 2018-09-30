# -*- coding: utf-8 -*-
import threading,queue
from LoginWorker import telnetConnect
from Status import Status
from UI_Updater import UI_TextFieldAndLabelUpdater,UI_ButtonUpdater

def doLogin(usernameList, passwordList, statusList, runLoginButton, clearButton, exportButton, loadFileButton):
    # queue for the return value of telnetConnect() 
    statusQueue = queue.Queue() 
    for i in range(10):
        #exclude blank field
        if usernameList[i].toPlainText().strip() != '':
            UI_TextFieldAndLabelUpdater(Status.STAT_CONNECTING, usernameList[i], passwordList[i],statusList[i])
            #create a new thread for telnet conneting to avoid time.sleep() in telnetConnect blocking main thread updating GUI components  
            t = threading.Thread(target=telnetConnect,
                                args=((usernameList[i].toPlainText().strip()), (passwordList[i].toPlainText().strip()),
                                     (statusQueue)))
            t.start()
            UI_TextFieldAndLabelUpdater(statusQueue.get(), usernameList[i], passwordList[i],statusList[i])
            t.join()
    #work done,enable all text fields & buttons
    UI_TextFieldAndLabelUpdater(Status.STAT_WORK_DONE, usernameList, passwordList, statusList)
    UI_ButtonUpdater(Status.STAT_WORK_DONE, runLoginButton, clearButton, exportButton, loadFileButton)        

    


