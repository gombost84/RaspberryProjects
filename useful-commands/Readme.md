# Setup, Update and Maintenance

sudo apt update &&sudo apt full-upgrade

sudo rpi-update

sudo reboot

## Firewall setup:

sudo apt install ufw

sudo ufw allow 22

sudo ufw allow OpenSSH

sudo ufw allow vnc

sudo ufw enable

## Docker

https://docs.docker.com/engine/install/raspberry-pi-os/

### Docker Local Registry

https://www.docker.com/blog/how-to-use-your-own-registry-2/

## K3S

https://docs.k3s.io/quick-start

## Useful Aliases

alias temp='/usr/bin/vcgencmd measure_temp'

alias ll='ls -la'

alias .="cd .."

alias ..="cd ../.."

alias ...="cd ../../.."

alias h="history"

alias h1="history 10"

alias h2="history 20"

alias h3="history 30"

alias hgrep='history | grep'


