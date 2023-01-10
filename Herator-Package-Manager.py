
# Import os
import os

# Warnings
print("IMPORTANAT: IF YOUR HPM CHRASHES HERE, RUN: pip install colorama     ")
print("NOTE: You may need to install pip depending on your distro")
print("Apt/Debian/Ubuntu: sudo apt install pip      Dnf/Redhap/Fedora: sudo dnf install pip      Pacman/Arch/Manjaro: sudo pacman -S python-pip")

# Import Colorama
from colorama import Fore, Style

# Var
Spacer = "=-" * 40
Package = "neofetch"
Method = "pacman"
Distro = "arch"

# ================================================
Version = "v1.4.1"
# ================================================

# DEF
def InstallSinglePackage():
    
    # Set Package
    global Package
    # Set Install Method
    global Method
    # Set Distro For Compatibility Mode
    global Distro
    # Set Operation
    global Operation
    # Set Spacer
    global Spacer  

    # Install
    if Operation == "Install":

        # Print Notice
        print(Spacer)
        print("Installing " + Package)

        # Confirmation
        Option = str(input("Is This Correct? y:N   >>>"))
        Option = Option.lower()

        # Install
        if Option in ["yes", "y", "yeah", "yea"]:
            
            # Apt Install
            if Distro == "debian/ubuntu":
                print(Spacer)
                print("| 1 | - Apt")
                print("| 2 | - Snap")
                print("| 3 | - Flatpak")
                print("| - | - .DEB NOT SURPORTED")
                print(Spacer)
                print("| UNOFICIAL DEBIAN/UBUNTU SURPORT")
                print(Spacer)
                Option = str(input(">>>"))
                
                if Option in ["1"]:
                    os.system("apt install " + Package)
                elif Option in ["2"]:
                    os.system("snap install " + Package)
                elif Option in ["3"]:
                    os.system("flatpak install " + Package)

            # Dnf Install
            if Distro == "redhat/fedora":
                print(Spacer)
                print("| 1 | - Dnf")
                print("| 2 | - Snap")
                print("| 3 | - Flatpak")
                print("| - | - .RPM NOT SURPORTED")
                print(Spacer)
                print("| UNOFICIAL REDHAT/FEDORA SURPORT")
                print(Spacer)
                Option = str(input(">>>"))
                
                if Option in ["1"]:
                    os.system("dnf install " + Package)
                elif Option in ["2"]:
                    os.system("snap install " + Package)
                elif Option in ["3"]:
                    os.system("flatpak install " + Package)

            # Pacman / Yay Install
            if Distro == "arch":
                # Pacman Install
                if Method == "pacman":
                    os.system("sudo pacman -S " + Package)
                # Yay Install
                elif Method == "yay":
                    os.system("yay " + Package)
                # Flatpak Install
                elif Method == "flatpak":
                    os.system("flatpak install " + Package)
                # Snap Install
                elif Method == "snap":
                    os.system("snap install " + Package)
                # Pip Install
                elif Method == "pip":

                    print("Install Pip?")
                    print("Why? Pip is not pre-installed on some distros and this current install wont work without it. If you know you installed it say No")
                    Option = str(input("Y:n     >>>"))
                    Option = Option.lower()

                    if Option in ["y", "yes", "yeah", "ye", "yea"]:
                        os.system("sudo pacman -S python-pip")

                    os.system("pip install " + Package)
            
            # Unreconised Install
            else:
                print("Unrecconised Method/Distro")

            # Print Notice
            print("Installed " + Package)
        
        # Cancel
        else:
            print("Installation Of " + Package + " Cancelled")

        # Spacer
        print(Spacer)
    
    # Remove
    elif Operation == "Remove":

        # Print Notice
        print(Spacer)
        print("Removing " + Package)

        # Confirmation
        Option = str(input("Is This Correct? y:N   >>>"))
        Option = Option.lower()

        # Remove
        if Option in ["yes", "y", "yeah", "yea"]:
            
            # Apt Remove
            if Distro == "debian/ubuntu":
                print(Spacer)
                print("| 1 | - Apt")
                print("| 2 | - Snap")
                print("| 3 | - Flatpak")
                print("| - | - .DEB NOT SURPORTED")
                print(Spacer)
                print("| UNOFICIAL DEBIAN/UBUNTU SURPORT")
                print(Spacer)
                Option = str(input(">>>"))
                
                if Option in ["1"]:
                    os.system("apt remove " + Package)
                elif Option in ["2"]:
                    os.system("snap remove " + Package)
                elif Option in ["3"]:
                    os.system("flatpak remove " + Package)

            # Dnf Remove
            if Distro == "redhat/fedora":
                print(Spacer)
                print("| 1 | - Dnf")
                print("| 2 | - Snap")
                print("| 3 | - Flatpak")
                print("| - | - .RPM NOT SURPORTED")
                print(Spacer)
                print("| UNOFICIAL REDHAT/FEDORA SURPORT")
                print(Spacer)
                Option = str(input(">>>"))
                
                if Option in ["1"]:
                    os.system("dnf remove " + Package)
                elif Option in ["2"]:
                    os.system("snap remove " + Package)
                elif Option in ["3"]:
                    os.system("flatpak remove " + Package)

            # Pacman / Yay Remove
            if Distro == "arch":
                # Pacman Remove
                if Method == "pacman":
                    os.system("sudo pacman -R " + Package)
                # Yay Remove
                elif Method == "yay":
                    os.system("yay -R " + Package)
                # Flatpak Remove
                elif Method == "flatpak":
                    os.system("flatpak remove " + Package)
                # Snap Remove
                elif Method == "snap":
                    os.system("snap remove " + Package)
                # Pip Remove
                elif Method == "pip":

                    print("Install Pip?")
                    print("Why? Pip is not pre-installed on some distros and this current uninstall wont work without it. If you know you installed it say No")
                    Option = str(input("Y:n     >>>"))
                    Option = Option.lower()

                    if Option in ["y", "yes", "yeah", "ye", "yea"]:
                        os.system("sudo pacman -S python-pip")

                    os.system("pip remove " + Package)
            
            # Unreconised Uninstall
            else:
                print("Unrecconised Method/Distro")

            # Print Notice
            print("Removed " + Package)
        
        # Cancel
        else:
            print("Remove Of " + Package + " Cancelled")

        # Spacer
        print(Spacer)

    else:
        print("ERROR: Cant decide to install or uninstall - Unrecognised Operation")

def Logo():
    print(Style.BRIGHT + Spacer)
    print(Fore.LIGHTCYAN_EX + r"      ___      " + Fore.LIGHTMAGENTA_EX + r"     ___      " + Fore.LIGHTGREEN_EX + r"     ___      ")
    print(Fore.LIGHTCYAN_EX + r"     /\__\     " + Fore.LIGHTMAGENTA_EX + r"    /\  \     " + Fore.LIGHTGREEN_EX + r"    /\__\     ")
    print(Fore.LIGHTCYAN_EX + r"    /:/  /     " + Fore.LIGHTMAGENTA_EX + r"   /::\  \    " + Fore.LIGHTGREEN_EX + r"   /::|  |    ")
    print(Fore.LIGHTCYAN_EX + r"   /:/__/      " + Fore.LIGHTMAGENTA_EX + r"  /:/\:\  \   " + Fore.LIGHTGREEN_EX + r"  /:|:|  |    ")
    print(Fore.LIGHTCYAN_EX + r"  /::\  \ ___  " + Fore.LIGHTMAGENTA_EX + r" /::\~\:\  \  " + Fore.LIGHTGREEN_EX + r" /:/|:|__|__  ")
    print(Fore.LIGHTCYAN_EX + r" /:/\:\  /\__\ " + Fore.LIGHTMAGENTA_EX + r"/:/\:\ \:\__\ " + Fore.LIGHTGREEN_EX + r"/:/ |::::\__\ ")
    print(Fore.LIGHTCYAN_EX + r" \/__\:\/:/  / " + Fore.LIGHTMAGENTA_EX + r"\/__\:\/:/  / " + Fore.LIGHTGREEN_EX + r"\/__/~~/:/  / ")
    print(Fore.LIGHTCYAN_EX + r"      \::/  /  " + Fore.LIGHTMAGENTA_EX + r"     \::/  /  " + Fore.LIGHTGREEN_EX + r"      /:/  /  ")
    print(Fore.LIGHTCYAN_EX + r"      /:/  /   " + Fore.LIGHTMAGENTA_EX + r"      \/__/   " + Fore.LIGHTGREEN_EX + r"     /:/  /   ")
    print(Fore.LIGHTCYAN_EX + r"     /:/  /    " + Fore.LIGHTMAGENTA_EX + r"              " + Fore.LIGHTGREEN_EX + r"    /:/  /    ")
    print(Fore.LIGHTCYAN_EX + r"     \/__/     " + Fore.LIGHTMAGENTA_EX + r"              " + Fore.LIGHTGREEN_EX + r"    \/__/     ")
    print(Style.RESET_ALL + Style.BRIGHT + Spacer)


# App Def
if True:

    # Gaming
    if True:
        # Steam
        def Steam():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "steam"
            Method = "pacman"

            # Installer
            InstallSinglePackage()
        
        # Lutris
        def Lutris():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "lutris"
            Method = "pacman"

            # Installer
            InstallSinglePackage()
        
        # Discord
        def Discord():
            
            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "discord"
            Method = "pacman"

            # Installer
            InstallSinglePackage()
        
        # Gaming
        def Gaming():
        
            # Steam
            Steam()
            # Lutris
            Lutris()
            # Discord
            Discord()

    # Development
    if True:
        # GitHub
        def GitHub():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "github-desktop"
            Method = "yay"

            # Installer
            InstallSinglePackage()
        
        # Code
        def VisualStudio():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "visual-studio-code"
            Method = "yay"

            # Installer
            InstallSinglePackage()
        
        # Pycharm
        def Pycharm():
            
            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "pycharm-community-edition"
            Method = "pacman"

            # Installer
            InstallSinglePackage()

        # Godot
        def Godot():
            
            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "godot"
            Method = "pacman"

            # Installer
            InstallSinglePackage()
        
        # Development
        def Development():
        
            # Github
            GitHub()
            # VisualStudio
            VisualStudio()
            # Pycharm
            Pycharm()
            # Godot
            Godot()

    # Essentials
    if True:
        # Neofetch
        def Neofetch():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "neofetch"
            Method = "pacman"

            # Installer
            InstallSinglePackage()
        
        # Htop
        def Htop():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "htop"
            Method = "pacman"

            # Installer
            InstallSinglePackage()
        
        # Flatpak
        def Flatpak():
            
            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "flatpak"
            Method = "pacman"

            # Installer
            InstallSinglePackage()

        # Esssentials
        def Essentials():
        
            # Neofetch
            Neofetch()
            # Htop
            Htop()
            # Flatpak
            Flatpak()
    
    # Extras
    if True:
        # Spotify
        def Spotify():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "spotify"
            Method = "flatpak"

            # Installer
            InstallSinglePackage()
        
        # Pamac
        def Pamac():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "pamac-all"
            Method = "yay"

            # Installer
            InstallSinglePackage()
    
    # Aesthetics
    if True:
        # BibataCursors
        def BibataCursors():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "bibata-cursor-theme"
            Method = "yay"

            # Installer
            InstallSinglePackage()
        
        # PapirusIcons
        def PapirusIcons():

            # Globals
            global Package
            global Method

            # Installer Options:
            Package = "papirus-icon-theme"
            Method = "pacman"

            # Installer
            InstallSinglePackage()
        
        # Aesthetics
        def Aesthetics():

            # BibataCursors
            BibataCursors()
            # PapirusIcons
            PapirusIcons()

# Loop
MenuLoop1 = True
Loop = True
while Loop:

    # Print
    os.system("clear")
    Logo()
    print("| 1 | - Install Via Menus")
    print("| 2 | - Install Via Search")
    print("| 3 | - QuickSetup")
    print("| 4 | - Remove Via Menus")
    print("| 5 | - Remove Via Search")
    print("| 6 | - Update All")
    print("| 7 | - Options")
    print("| 8 | <-Exit")
    print(Spacer)
    Option = str(input("| >>>"))
    os.system("clear")

    # Set Install
    if Option in ["1", "2", "3"]:
        Operation = "Install"
    # Set Remove
    elif Option in ["4", "5"]:
        Operation = "Remove"

    # Menu Install/Remove
    if Option in ["1", "4"]:

            # Print
            MenuLoop1 = True
            while MenuLoop1:
                Logo()
                print("| 1 | - Gaming")
                print("| 2 | - Development")
                print("| 3 | - Essentials")
                print("| 4 | - Extras")
                print("| 5 | - Aesthetics")
                print("| 6 | - ")
                print("| 7 | - ")
                print("| 8 | <-Back")
                print(Spacer)
                Option = str(input("| >>>"))
                os.system("clear")

                if Option in ["1"]:
                    # Loop
                    MenuLoop2 = True
                    while MenuLoop2:
                        # Print
                        Logo()
                        print("| 1 | - Steam")
                        print("| 2 | - Lutris")
                        print("| 3 | - Discord")
                        print("| 4 | - ")
                        print("| 5 | - ")
                        print("| 6 | - ")
                        print("| 7 | - All")
                        print("| 8 | <-Back")
                        print(Spacer)
                        Option = str(input("| >>>"))
                        os.system("clear")

                        if Option in ["1"]:
                            Steam()
                        elif Option in ["2"]:
                            Lutris()
                        elif Option in ["3"]:
                            Discord()
                        elif Option in ["7"]:
                            Gaming()
                        elif Option in ["8"]:
                            MenuLoop2 = False

                elif Option in ["2"]:
                    # Loop
                    MenuLoop2 = True
                    while MenuLoop2:
                        # Print
                        Logo()
                        print("| 1 | - GitHub-Desktop")
                        print("| 2 | - Vs-Code")
                        print("| 3 | - PyCharm")
                        print("| 4 | - Godot")
                        print("| 5 | - ")
                        print("| 6 | - ")
                        print("| 7 | - All")
                        print("| 8 | <-Back")
                        print(Spacer)
                        Option = str(input("| >>>"))
                        os.system("clear")

                        if Option in ["1"]:
                            GitHub()
                        elif Option in ["2"]:
                            VisualStudio()
                        elif Option in ["3"]:
                            Pycharm()
                        elif Option in ["4"]:
                            Godot()
                        elif Option in ["7"]:
                            Development()
                        elif Option in ["8"]:
                            MenuLoop2 = False

                elif Option in ["3"]:
                    # Loop
                    MenuLoop2 = True
                    while MenuLoop2:
                        # Print
                        Logo()
                        print("| 1 | - NeoFetch")
                        print("| 2 | - Htop")
                        print("| 3 | - Flatpak")
                        print("| 4 | - ")
                        print("| 5 | - ")
                        print("| 6 | - ")
                        print("| 7 | - All")
                        print("| 8 | <-Back")
                        print(Spacer)
                        Option = str(input("| >>>"))
                        os.system("clear")

                        if Option in ["1"]:
                            Neofetch()
                        elif Option in ["2"]:
                            Htop()
                        elif Option in ["3"]:
                            Flatpak()
                        elif Option in ["7"]:
                            Essentials()
                        elif Option in ["8"]:
                            MenuLoop2 = False

                elif Option in ["4"]:
                    # Loop
                    MenuLoop2 = True
                    while MenuLoop2:
                        # Print
                        Logo()
                        print("| 1 | - Spotify(Flatpak)")
                        print("| 2 | - Pamac(Add or Remove software)")
                        print("| 3 | - ")
                        print("| 4 | - ")
                        print("| 5 | - ")
                        print("| 6 | - ")
                        print("| 7 | - ")
                        print("| 8 | <-Back")
                        print(Spacer)
                        Option = str(input("| >>>"))
                        os.system("clear")

                        if Option in ["1"]:
                            Spotify()
                        elif Option in ["2"]:
                            Pamac()
                        elif Option in ["8"]:
                            MenuLoop2 = False

                elif Option in ["5"]:
                    # Loop
                    MenuLoop2 = True
                    while MenuLoop2:
                        # Print
                        Logo()
                        print("| 1 | - Bibata Cursors")
                        print("| 2 | - Papirus Icons")
                        print("| 3 | - ")
                        print("| 4 | - ")
                        print("| 5 | - ")
                        print("| 6 | - ")
                        print("| 7 | - All")
                        print("| 8 | <-Back")
                        print(Spacer)
                        Option = str(input("| >>>"))
                        os.system("clear")

                        if Option in ["1"]:
                            BibataCursors()
                        elif Option in ["2"]:
                            PapirusIcons()
                        elif Option in ["7"]:
                            Aesthetics()
                        elif Option in ["8"]:
                            MenuLoop2 = False

                elif Option in ["8"]:
                    MenuLoop1 = False

    # Search Install/Remove
    elif Option in ["2", "5"]:
        
        # Search Input
        Logo()
        print("Availible Package Managers")
        print(Spacer)
        print("Pacman/Yay")
        print("Flatpak")
        print("Snap")
        print("Apt/Dnf")
        print(Spacer)
        Option = str(input("SEARCH FOR A PACKAGE  >>>"))
        Option = Option.lower()
        os.system("clear")


        # Gaming
        if Option in ["steam"]:
            Steam()
        elif Option in ["lutris"]:
            Lutris()
        elif Option in ["discord"]:
            Discord()
        elif Option in ["game", "gaming"]:
            Gaming()

        # Development
        elif Option in ["github", "github desktop", "github-desktop"]:
            GitHub()
        elif Option in ["code", "visual-studio", "visual studio", "visual studio code", "visual-studio-code"]:
            VisualStudio()
        elif Option in ["pycharm", "pycharm community", "pycharm-community", "pycharm community edition", "pycharm-community-edition"]:
            Pycharm()
        elif Option in ["godot", "godot game engine", "godot-game-engine"]:
            Godot()
        elif Option in ["development", "coding"]:
            Development()

        # Essentials
        elif Option in ["neofetch"]:
            Neofetch()
        elif Option in ["htop"]:
            Htop()
        elif Option in ["flatpak"]:
            Flatpak()
        elif Option in ["essentials"]:
            Essentials()

        # Extra
        elif Option in ["spotify", "music"]:
            Spotify()
        elif Option in ["software", "add or remove software", "add-or-remove-software", "pamac"]:
            Pamac()

        # Aesthetic
        elif Option in ["icon", "icons", "papirus", "papirus-icon-theme", "papirus icon theme", "papirus-icons", "papirus icons"]:
            PapirusIcons()
        elif Option in ["cursor", "cursors", "bibata", "bibata-cursor", "bibata-cursors", "bibata cursor", "bibata cursors"]:
            BibataCursors()
        elif Option in ["aesthetic", "looks", "aesthetics", "look"]:
            Aesthetics()

        # Else
        else:
            
            # Search
            if Distro == "arch":
                # for x in range(1, (No. of packages + 1)
                for x in range(1, 5):
                    print("Package", x)

                    # Installer options
                    Package = Option

                    # Method Changer
                    if x == 1:
                        Method = "pacman"
                    elif x == 2:
                        Method = "yay"
                    elif x == 3:
                        Method = "flatpak"
                    elif x == 4:
                        Method = "snap"

                    InstallSinglePackage()

            # Compatibility Mode/s
            elif Distro == "debian/ubuntu":
                # for x in range(1, (No. of packages + 1)
                for x in range(1, 4):
                    print("Package", x)

                    # Installer options
                    Package = Option

                    # Method Changer
                    if x == 1:
                        Method = "flatpak"
                    elif x == 2:
                        Method = "snap"
                    elif x == 3:
                        Method = "apt"

                    InstallSinglePackage()
            
            elif Distro == "redhat/fedora":
                # for x in range(1, (No. of packages + 1)
                for x in range(1, 4):
                    print("Package", x)

                    # Installer options
                    Package = Option

                    # Method Changer
                    if x == 1:
                        Method = "flatpak"
                    elif x == 2:
                        Method = "snap"
                    elif x == 3:
                        Method = "dnf"

                    InstallSinglePackage()

    # Quick Setup
    elif Option in ["3"]:

            Logo()
            print("| 1 | - Herator's")
            print("| 2 | - Daft's")
            print("| 3 | - ")
            print("| 4 | - ")
            print("| 5 | - ")
            print("| 6 | - ")
            print("| 7 | - ")
            print("| 8 | <-Back")
            print(Spacer)
            Option = str(input(">>>"))
            os.system("clear")
            print(Spacer)

            # Herator's
            if Option in ["1"]:
                
                Steam()
                Lutris()
                Pycharm()
                Development()
                Essentials()
                Spotify()
                Aesthetics()

            # Daft's
            if Option in ["2"]:

                Steam()
                Lutris()
                Essentials()
                Aesthetics()

    # TO OTHER PEOPLE: Where is Options 4 And 5?
    #
    # Options 4 and 5 Use very similar methods to 1 and 2
    # As such I have intergrated them into each other
    # Which one to do is chosen by the variable 'Operation'
    # 'Operation' Is decided from the inputted number
    # Operation is then used in the 'InstallSinglePackage' Function to decide whether to install or unintstall
    # This Function will give an error if 'Operation' is not set to 'Install' or 'Remove' CAPITILASATION IMPORTANT
    #
    # Message From Herator2

    # Update Apps
    elif Option in ["6"]:

        print(Spacer)
        print("Starting Update")

        # Arch
        if Distro == "arch":
            os.system("yay -Syu")
            os.system("yay -c")

        # Compatibility
        elif Distro == "debian/ubuntu":
            os.system("apt update")
        elif Distro == "redhat/fedora":
            os.system("dnf update")

        # The rest
        os.system("flatpak update")
        os.system("snap refresh")
        print("Finished Update")

    # Options
    elif Option in ["7"]:

        print(Spacer)
        print("| 1 | - Set Distro To Arch")
        print("| 2 | - Set Distro To Debian/Ubuntu")
        print("| 3 | - Set Distro To RedHat/Fedora")
        print("| 4 | - ")
        print("| 5 | - ")
        print("| 6 | - ")
        print("| 7 | - ")
        print("| 8 | - Back")
        print(Spacer)
        Option = str(input(">>>"))
        os.system("clear")
        print(Spacer)

        # Arch
        if Option in ["1"]:
            Distro = "arch"
        
        elif Option in ["2"]:
            Distro = "debian/ubuntu"

        elif Option in ["3"]:
            Distro = "redhat/fedora"

    # Exit
    elif Option in ["8"]:

        print(Spacer)
        print("EXITING")
        Loop = False

# Exit
print("See Ya Next Time!")
