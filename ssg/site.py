from genericpath import exists
from msilib.schema import Directory
from os import mkdir
from pathlib import Path 

class Site:
  
  def __init__(self, source, dest):
    source = self.Path(source)
    dest = self.Path(dest)
    
  def create_dir(self, path):
    directory = self.dest/ path.relative_to(self.source)
    directory.mkdir(parents = True, exist_ok = True)
    
  def build(self):
    self.dest.mkdir(parents = True, exist_ok = True)
    
    for path in self.source.rglob("*"):
      if path.is_directory():
        self.create_dir(path)