"""Точка входа эмулятора."""
import sys
import tkinter as tk
from src.config import parse_arguments, AppConfig
from src.vfs import VirtualFS
from src.shell_core import ShellEngine
from src.gui import ShellWindow


def run_script(engine: ShellEngine, path: str, win: ShellWindow) -> None:
    """Выполняет стартовый скрипт, прекращая работу при ошибке."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError as err:
        win.append_text(f"Script Error: Cannot read file: {err}\n")
        return

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        win.append_text(f"$ {line}\n")
        output, success = engine.execute(line)
        if output:
            win.append_text(f"{output}\n")
        if not success:
            win.append_text(f"Script Error: halted at '{line}'\n")
            break
        if not engine.is_running:
            break


def main() -> None:
    """Запуск приложения."""
    config = parse_arguments()
    vfs = VirtualFS()

    if config.vfs_path:
        try:
            vfs.load_from_directory(config.vfs_path)
            sys.stdout.write("[DEBUG] VFS mounted successfully.\n")
        except FileNotFoundError as err:
            sys.stderr.write(f"[ERROR] {err}\n")

    engine = ShellEngine(config, vfs)
    root = tk.Tk()
    window = ShellWindow(root, engine)

    if config.script_path:
        run_script(engine, config.script_path, window)

    root.mainloop()


if __name__ == "__main__":
    main()