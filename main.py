import operations

print("Welcome To MinShell")

while True:
    user_input = input("DK-Shell => ").strip()

    command_split = user_input.split()
    command = ''
    argument = ''

    try:
        command = command_split[0]
        argument = command_split[1:]
        # print(argument)
        argument = ' '.join(argument)

    except IndexError:
        command = command_split[0]

    # print(command)
    # print(argument)
    # break

    if command in operations.commands_line:
        if argument:
            operations.commands_line.get(command)(argument)
        else:
            operations.commands_line.get(command)()

    else:
        print(f"{command}: Command Not Found, Type 'help' For More Information.")
