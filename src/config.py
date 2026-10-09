"""Модуль работы с конфигурацией приложения."""
import argparse
import sys
from typing import Optional


class AppConfig:
    """Хранилище настроек запуска эмулятора."""

    def __init__(
        self,
        vfs_path: Optional[str] = None,
        script_path: Optional[str] = None
    ) -> None:
        """Инициализация конфигурации."""
        self.vfs_path = vfs_path
        self.script_path = script_path

    def dump(self) -> str:
        """Возвращает параметры в формате ключ-значение."""
        lines = [
            f"vfs_path={self.vfs_path or ''}",
            f"script_path={self.script_path or ''}"
        ]
        return "\n".join(lines)


def parse_arguments() -> AppConfig:
    """Разбор аргументов командной строки."""
    parser = argparse.ArgumentParser(description="VFS Shell Emulator")
    parser.add_argument("--vfs", type=str, help="Path to VFS directory")
    parser.add_argument("--script", type=str, help="Startup script path")
    args = parser.parse_args()

    cfg = AppConfig(vfs_path=args.vfs, script_path=args.script)
    _print_debug_info(cfg)
    return cfg


def _print_debug_info(cfg: AppConfig) -> None:
    """Отладочный вывод параметров эмулятора."""
    sys.stdout.write("[DEBUG] Configuration loaded:\n")
    sys.stdout.write(f"[DEBUG] VFS path: {cfg.vfs_path}\n")
    sys.stdout.write(f"[DEBUG] Script path: {cfg.script_path}\n")
    sys.stdout.flush()