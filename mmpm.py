import sys, requests, json
class MMPMCommand:
  def __init__(self, function, arguments):
    self.arguments = arguments
    self.callback = function
  def __call__(self, *args):
    if len(args) < self.arguments:
      print(f'Not enough arguments, expected {self.arguments}, got {len(args)}')
      exit(1)
    self.callback(*args)
def sync(package):
  package = requests.get(f'https://www.graffbt.com/mmpm/{package}.json')
  if package.status != 200:
    print(f'Failed to get package, status code {package.status}')
    exit(1)
  filename = f'{package}.json'
  file = open(filename, 'w')
  file.write(package.body)
def update():
  db = requests.get(f'https://www.graffbt.com/mmpm/all.json')
  if db.status != 200:
    print(f'Failed to get database, status code {package.status}')
    exit(1)
  for i in db.json()['urls']:
    print(f'Get {i}')
    package = requests.get(f'https://www.graffbt.com/mmpm/{package}.json')
    if package.status != 200:
        print(f'Miss {package.status}')
    else:
      print('Hit')
      filename = f'{package}.json'
      file = open(filename, 'w')
      file.write(package.body)
    
    
  
commands = {'sync':MMPMCommand(sync, 1), 'update':MMPMCommand(update, 0)}
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
