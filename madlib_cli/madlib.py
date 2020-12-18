import re
def welcome_message():
    """Prints welcome message.
    """
    bienvenidos = "Welcome to the Pirate Story. Please provide a word that matches the specified category!"
    print(bienvenidos)

def get_user_input(prompt):
    """Prompts the user for their input.

    Args:
        prompt (string): replacement word

    Returns:
        string : "Please enter {replacement word / prompt}"
    """
    user_input = input(f'Please enter {prompt}\n>>')
    return user_input

def collect_inputs(answer_list):
    """Collects input from user and puts it into a list.

    Args:
        answer_list (tuple): tuple of inputted answers from user

    Returns:
        [list]: returns a complete list of inputted answers
    """
    answers = []
    for question in answer_list:
        answer = get_user_input(question)
        answers.append(answer)
    return answers

# Read, Parse, Merge ---------------------------------------
def read_template(filepath):
    """Open and read file. If file not found, raise Exception Error"""
    try:
        with open(filepath, "r") as story:
            contents = story.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError('No such file or directory.')

def parse_template(tempstring):
    """Add each character from tempstring to stripped string, stopping at "{" if found. Append everything after the "}" to stripped string. Finally, add parts to parts list""" 
    found = False
    stripped = ""
    parts = []
    parts_char = ""

    for char in tempstring: 
        if not found:
            stripped += char
            if char == "{":
                found = True
        elif char == "}":
            found = False
            parts.append(parts_char)
            parts_char = ""
            stripped += char
        else:
            parts_char += char 
    return stripped, tuple(parts)

def merge(bare_temp, string):
    """Merge string words to the bare template"""
    merged_string = bare_temp.format(*string)
    return(merged_string)

# Save Template and Start Game ---------------------------------------
def save_template(template):
    """Saves the template to a filepath.

    Args:
        template (string): overwritten template with inputted answers
    """
    file = open("../assets/story.txt", 'w')
    file.write(template)
    file.close()

def start_game():
    """Starts the game and prints out the completed story!
    """
    welcome_message()
    string = read_template("../assets/template.txt")
    template, correct_list = parse_template(string)
    answers = collect_inputs(correct_list)
    completed = merge(template, answers)
    print(completed)

if __name__ == "__main__":
    start_game()


# Attribution for chaining replace (didn't end up using after revising code): https://stackoverflow.com/questions/3411771/best-way-to-replace-multiple-characters-in-a-string

# Attribution for found flag was from first lab: https://stackoverflow.com/questions/20157108/if-else-statement-and-dictionary-in-python

# Attribution for format with multiple arguments (str.format(*args, **kwargs)): https://stackoverflow.com/questions/3395138/using-multiple-arguments-for-string-formatting-in-python-e-g-s-s

# Madlib Template: https://www.pinterest.com/pin/248120260697620838/