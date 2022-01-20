#Import OS library to acquire windows manipulation capabilities
import os
#datetime (date) to get current date
from datetime import date
from turtle import end_fill
#wind10toast (toastnotifier) to get pop up messages on Windows
from win10toast import ToastNotifier
#Save the date as a variable
myDate= str(date.today())
#assignes a variable to the notification pop up message
toaster = ToastNotifier()
#User's input for the variables ProjectName and extension
ProjectName = str(input('proyect?'))
extension = str(input('file_extension'))
#Counter to name the files
counter = 1
#iteration through all the objects - 1. name will act as placeholder for all the files inside de desired destination
for name in os.listdir("<files_path>"):
    #endswith() is a python method
    if name.endswith(extension):
        print(name)
        #New variable that holds the counter value as string to add it to the new filename
        countstr=str(counter)
        #New name of the file concatenating variables (as strings) and strings.
        newname = ProjectName+'_'+countstr+'_'+myDate+'.'+extension
        #Increase counter
        counter=counter+1
        #os package with rename functionality (src,dst)
        os.rename(name, newname)
        #Pop Up message on Windows
        toaster.show_toast('The old file '+name+' has been changed to '+newname)
        #print new name of the file on terminal to keep track on backend
        print (newname)
#End Of Script
