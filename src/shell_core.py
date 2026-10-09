"""Ядро эмулятора командной оболочки."""
from typing import List, Tuple
from src.config import AppConfig
from src.vfs import VirtualFS
from src.parser import parse_command_line


class ShellEngine:
    """Обработчик команд и состояния сессии."""

    def __init__(self, config: AppConfig, vfs: VirtualFS) -> None:
        """Инициализирует зависимости оболочки."""
        self.config = config
        self.vfs = vfs
        self.is_running = True

    def execute(self, line: str) -> Tuple[str, bool]:
        """Выполняет одну строковую команду. Возвращает (вывод, статус)."""
        tokens = parse_command_line(line)
        if not tokens:
            return "", True

        cmd, args = tokens[0], tokens[1:]
        handler = getattr(self, f"cmd_{cmd}", None)
        if handler is None:
            return f"Error: command not found: {cmd}", False
        return handler(args)

    def cmd_exit(self, _args: List[str]) -> Tuple[str, bool]:
        """Завершает работу эмулятора."""
        self.is_running = False
        return "Session terminated.", True

    def cmd_ls(self, args: List[str]) -> Tuple[str, bool]:
        """Заглушка команды ls."""
        args_repr = ", ".join(repr(a) for a in args)
        return f"[STUB] ls called with args: [{args_repr}]", True

    def cmd_cd(self, args: List[str]) -> Tuple[str, bool]:
        """Заглушка команды cd."""
        args_repr = ", ".join(repr(a) for a in args)
        return f"[STUB] cd called with args: [{args_repr}]", True

    def cmd_conf_dump(self, _args: List[str]) -> Tuple[str, bool]:
        """Выводит текущую конфигурацию."""
        return self.config.dump(), True