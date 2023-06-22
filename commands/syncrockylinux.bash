#!/bin/bash

export DL_PATH=/data
dnf -y update 
dnf -y install epel-release
rpm -import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-9

ln -s /repos/yum.repos.d/*.repo /etc/yum.repos.d/

dnf reposync --norepopath --download-metadata --downloadcomps --download-path $DL_PATH/appstream8 -n  --repoid appstream8 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/devel -n  --repoid rocky8_devel 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/baseos -n  --repoid rocky8_baseos 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/powertools -n  --repoid rocky8_powertools 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/epel -n  --repoid rocky8_epel 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/extras -n  --repoid rocky8_extras 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/plus -n  --repoid rocky8_plus 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/highavailability -n  --repoid rocky8_highavailability 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/rpmfusion-free-updates -n  --repoid rocky8_rpmfusion-free-updates 
dnf reposync --norepopath --download-path $DL_PATH/rockylinux/8/x86_64/rpmfusion-nonfree-updates -n  --repoid rocky8_rpmfusion-nonfree-updates
