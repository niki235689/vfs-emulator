"""Тестирование модуля VFS в оперативной памяти."""
import unittest
import tempfile
import os
from src.vfs import VirtualFS


class TestVFS(unittest.TestCase):
    """Проверка загрузки структуры директории в память."""

    def test_load_in_memory(self) -> None:
        """Проверка считывания трехуровневой папки."""
        with tempfile.TemporaryDirectory() as tmpdir:
            l1 = os.path.join(tmpdir, "l1")
            l2 = os.path.join(l1, "l2")
            os.makedirs(l2)
            with open(os.path.join(l2, "target.txt"), "w") as f:
                f.write("payload")

            vfs = VirtualFS()
            vfs.load_from_directory(tmpdir)
            node = vfs.get_node("l1/l2/target.txt")
            self.assertIsNotNone(node)
            self.assertEqual(node.get("type"), "file")