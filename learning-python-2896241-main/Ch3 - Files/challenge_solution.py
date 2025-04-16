# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
from typing import List

def file_info(dirlist: List[str], ext: str) -> int:
    """Calculate the total size of files with a specific extension."""
    total_size_in_bytes = 0
    for entry in dirlist:
        if entry.is_file() and entry.name.endswith(f".{ext}"):
            total_size_in_bytes += entry.stat().st_size
    return total_size_in_bytes

# Get a list of all the files in the current directory using scandir for efficiency
with os.scandir() as entries:
    dirlist = list(entries)

ext = "txt"
total_bytes = file_info(dirlist, ext)
print(f"Total size of {ext} files in current directory: {total_bytes} bytes")