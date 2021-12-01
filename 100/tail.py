def tail(filepath, n):
   """Simulate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
   with open(filepath) as f:
      stream = f.read()
      lines = stream.splitlines()[-n:]
      return lines
