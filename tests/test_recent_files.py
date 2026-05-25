import os
import tempfile
import unittest

from chemcanvas.recent_files import normalize_recent_files, push_recent_file


class TestRecentFilesHelpers(unittest.TestCase):
    def test_normalize_recent_files_keeps_existing_unique_paths(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            first = os.path.join(temp_dir, "a.ccdx")
            second = os.path.join(temp_dir, "b.ccdx")
            with open(first, "w", encoding="utf-8"):
                pass
            with open(second, "w", encoding="utf-8"):
                pass

            items = normalize_recent_files([first, second, first, os.path.join(temp_dir, "missing.ccdx")])
            self.assertEqual(items, [first, second])

    def test_push_recent_file_moves_item_to_top(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            first = os.path.join(temp_dir, "a.ccdx")
            second = os.path.join(temp_dir, "b.ccdx")
            with open(first, "w", encoding="utf-8"):
                pass
            with open(second, "w", encoding="utf-8"):
                pass

            items = push_recent_file([first, second], second)
            self.assertEqual(items, [second, first])


if __name__ == "__main__":
    unittest.main()
