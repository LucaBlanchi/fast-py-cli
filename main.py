import command_launcher

def main():
    comm_launcher = command_launcher.CommandLauncher()

    while comm_launcher.loop:
        command = input("py-cli >> ").split()
        comm_launcher.execute(command)

if __name__ == "__main__":
    main()
