#!/bin/python
import shutil

#w1Destination = "/home/volga/00_repos/07_SH_Kernel_T_reader/sh_temperature_reader/linux-6.6.68/drivers/w1/masters/"
#w1Source = "/home/volga/00_repos/05_bbBuildroot/buildroot-2024.02.10/output/build/linux-6.6.68/drivers/w1/masters/"

#w1Files = ["Makefile", "Kconfig", "sh_t_reader.c"]

#for file in w1Files:
#    shutil.copy2(w1Source + file, w1Destination)

GIT_PATH="/home/volga/00_repos/07_SH_Kernel_T_reader/sh_temperature_reader/"

BUILDROOT_SRC="./buildroot-2024.02.10/"
CONFIG_SRC=".config"
LINUX_KERNEL_KONFIG="./buildroot-2024.02.10/output/build/linux-6.6.68/arch/arm/configs/omap2plus_defconfig"
IMAGES_DIR="output/images/"

print("Copy config")
shutil.copy2(BUILDROOT_SRC + CONFIG_SRC, GIT_PATH)

shutil.copy2("deploy.sh", GIT_PATH)
print("deploy script coppied to the repo")

shutil.copy2(BUILDROOT_SRC + IMAGES_DIR + "extlinux.conf", GIT_PATH + IMAGES_DIR)
print("extlinux.conf coppied to the repo")

shutil.copy2("./copy.py", GIT_PATH)
print("copy.py coppied to the repo")