import operations

print("Welcome To MinShell")

while True:
    user_input = input("DK-Shell => ").strip()

    command_split = user_input.split()
    command = ''
    argument = ''

    try:
        command = command_split[0]
        argument = command_split[1:] # For Multi Word Argument, We Will Take All The Words After The Command As Argument.
        argument = ' '.join(argument) # For Multi Word Argument, We Will Join It With Space.

    except IndexError:
        command = command_split[0]

    if command in operations.commands_line:
        if argument:
            operations.commands_line.get(command)(argument)
        else:
            operations.commands_line.get(command)()

    else:
        print(f"{command}: Command Not Found, Type 'help' For More Information.")
