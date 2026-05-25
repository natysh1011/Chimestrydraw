# -*- coding: utf-8 -*-

import os


RECENT_FILES_LIMIT = 15


def normalize_recent_files(paths, max_items=RECENT_FILES_LIMIT):
    """Return unique, existing absolute paths preserving order."""
    result = []
    seen = set()
    for path in paths or []:
        if not path:
            continue
        abspath = os.path.abspath(path)
        if abspath in seen or not os.path.isfile(abspath):
            continue
        seen.add(abspath)
        result.append(abspath)
        if len(result) >= max_items:
            break
    return result


def push_recent_file(paths, filename, max_items=RECENT_FILES_LIMIT):
    """Put filename at top of recent paths while keeping unique ordering."""
    if not filename:
        return normalize_recent_files(paths, max_items=max_items)

    abspath = os.path.abspath(filename)
    if not os.path.isfile(abspath):
        return normalize_recent_files(paths, max_items=max_items)

    items = [abspath]
    for path in paths or []:
        if not path:
            continue
        candidate = os.path.abspath(path)
        if candidate != abspath:
            items.append(candidate)
    return normalize_recent_files(items, max_items=max_items)
