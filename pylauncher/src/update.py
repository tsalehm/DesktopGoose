import os
import shutil
import zipfile
from io import BytesIO
from requests import get
from github import Github
from packaging.version import parse
from subprocess import DEVNULL, Popen
from installer import resource_path, down_latestgoose


def updategoose():  # update goose from "added.zip" file without removing user assets
   goosezip = zipfile.ZipFile(BytesIO(get(
      r"https://github.com/tsalehm/DesktopGoose/releases/download/" + tag + r"/added.zip").content))
   goosezip.extractall(os.path.expandvars(r"%appdata%\added"))
   shutil.copytree(os.path.expandvars(r"%appdata%\added"), dirs_exist_ok=True)
   shutil.rmtree(os.path.expandvars(r"%appdata%\added"))


repo = Github().get_repo("tsalehm/DesktopGoose")
tag = repo.get_latest_release().tag_name  # get latest release tag name

with open(os.path.expandvars(r"%appdata%\DesktopGoose\pylauncher\files\version.txt", "r")) as vers:
   if parse(vers.readline).major != parse(tag).major:
      down_latestgoose()  # if major version has been changed, download whole goose again
   else:
      updategoose()  # or just update some files

Popen(resource_path('opengoose.bat'), shell=False, stdout=DEVNULL, stderr=DEVNULL)
