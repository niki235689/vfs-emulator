"""Модуль виртуальной файловой системы, работающей в памяти."""
import os
from typing import Dict, Any, Optional


class VirtualFS:
    """Файловая система, загруженная в оперативную память."""

    def __init__(self) -> None:
        """Инициализация корневого узла."""
        self.root: Dict[str, Any] = {"type": "dir", "children": {}}
        self.cwd = "/"

    def load_from_directory(self, base_dir: str) -> None:
        """Загружает структуру физической папки в память."""
        if not os.path.exists(base_dir):
            raise FileNotFoundError(f"VFS path not found: {base_dir}")
        self.root = self._read_node(base_dir)

    def _read_node(self, path: str) -> Dict[str, Any]:
        """Рекурсивно считывает директорию в древовидный словарь."""
        if os.path.isdir(path):
            children = {}
            for item in os.listdir(path):
                child_path = os.path.join(path, item)
                children[item] = self._read_node(child_path)
            return {"type": "dir", "children": children}
        return {"type": "file", "size": os.path.getsize(path)}

    def get_node(self, path: str) -> Optional[Dict[str, Any]]:
        """Ищет узел по абсолютному или относительному пути."""
        target = self._normalize_path(path)
        if target == "/":
            return self.root
        tokens = [p for p in target.split("/") if p]
        curr = self.root
        for part in tokens:
            if curr.get("type") != "dir":
                return None
            curr = curr.get("children", {}).get(part)
            if curr is None:
                return None
        return curr

    def _normalize_path(self, path: str) -> str:
        """Нормализует путь относительно cwd."""
        if path.startswith("/"):
            combined = path
        else:
            combined = os.path.join(self.cwd, path)
        return os.path.normpath(combined).replace("\\", "/")