from io import BytesIO
import re
import time
import zipfile
import os
import requests
from colorama import init, Style, Fore, Back, Cursor, deinit
import climage
import shutil
import winreg
from win32com.client import Dispatch

def getin(): #get 'y' or 'n'
   while True:
      inp=input()
      if re.match(r"[nN]",inp):return False
      elif re.match(r"[yY]",inp):return True
      else : print("\n i didn't understand you. please answer with [y] or [n] :")

def showgoose(): #show goose's picture
   deinit()
   print('')
   os.system('')
   print(climage.convert(filename="gooseicon.png",is_unicode=True))
   print('')

def print_info(): #print goose's info
   init()
   tsize=shutil.get_terminal_size()
   print(Style.BRIGHT+Fore.GREEN+"Desktop Goose".center(tsize[0]))
   print(Fore.CYAN+"\n\n            this is DesktopGoose, a goose for your desktop\n"           
   +"            It wlil be your desktop pet, walks everywhere, poops everywhere and you can't stop it\n"
   +"            if you annoy it, honks and steals your mouse,our goose is really rude and loves crime\n"
   +"            BUT you can be friends, you can play games together, do crimes together :) and etc.\n"
   +"            be sure goose won't let you be alone, it will show you memes and talk to you even\n"
   +"            when you are not playing games, but if you close memes, it will get angry and steals\n"
   +"            your mouse. if it gets bored, it will steal your mouse for fun")
   print(Fore.MAGENTA+"\n\n            i'm not respondibale if the goose rickrolls you or tries to kill someone!")
   print(Back.BLUE+Fore.YELLOW+"\n\n\n            after all of this, Do you want to keep the goose? [Y/n] :")

   ans=getin()
   if ans==False:
      print(Back.BLACK+Fore.RED+Style.BRIGHT+"\n           are you sure you don't want the goose? you shuld give it a try [y:bye/n:ok] :")
      if getin()==True : 
         print ("\n\n            hoooonks !")
         time.sleep(4)
         quit()
      
      
def downgoose(): #download goose
   print(Style.RESET_ALL+Fore.LIGHTGREEN_EX+"\n\n        OK, let me download the goose")
   req=requests.get(gooseurl)
   if req.status_code!=200 :
      print(Fore.MAGENTA+'\n         it seems like you have some internet problems. check your internet connection'
      +'\n         and make sure you can connect to \"github.com\" ')
      print('do yo want to try again?[y/n] :')
      if getin()== False:
         print('\n\nsee you soon!');time.sleep(3);quit()
      downgoose()
      return True
   
   goosezip=zipfile.ZipFile(BytesIO(req.content))
   goosezip.extractall(path=os.getenv('appdata'))

def addgose(): #add goose to registry and start menu and...
   
   #adding goose to registry and control panel
   with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,softreg) as gkey: 

      for greg in goosereg:
         winreg.SetValueEx(gkey,greg,0,winreg.REG_SZ,goosereg.get(greg))
   
   #adding goose to start menu
   if not os.path.exists(startmenupath) :
      os.mkdir(startmenupath)
   for cutpath in goosecut:
      cut=Dispatch('WScript.Shell').CreateShortCut(
         startmenupath+re.split(r'\.',cutpath)[0]+'lnk')
      cut.Targetpath=os.path.join(goosepath,cutpath)
      cut.save()

   #adding goose to startup
   with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,runreg) as rreg:
      winreg.SetValueEx(rreg,'DesktopGoose',0,winreg.REG_SZ,goosereg.get('DisplayIcon'))
   
def finalinfo():
   print(Style.RESET_ALL+Fore.LIGHTGREEN_EX+'\n\n\n'+
   '        goose\'s got installed in your computer. now I\'ll open a page that will help you'+
   '        press enter...')
   input()
   quit()




#defines
startmenupath=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\DesktopGoose"
gooseurl='https://github.com/tsalehm/DesktopGoose/archive/refs/heads/main.zip'
goosepath=os.path.expandvars(r'%appdata%\DesktopGoose-main')
softreg=r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\DesktopGoose'
runreg='SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
goosereg={
   'DisplayName':'DesktopGoose',
   'DisplayVersion':'0.3',
   'UninstallString':os.path.join(goosepath,'uninstall.exe'),
   'InstallLocation':goosepath,
   'Publisher':'tsalehm',
   'DisplayIcon':os.path.join(goosepath,'DesktopGoose.exe'),
   'URLInfoAbout':'https://github.com/tsalehm/DesktopGoose',
}
goosecut=['DesktopGoose.exe','about goose.txt','uninstall.exe']
startupath=os.path.expandvars(r'%appdata%\Microsoft\Windows\Start Menu\Programs\Startup')

#start
showgoose();
print_info()
downgoose()
addgose()
finalinfo()


