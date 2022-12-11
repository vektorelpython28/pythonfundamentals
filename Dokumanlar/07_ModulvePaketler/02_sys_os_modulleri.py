import sys,os
print(os.name) # posix,nt
import platform
print(platform.platform()) #Linux-5.15.0-47-generic-x86_64-with-glibc2.29
print(*sys.path,sep="\n")
"""
/workspace/pythonfundamentals/Dokumanlar/07_ModulvePaketler
/home/gitpod/.pyenv/versions/3.8.13/lib/python38.zip
/home/gitpod/.pyenv/versions/3.8.13/lib/python3.8
/home/gitpod/.pyenv/versions/3.8.13/lib/python3.8/lib-dynload
/workspace/pythonfundamentals/env/lib/python3.8/site-packages
"""
