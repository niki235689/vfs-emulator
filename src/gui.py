"""Модуль графического интерфейса пользователя."""
import getpass
import socket
import tkinter as tk
from tkinter import scrolledtext
from src.shell_core import ShellEngine


class ShellWindow:
    """Графическое окно оболочки на tkinter."""

    def __init__(self, root: tk.Tk, engine: ShellEngine) -> None:
        """Инициализация элементов окна."""
        self.root = root
        self.engine = engine
        self._configure_window()
        self._build_widgets()

    def _configure_window(self) -> None:
        """Устанавливает заголовок и размеры окна."""
        user = getpass.getuser()
        host = socket.gethostname()
        self.root.title(f"Эмулятор [{user}@{host}]")
        self.root.geometry("700x450")

    def _build_widgets(self) -> None:
        """Создает терминальный текстовый блок и поле ввода."""
        self.text_area = scrolledtext.ScrolledText(
            self.root, bg="#1e1e1e", fg="#ffffff", insertbackground="white"
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(
            self.root, bg="#2d2d2d", fg="#ffffff", insertbackground="white"
        )
        self.entry.pack(fill=tk.X, side=tk.BOTTOM)
        self.entry.bind("<Return>", self._on_enter)
        self.entry.focus_set()

    def _on_enter(self, _event: tk.Event) -> None:
        """Событие нажатия клавиши Enter."""
        cmd_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.append_text(f"$ {cmd_text}\n")

        output, _ok = self.engine.execute(cmd_text)
        if output:
            self.append_text(f"{output}\n")

        if not self.engine.is_running:
            self.root.destroy()

    def append_text(self, message: str) -> None:
        """Добавляет текст в консольный вывод."""
        self.text_area.insert(tk.END, message)
        self.text_area.see(tk.END)