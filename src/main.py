import sys
import tkinter as tk
from tkinter import messagebox


APP_NAME = "YourApp"


def on_hello():
    messagebox.showinfo(APP_NAME, "Привіт! Це portable .exe без встановленого Python ✨")


def main():
    root = tk.Tk()
    root.title(f"{APP_NAME} — мінімальний приклад")
    root.geometry("400x200")


    label = tk.Label(root, text="Натисни кнопку, щоб перевірити роботу.", font=("Segoe UI", 10))
    label.pack(pady=20)


    btn = tk.Button(root, text="Hello", command=on_hello)
    btn.pack(pady=10)


    root.mainloop()


if __name__ == "__main__":
    sys.exit(main())