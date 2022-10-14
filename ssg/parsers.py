from distutils import extension
from typing import List
from pathlib import Path

class Parser:

  extensions: List[str] = []

  def __init__(self):
    pass
  
  def valid_extension(self, extension):
    return extension in self.extensions
  
  def parse(self, path: Path, source: Path, dest: Path):
    raise NotImplementedError
  
  def read(self, path):
    with open(path) as file:
      return file.read()
    
  def write(self, path, dest, content, ext):
    full_path = dest/path.with_suffix(ext).name
    
    with open(full_path, "wt") as file:
      file.write(content)
      