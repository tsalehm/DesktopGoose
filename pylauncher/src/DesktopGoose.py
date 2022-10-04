import re
import os
import sys
import pyvda
import psutil
import shutil
import win32gui
import subprocess
from github import Github
from keyboard import press
from time import sleep, time
from packaging import version
from installer import resource_path, goosepath


# info
versionpath = os.path.expandvars(r'%appdata%\DesktopGoose\pylauncher\files\version.txt')
thegoosepath = os.path.join(goosepath, 'GooseDesktop.exe')


# functions
def check_for_updates():

   rpo = Github().get_repo('tsalehm/DesktopGoose')
   with open() as vrs:
      thevrs = vrs.readline()
   if version.parse(rpo.get_latest_release().tag_name()) > version.parse(thevrs): return True
   return False


def do_the_update():

   if os.path.exists(os.path.expandvars(r'%appdata%\.gupdate')):
      shutil.rmtree(os.path.expandvars(r'%appdata%\.gupdate'))
   os.mkdir(os.path.expandvars(r'%appdata%\.gupdate'))
   shutil.copy(os.path.expandvars(r'%appdata%\DesktopGoose\pylauncher\build\update.exe'),
               os.path.expandvars(r'%appdata%\.update\update.exe'))

   subprocess.call(resource_path('update.bat'), shell=False, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
   sys.exit()


def getShell():  # get apps hwnd
   thelist = []

   def findit(hwnd, ctx):
      thelist.append(hwnd)
   win32gui.EnumWindows(findit, None)
   return thelist


def opengoose():  # open goose and find its hwnd
   first_hd = getShell()
   subprocess.Popen(thegoosepath, shell=False)
   f_time = time()
   sleep(0.5)
   while 'pinobj' not in locals() and time() - f_time <= 20:
      modshell = getShell()
      for mod in modshell:
         if re.search("Mod Enabler Warning", win32gui.GetWindowText(mod)):
            try:
               pinobj = pyvda.AppView(hwnd=mod)
               pinobj.switch_to()
               pinobj.set_focus()
               pinobj.pin()
            except Exception:
               pass
   press('enter')
   sleep(1)  # wait for goose to fully open
   sec_hd = getShell()
   dif_hd = [element for element in sec_hd if element not in first_hd]

# pin goose to all desktops
   for honk in dif_hd:
      try:
         if win32gui.GetWindowText(honk) == '':  # goose's main process is named ''
            tsk = pyvda.AppView(hwnd=honk)
            tsk.pin()
      except Exception:  # if a process with name '' cannot get pinned
         pass


# main
try:
   if check_for_updates(): do_the_update()
except Exception:
   pass

opengoose()

# look for goose's memes and pin them untill the app gets closed
while True:
   memeshell = getShell()
   for meme in memeshell:

      if re.search("Goose \"Not-epad\"|^$", win32gui.GetWindowText(meme)) and meme > 0:
         # memes are names with 'Goose "Not-epad"' and ''
         try:
            memeobj = pyvda.AppView(hwnd=meme)
            if not memeobj.is_pinned(): memeobj.pin()
         except Exception:  # if a process with name '' cannot get pinned
            pass

   sleep(1)
   if "GooseDesktop.exe" not in (i.name() for i in psutil.process_iter()):
      sys.exit()  # close launcher if goose's got closed
