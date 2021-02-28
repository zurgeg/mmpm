import sys
class MMPMCommand:
  def __init__(self, function, arguments):
    self.arguments = arguments
    self.callback = function
  def __call__(self, *args):
    if len(args) < self.arguments:
      print(f'Not enough arguments, expected {self.arguments}, got {len(args)}')
      exit(1)
    self.callback(*args)
    
commands = {}
def help():
  print('MMPM Commands')
  print('mmpm sync <package>: Gets a package\'s metadata from MMPI')
  print('mmpm update: Updates all package metadata')
  print('mmpm upgrade: Updates all packages')
  print('mmpm install <package>: Installs a package')
  print('mmpm install special.mm2: Installs MagicMirror2')
  print('mmpm -[-]h[elp]: Shows this message')
if len(sys.argv) < 2:
  help()
  print('Not enough arguments provided')
if sys.argv[1] == '-h' or sys.argv[1] == '--help':
  help()
if sys.argv[1] in list(commands.keys()):
  command = commands[sys.argv[1]]
  if command.arguments == 0:
    command()
  else:
    command(sys.argv[2:])
