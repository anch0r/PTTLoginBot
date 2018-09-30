import csv
from Status import Status
from UI_Updater import UI_TextFieldAndLabelUpdater

def export(usernameList, passwordList):
    try:
        with open('list.csv', 'w', newline = '') as csvFile:
            csvWriter = csv.writer(csvFile)
            for i in range(10):
                if (usernameList[i].toPlainText().strip() != '') and (passwordList[i].toPlainText().strip() != ''):
                    csvWriter.writerow([usernameList[i].toPlainText().strip(), passwordList[i].toPlainText().strip()])
        csvFile.close()
        return Status.STAT_EXPORT_SUCCESS
    except IOError:
        return Status.STAT_FILE_IO_ERROR

def load(file, loadUsernameList, loadPasswordList):
    try:
        with open(file, 'r', newline = '') as csvFile:
            rows = csv.reader(csvFile)
            list_ = []
            for data in rows:
                list_.append(data)
            for i in range(len(list_)):
                loadUsernameList.append(list_[i][0])
                loadPasswordList.append(list_[i][1])    
        csvFile.close()
        return Status.STAT_LOADFILE_SUCCESS
    except IOError:
        return Status.STAT_FILE_IO_ERROR





