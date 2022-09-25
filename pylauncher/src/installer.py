import re
import os
import sys
import shutil
import winreg
import climage
import zipfile
import requests
import webbrowser
from time import sleep
from io import BytesIO
from github import Github
from subprocess import PIPE, call
from win32com.client import Dispatch
from colorama import init, Style, Fore


# info
startmenupath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\DesktopGoose"
goosepath = os.path.expandvars(r'%appdata%\DesktopGoose')
softreg = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\DesktopGoose'
runreg = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
goosereg = {
   'DisplayName': 'DesktopGoose',
   'DisplayVersion': '0.3',
   'UninstallString': os.path.join(goosepath, 'uninstall.exe'),
   'InstallLocation': goosepath,
   'Publisher': 'tsalehm',
   'DisplayIcon': os.path.join(goosepath, 'DesktopGoose.exe'),
   'URLInfoAbout': 'https://github.com/tsalehm/DesktopGoose',
}
goosecut = ['DesktopGoose.exe', 'about goose.html', 'uninstall.exe']


# functions
def resource_path(relative_path):  # get gooseicon.png path in exe file (pyinstaller)

   # return os.path.join(os.getcwd(), relative_path)
   try:
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")

   return os.path.join(base_path, relative_path)


def getin():  # get 'y' or 'n'

   while True:
      inp = input()
      if re.match(r"[nN]", inp): return False
      elif re.match(r"[yY]", inp): return True
      else: print("\n i didn't understand you. please answer with [y] or [n] :")


def down_latestgoose():  # shuld i say anything ?

   rpo = Github().get_repo('tsalehm/DesktopGoose')
   rls = rpo.get_latest_release().tag_name
   gooseurl = ('https://github.com/tsalehm/DesktopGoose/archive/refs/tags/'
               + rls
               + '.zip')
   req = requests.get(gooseurl)

   call(resource_path('closegoose.bat'), shell=False, stdout=PIPE, stderr=False)

   if os.path.exists(goosepath): shutil.rmtree(goosepath)
   goosezip = zipfile.ZipFile(BytesIO(req.content))
   goosezip.extractall(os.getenv('appdata'))
   os.rename(os.path.expandvars('%appdata%\\' + 'DesktopGoose-' + rls), goosepath)


# main
def main():

   # show goose's picture
   print('\n\n')
   os.system('')
   print(climage.convert(filename=resource_path('gooseicon.png'), is_unicode=True))
   print('\n')

   # print goose's info

   init()
   tsize = shutil.get_terminal_size()
   print(Style.BRIGHT + Fore.GREEN + "Desktop Goose".center(tsize[0]))
   print(Fore.CYAN + "\n\n            this is DesktopGoose, a goose for your desktop\n"
         + "            It will be your desktop pet, walks everywhere, poops everywhere, and you can't stop it\n"
         + "            if you annoy it, honks and steals your mouse, our goose is really rude and loves crime\n"
         + "            BUT you can be friends, you can play games together, do crimes together :) and etc.\n"
         + "            be sure goose won't let you be alone; it will show you memes and talk to you even\n"
         + "            when you are not playing games, but if you close memes, it will get angry and steals\n"
         + "            your mouse. if it gets bored, it will steal your mouse for fun")
   print(Fore.MAGENTA + "\n\n         I'm not responsible if the goose rickrolls you or tries to kill someone!")
   print(Fore.YELLOW + "\n\n\n            after all of this, Do you want to keep the goose? [Y/n] :")

   # ask the user about installing goose
   if getin() is False:
      print(Fore.RED + Style.BRIGHT + "\n            are you sure you don't want the goose?"
            + "            you should give it a try [y:bye/n:ok] :")
      if getin() is True:
         print("\n\n            hoooonks !")
         sleep(4)
         quit()

   print(Style.RESET_ALL + Fore.LIGHTGREEN_EX + "\n\n         OK, let me download the goose")

   while True:
      try:
         down_latestgoose()
         break
      except Exception:
         print(Fore.MAGENTA + '\n         it seems like you have some internet problems. check your internet connection'
               + '\n         and make sure you can connect to \"github.com\" ')
         print('         do yo want to try again?[y/n] :')
         if getin() is False:
            print('\n\n         see you soon!'); sleep(3); quit()

   # adding goose to registry and control panel
   with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, softreg) as gkey:

      for greg in goosereg:
         winreg.SetValueEx(gkey, greg, 0, winreg.REG_SZ, goosereg.get(greg))

   # adding goose to start menu
   if not os.path.exists(startmenupath):
      os.mkdir(startmenupath)
   for cutpath in goosecut:
      cut = Dispatch('WScript.Shell').CreateShortCut(os.path.join(
         startmenupath, re.split(r'\.', cutpath)[0] + '.lnk'))
      cut.Targetpath = os.path.join(goosepath, cutpath)
      cut.save()

   # adding goose to startup
   with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, runreg) as rreg:
      winreg.SetValueEx(rreg, 'DesktopGoose', 0, winreg.REG_SZ, goosereg.get('DisplayIcon'))

   webbrowser.open("https://github.com/tsalehm/DesktopGoose", 1)
   call(resource_path("opengoose.bat"), shell=False)


if __name__ == "__main__":  # don't run codes if file was imported
   main()
 #NO VPN