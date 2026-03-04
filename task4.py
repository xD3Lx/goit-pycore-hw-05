def input_error(func):
    """
    A decorator that handles common errors in command processing functions.
    This decorator wraps functions to catch and handle specific exceptions that may
    occur during execution, returning user-friendly error messages instead of raising
    exceptions.
    Catches:
        KeyError: Returns "Contact does not exist." when a contact key is not found.
        ValueError: Returns "Enter the argument for the command" when the required number of arguments is incorrect.
        IndexError: Returns "Enter the correct number of arguments for the command." when required arguments are missing.
    Returns:
        function: A wrapper function that executes the decorated function with error handling.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact does not exist."
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "Enter the correct number of arguments for the command."
    return inner

@input_error
def parse_input(user_input):
    """
    Parse user input into a command and its arguments.
    Args:
        user_input (str): The raw user input string to be parsed.
    Returns:
        tuple: A tuple containing the command (str) as the first element,
               followed by any number of arguments (str) as remaining elements.
    """

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    Args:
        args (tuple): A tuple containing two elements:
            - name (str): The name of the contact to add.
            - phone (str): The phone number of the contact.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A message indicating whether the contact was successfully added or if it already exists.
            - "Contact added." if the contact was successfully added.
            - "Contact {name} already exists." if a contact with the same name already exists.
    """

    name, phone = args
    if name in contacts:
        return f"Contact {name} already exists."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Update an existing contact's phone number.
    Args:
        args (tuple): A tuple containing two elements:
            - name (str): The name of the contact to update.
            - phone (str): The new phone number for the contact.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A message indicating whether the contact was successfully updated
             or if the contact does not exist.
    """

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:        
        return f"Contact {name} does not exist."

@input_error
def show_phone(args, contacts):
    """
    Retrieve and display the phone number for a given contact.
    Args:
        args (list): A list containing the contact name as the first element.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: The phone number associated with the contact name, or an error message 
             if the contact does not exist.
    """

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} does not exist."

@input_error
def all(args, contacts):
    """
    Display all contacts from the contacts dictionary.
    Args:
        args (list): A list of arguments (should be empty for this command).
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A string containing all contacts in the format "name: phone" separated by newlines,
             or "No contacts found." if the contacts dictionary is empty.
    """

    output = []

    if (len(contacts) == 0):
        return "No contacts found."
    else:
        for name, phone in contacts.items():
            output.append(f"{name}: {phone}")
        return "\n".join(output)

@input_error
def close(args, contacts):
    return "Good bye!"

@input_error
def hello(args, contacts):
    return "How can I help you?"


COMMANDS_TO_HANDLERS = {
    "exit": close,
    "close": close,
    "hello": hello,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": all  
}


def handle_command(command, args, contacts):
    """
    Route and execute commands based on user input.
    Args:
        command (str): The command name to be executed.
        args (list): Arguments to pass to the command handler.
        contacts (dict): The contacts dictionary to operate on.
    Returns:
        str: The result of the command execution, or an error message if the command is invalid.
    Note:
        Supported commands: exit, close, hello, add, change, phone, all
    """

    handler = COMMANDS_TO_HANDLERS.get(command)
    if handler:
        return handler(args, contacts)
    else:
        return "Invalid command."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # Get user input and parse it into a command and arguments
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        print(handle_command(command, args, contacts))

        # Check if the command is "close" or "exit" to terminate the chat
        if command in ["close", "exit"]:
            break

if __name__ == "__main__":
    main()