import os

def install_with_apt(program):
    print("Installing...")
    os.system(f"sudo apt install {program}")

def search_with_apt(keyword):
    print("Searching...")
    os.system(f"sudo apt search {keyword}")

def update_apt_database():
    print("Updating package database...")
    os.system("sudo apt update")

def upgrade_packages():
    print("Upgrading packages")
    os.system("sudo apt upgrade")

def
