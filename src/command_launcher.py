import subprocess

class CommandLauncher:
    
    def __init__(self):
        self.loop = True

        self.commands = {
            'quit': self.quit,
            'q': self.quit,
        }

    def quit(self, params):
        self.loop = False
    
    def execute(self, command):
        method_name = command[0]
        params = command[1:]

        method = self.commands.get(method_name, None)
        if method != None:
            return method(params)
        else:
            subprocess.run(command)
