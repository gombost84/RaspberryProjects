# How To Use a Raspberry Pi as a Cheap NAS

## Intro

I created this guide because I couldn't find one out there that had all the information needed to properly set up the Pi as a NAS.  
Most of them work if you have the time and will to do your own experimenting but sometimes you just need and end-to-end guide and be done with it.  
This one is intended to be just that.

## Before You Start

I trust, you know what you're doing. The commands in this guide were tested and they do work but it's up to you to create backups and make sure your Pi is not damaged.

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

