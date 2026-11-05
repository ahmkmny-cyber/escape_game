from auth import start
from menu import menu

if __name__ == "__main__":
    while True:
        username=start()
        if username:
            menu(username)
        else:
            break