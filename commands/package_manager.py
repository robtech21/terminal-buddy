import os

def install(package):
    print("Installing...")
    os.system(f"sudo apt install {package}")

def search(keyword):
    print("Searching...")
    os.system(f"sudo apt search {keyword}")

def update():
    print("Updating package database...")
    os.system("sudo apt update")

def upgrade():
    print("Upgrading packages")
    os.system("sudo apt upgrade")

def remove(package):
    print("Removing...")
    os.system(f"sudo apt remove {package}")