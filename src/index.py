from tkinter import Tk

from ui.user_interface import UserInterface


def main():
    """Main function of the program."""
    window = Tk()
    title = "Yesan"
    window.title(title)

    user_interface = UserInterface(window)
    user_interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
