#!/usr/bin/python3.10

import subprocess
import os
import sys
import time

####Global variables####

HOME = os.getenv("HOME", default=None)
DNF_INSTALL='sudo dnf install -y {}'
CONFIG_SSH='git@github.com:avGenie/linux-config.git'
CONFIG_HTTPS='https://github.com/avGenie/linux-config.git'
CONFIG_FOLDER='linux-config'
LAUNCH_FOLDER=os.getcwd()

####End global variables####

def get_installed_packages() -> list:
    packages = subprocess.check_output(['rpm', '-qa']).decode('utf-8')
    return packages.split('\n')

def install_git():
    installed_packages = get_installed_packages()
    installed_git = [rec for rec in installed_packages if 'git-' in rec]
    if not installed_git:
        print(os.system(DNF_INSTALL.format('git')))
        ret_status = True
    else:
        print('git has been installed')


def create_git_key():
    print(os.system('ssh-keygen -t ed25519 -C "aleksandr-generalov19@yandex.ru"'))
    print(os.system('ssh-add ~/.ssh/id_ed25519'))
    pub_key_file_path = HOME + '/.ssh/id_ed25519.pub'

    with open(pub_key_file_path) as file:
        pub_key = file.read().rstrip()
        print('Copy this public ssh key to the git keys repo')
        print(pub_key)

        input('Press Enter to continue...')


def create_git_credentials():
    print(os.system('git config --global user.name avGenie'))
    print(os.system('git config --global user.email aleksandr-generalov19@yandex.ru'))


def git_clone():
    git_clone_command='git clone {}'.format(CONFIG_HTTPS)
    print(os.system(git_clone_command))


def enter_config_folder(): 
    new_dir = LAUNCH_FOLDER + '/' + CONFIG_FOLDER
    os.chdir(new_dir)


def set_up_vim_config():
    vimrc_home_path = HOME + '/' + '.vimrc'
    cp_command = 'cp .vimrc {}'.format(HOME)
    print(os.system(cp_command))
    print(os.system('chmod 755 {}'.format(vimrc_home_path)))
    print(os.system('~/.vimrc'))

    ## Install Vundle
    print(os.system('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim'))
    print(os.system('vim +PluginInstall +qall'))


def set_up_zsh():
    print(os.system(DNF_INSTALL.format('zsh')))
    print(os.system('sudo chsh -s /bin/zsh alexander'))

    vimrc_home_path = HOME + '/' + '.zshrc'
    cp_command = 'cp .zshrc {}'.format(HOME)
    print(os.system(cp_command))
    print(os.system('chmod 755 {}'.format(vimrc_home_path)))

    ohmyzsh_home_path = HOME + '/' + '.oh-my-zsh'
    mkdir_command = 'mkdir {}/.oh-my-zsh'.format(HOME)
    print(os.system(mkdir_command))

    new_dir = LAUNCH_FOLDER + '/' + CONFIG_FOLDER + '/oh_my_zsh'
    os.chdir(new_dir)
    cp_command = 'cp -R . {}'.format(ohmyzsh_home_path)
    print(os.system(cp_command))

    print(os.system('chmod 775 -R {}'.format(ohmyzsh_home_path)))


def install_common_apps():
    print(os.system(DNF_INSTALL.format('cmake')))
    print(os.system('sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc'))
    print(os.system('printf "[vscode]\nname=packages.microsoft.com\nbaseurl=https://packages.microsoft.com/yumrepos/vscode/\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc\nmetadata_expire=1h" | sudo tee -a /etc/yum.repos.d/vscode.repo'))
    print(os.system('sudo dnf install code -y'))
    print(os.system(DNF_INSTALL.format('qt-devel qtcreator')))


def install_packets() -> int:
    ## Installation git
    #install_git()
    #create_git_key()
    #create_git_credentials()
    #git_clone()
    enter_config_folder()
    #set_up_vim_config()
    #set_up_zsh()
    install_common_apps()

    ## Installation



if __name__ == '__main__':
    install_packets()
