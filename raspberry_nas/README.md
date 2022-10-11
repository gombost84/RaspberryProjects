# How To Use a Raspberry Pi as a Cheap NAS

## Intro

I created this guide because I couldn't find one out there that had all the information needed to properly set up the Pi as a NAS.  
Most of them work if you have the time and will to do your own experimenting but sometimes you just need and end-to-end guide and be done with it.  
This one is intended to be just that.  

## Before You Start

I trust, you know what you're doing. The commands in this guide were tested and they do work but it's up to you to create backups and make sure your Pi and other hardware is not damaged.  
The first time I was doing it, I messed up and the Pi wouldn't even boot. I had to reinstall the OS. So, be careful. Don't just copy paste everything, think about your own setup. But this applies to everything on the internet.  

### Basic Security

I'm not going to get into the security side of any of this. But before you start you should, at the very least, create a sudo user and disable the default one.  

### What You Need

- Raspberry Pi (I use a Pi 4 Model B)
- an external Hard Drive
- another computer on the same network to test things

I'm using PuTTY on a Windows machine to connect to the Pi over SSH but since the commands are run on the Pi, this should be the same on every operating system once you SSH in.  

Or you can just do it directly on the machine.  

### Preparing the Pi

Make sure that all your packages are up to date. Run the following command:  

    sudo apt update && sudo apt full-upgrade
 

### Creating a New User and Group

---
**NOTE**

You can use any existing user but it's better to separate this from everything else. In that case, you can skip this section.  

--- 

Now we create a new user and add it to a new group. This user will be used only to access the mounted drive.  

    sudo useradd nas

I named it *nas* so it's always obvious at first glance.  

Now create a password for the user:  

    sudo passwd nas

You are asked to type and re-type the password.  

Now create a group:  

    sudo groupadd nasusers

And add the user to this group:  

    sudo usermod -a -G nasusers nas

### Mounting the Drive

Connect your external drive if you haven't already. Then run the following command:  

    sudo fdisk -l

You might see a bunch of information but we're only interested at the end, see the marked part on the screenshot below.  

![fdisk output](/screens/fdisk.PNG)

That's where your drive resides. Now, we have to mount it. But for that, we need to create a folder with the following command:  

    sudo mkdir /media/USBHDD

Now we need to find out the *nasusers* group's ID:  

    grep nasusers /etc/group

Mine looks like this:  

    nasusers:x:1003:nas

Where the ID is *1003*.