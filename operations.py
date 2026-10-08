import os

def help_user(noth='') -> None:
    """This Method Will Display All Available Commands Line."""
    if not noth:
        print("Available Commands Line:")
        print("------------------------")

        for command_line in commands_line:
            print(command_line)
    else:
        print("Can not 'help' command has argument yet")

    return

# ====================================

def list_show(dir='.') -> None:
    """This Method Will Display The Folders And Files 
        In Current Direction As Default Or The Given Directory."""

    try:
        with os.scandir(dir) as dir_content:
            for content in dir_content:
                print(content.name)

    except FileNotFoundError:
        # print("File or directory not found")
        print(f"ls => {dir}: No such file or directory")

    return

# ====================================

def clear_screen(noth='') -> None:
    """This Method Will Clear The Screen By
        Using The Command Line Command 'cls' For Windows
        And 'clear' For Linux And MacOS."""
    
    if not noth:
        os.system("cls" if os.name == "nt" else "clear")

    else:
        print("Can not 'clear' command has argument")

    return

# ====================================

def current_work_dir(noth='') -> None:
    """This Method Will Return The Current Work Directory."""

    if not noth:
        current_dir = os.getcwd()
        print(current_dir)

    else:
        print("Can not 'cwd' command has argument")

    return

# ====================================

def change_dir(dir='') -> None:
    """This Method Will Change The Current Directory To 
        The Root As Default Or The Given Directory."""

    if not dir:
        dir = os.path.expanduser('~') # Change To Home Directory If No Argument Is Given.

    try:
        os.chdir(dir)

    except FileNotFoundError:
        print(f"cd => {dir}: No such file or directory")

    return

# ====================================

def exit_shell(noth='') -> None:
    """This Method Will Exit From The Shell."""

    print("Created By Dark-Knight:-")
    exit()

# ====================================

commands_line = { # If You Will Add New Command Line, You Must Add It Here.

    "ls": list_show,
    "clear": clear_screen,
    "cwd": current_work_dir,
    "cd": change_dir,
    "exit": exit_shell,
    "help": help_user,

}
