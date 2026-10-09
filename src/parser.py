"""Модуль лексического анализа командной строки."""
import shlex
from typing import List


def parse_command_line(cmd_str: str) -> List[str]:
    """Разбивает строку на лексемы с учетом кавычек."""
    cleaned = cmd_str.strip()
    if not cleaned:
        return []
    return shlex.split(cleaned)