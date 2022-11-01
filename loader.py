import os
import sys
import importlib.util

def import_from_path(path):
  spec = importlib.util.spec_from_file_location('__dynamic__', path)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  return module

def load(path: str):
  def recurse(path, files):
    for f in os.scandir(path):
      fp = os.path.join(path, f)
      if os.path.isfile(fp):
        files.append(import_from_path(fp))
    return files
  return recurse(os.path.join(os.getcwd(), path), [])