#!/bin/python
import shutil

ROOT_PATH="/home/volga/00_repos/05_bbBuildroot/"
BUILDROOT_PATH="/home/volga/00_repos/05_bbBuildroot/buildroot-2024.02.10/"

print("Main buildroot config coppied to buildroot path")
shutil.copy2("./.config", BUILDROOT_PATH)

shutil.copy2("./.deploy.sh", ROOT_PATH)
print("Deploy script copied to the ROOT  work path")