# fast-py-cli
Template code for writing your own python command line utility tool quickly.

## How it works
main.py listens in loop to console commands. It splits them by spaces, the first word will be the command, and the next words will be the parameters.
Out of the box, it has a 'quit'/'q' command (does not need any param) that instructs main to stop looping. If the command is not found, the default behaviour
is executing the user command as bash.

## How to customize it
Add new methods to the CommandLauncher class (with the needed dependencies) taking in input the params as a list of Strings.
Bind methods to command names in the commands dictionary in the constructor.

## CREATE A BASH SCRIPT (Linux)
To launch the script as a command, without referencing its path, create a .sh file containing python3 {path-to-main.py} and move it to a folder in $PATH (echo $PATH to list them, usually /usr/local/bin). The script can now be executed in the terminal with {script-name}.sh.
