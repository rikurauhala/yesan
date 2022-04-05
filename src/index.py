from tkinter import Tk

from ui.user_interface import UserInterface


def main():
    """Main function of the program."""
    window = Tk()
    title = "Yesan"
    window.title(title)

    ui = UserInterface(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
