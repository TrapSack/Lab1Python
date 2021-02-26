from datetime import date
import os
import sys
import time

class Message():
    def __init__(self,message:str):
        self.message = message
        self.date = str(date.today())
    
class MessageList():
    def __init__(self):
        self.messageList = list()

    def add(self,message:Message):
        self.messageList.append(message)
    
    def show(self):
        os.system('clear')
        for msg in self.messageList:
            print(msg.message + ' ' + msg.date + '\n')
        
newML = MessageList()

# print(str(newML.messageList))

def menu():
    os.system('clear')
    choice = str(input("1|Get to chat\n2|Add a message\n3|Exit\n"))
    if choice == '1':
        if newML.messageList == []:
          print('No messages!')
          time.sleep(1)
        else:
          newML.show()
          temp = input('Print anything to exit')      
          if temp :
                menu()
    elif choice == '2':
        os.system('clear')
        newTXT = str(input('Enter a message\n'))
        newML.add(Message(newTXT))
        menu()
    elif choice == '3':
        sys.exit()
    else:
        os.system('clear')
        print('No such parameter')
        time.sleep(1)
        menu()

menu()