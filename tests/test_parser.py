"""Тестирование парсера аргументов."""
import unittest
from src.parser import parse_command_line


class TestParser(unittest.TestCase):
    """Набор тестов для shlex-парсера."""

    def test_quoted_arguments(self) -> None:
        """Проверка строк с пробелами внутри кавычек."""
        res = parse_command_line('cd "My Folder" \'Another Path\'')
        self.assertEqual(res, ["cd", "My Folder", "Another Path"])

    def test_empty_string(self) -> None:
        """Проверка пустой строки."""
        self.assertEqual(parse_command_line("   "), [])