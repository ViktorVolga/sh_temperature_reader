#!/bin/bash

bootDestination="/media/volga/boot"
Source="/home/volga/00_repos/05_bbBuildroot/buildroot-2024.02.10/output/images"
rootDestination="/media/volga/root"


rm -rf ${bootDestination}/* 
rm -rf ${rootDestination}/* 

cp ${Source}/MLO ${Source}/u-boot.img ${Source}/zImage /home/volga/00_repos/05_bbBuildroot/buildroot-2024.02.10/output/build/linux-6.6.68/arch/arm/boot/dts/ti/omap/am335x-boneblack.dtb ${bootDestination}/
mkdir ${bootDestination}/extlinux
cp ${Source}/extlinux.conf ${bootDestination}/extlinux/

tar -C /media/volga/root/ -xf ${Source}/rootfs.tar
