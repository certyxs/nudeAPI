import subprocess
import sys
import os
import platform
import time

try:
    from pystyle import Colorate, Colors
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pystyle", "--upgrade"])
    from pystyle import Colorate, Colors

REQUIRED_PACKAGES = [
    "nudeAPI",
    "uvicorn",
    "requests",
]

def print_header():
    header = """

                           /$$            /$$$$$$  /$$$$$$$  /$$$$$$
                          | $$           /$$__  $$| $$__  $$|_  $$_/
 /$$$$$$$  /$$   /$$  /$$$$$$$  /$$$$$$ | $$  \\ $$| $$  \\ $$  | $$  
| $$__  $$| $$  | $$ /$$__  $$ /$$__  $$| $$$$$$$$| $$$$$$$/  | $$  
| $$  \\ $$| $$  | $$| $$  | $$| $$$$$$$$| $$__  $$| $$____/   | $$  
| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$  | $$| $$        | $$  
| $$  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$       /$$$$$$
|__/  |__/ \\______/  \\_______/ \\_______/|__/  |__/|__/      |______/
                                                                    

"""
    print(Colorate.Horizontal(Colors.blue_to_cyan, header))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_pip():
    print(Colorate.Horizontal(Colors.yellow, "[*] Checking pip availability..."))
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(Colorate.Horizontal(Colors.green, "[+] pip is available.\n"))
    except subprocess.CalledProcessError:
        print(Colorate.Horizontal(Colors.red, "[!] pip not found. Please install pip before proceeding."))
        sys.exit(1)

def create_venv():
    venv_dir = "venv"
    if os.path.isdir(venv_dir):
        print(Colorate.Horizontal(Colors.cyan, f"[*] Virtual environment '{venv_dir}' already exists.\n"))
        return
    print(Colorate.Horizontal(Colors.yellow, "[*] Creating virtual environment..."))
    try:
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
        print(Colorate.Horizontal(Colors.green, f"[+] Virtual environment '{venv_dir}' created.\n"))
    except subprocess.CalledProcessError:
        print(Colorate.Horizontal(Colors.red, "[!] Failed to create virtual environment.\n"))
        sys.exit(1)

def get_venv_python():
    if platform.system() == "Windows":
        return os.path.join("venv", "Scripts", "python.exe")
    else:
        return os.path.join("venv", "bin", "python")

def upgrade_venv_pip(venv_python):
    print(Colorate.Horizontal(Colors.yellow, "[*] Upgrading pip inside virtual environment..."))
    try:
        subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
        print(Colorate.Horizontal(Colors.green, "[+] pip upgraded inside virtual environment.\n"))
    except subprocess.CalledProcessError:
        print(Colorate.Horizontal(Colors.red, "[!] Failed to upgrade pip inside virtual environment.\n"))

def activate_venv_instruction():
    print(Colorate.Horizontal(Colors.cyan, "[*] To activate the virtual environment:"))
    if platform.system() == "Windows":
        print(Colorate.Horizontal(Colors.white, r"    .\venv\Scripts\activate"))
    else:
        print(Colorate.Horizontal(Colors.white, "    source ./venv/bin/activate"))
    print()

def install_package(venv_python, package):
    print(Colorate.Horizontal(Colors.yellow, f"[*] Installing {package}..."))
    try:
        subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", package])
        print(Colorate.Horizontal(Colors.green, f"[+] {package} installed successfully.\n"))
        return True
    except subprocess.CalledProcessError:
        print(Colorate.Horizontal(Colors.red, f"[!] Failed to install {package}.\n"))
        return False

def check_and_install():
    venv_python = get_venv_python()
    installed = []
    failed = []
    for package in REQUIRED_PACKAGES:
        try:
            # system python
            __import__(package)
            print(Colorate.Horizontal(Colors.green, f"[+] {package} already installed globally."))
            installed.append(package)
        except ImportError:
            # ENV VIRTUAL
            if install_package(venv_python, package):
                installed.append(package)
            else:
                failed.append(package)
    return installed, failed

def main():
    print_header()
    check_pip()
    create_venv()
    venv_python = get_venv_python()
    upgrade_venv_pip(venv_python)
    activate_venv_instruction()

    print(Colorate.Horizontal(Colors.cyan, "[*] Installing required packages...\n"))
    installed, failed = check_and_install()

    print()
    print(Colorate.Horizontal(Colors.blue, "Installation Summary:"))
    print(Colorate.Horizontal(Colors.green, f"  Successfully installed or found: {', '.join(installed) if installed else 'None'}"))
    if failed:
        print(Colorate.Horizontal(Colors.red, f"  Failed to install: {', '.join(failed)}"))
    else:
        print(Colorate.Horizontal(Colors.green, "  All packages installed successfully!"))

    print()
    print(Colorate.Horizontal(Colors.yellow, "You can now run your nudeAPI app with:"))
    print(Colorate.Horizontal(Colors.white, f"  {venv_python} -m uvicorn my_api:app --reload"))
    print()

    time.sleep(3)
    clear_console()

if __name__ == "__main__":
    main()
