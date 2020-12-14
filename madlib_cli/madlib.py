# Template -----------------------------------------------
bienvenidos = "Welcome to the Pirate Story. Please provide a word that matches the specified category!"
print(bienvenidos)

Noun = input('noun > ')
Adjective = input('adjective > ')
Verb = input('verb > ')
Adverb = input('adverb > ')
Noun2 = input('noun > ')
Adjective2 = input('adjective > ')
Pluralnoun = input('plural noun > ')
Bodypart = input('body part > ')
Noun3 = input('noun > ')
Noun4 = input('noun > ')
Noun5 = input('noun > ')
Noun6 = input('noun > ')
Bodypart2 = input('body part > ')

template = f"Ye can always pretend to be a bloodthirsty {Noun}, threatening everyone by waving yer {Adjective} sword in the air, but until ye learn to {Verb} like a pirate, ye'll never be {Adverb} accepted as an authentic {Noun2}. So here's what ye do: Cleverly work into yer daily conversations {Adjective2} private phrases such as \"Ahoy there, {Pluralnoun},\" Remember to drop all yer gs when ye say such words as sailin', spittin', and fightin'. This will give ye a/an {Bodypart} start to being recognized as a swashbucklin' {Noun3}. Once ye have the lingo down pat, it helps to wear a three-cornered {Noun4} on yer head, stash a/an {Noun5} in yer pants, and keep a/an {Noun6} perched atop yer {Bodypart2}. Aye, now ye be a real prirate!"
print(template)

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
parse_template("It was a {Adjective} and {Adjective} {Noun}.")

def merge(bare_temp, string):
    """Merge string words to the bare template"""
    merged_string = bare_temp.format(*string)
    return(merged_string)
merge("It was a {} and {} {}.", ("dark", "stormy", "night"))


# Attribution for chaining replace (didn't end up using after revising code): https://stackoverflow.com/questions/3411771/best-way-to-replace-multiple-characters-in-a-string

# Attribution for found flag was from first lab: https://stackoverflow.com/questions/20157108/if-else-statement-and-dictionary-in-python

# Attribution for format with multiple arguments (str.format(*args, **kwargs)): https://stackoverflow.com/questions/3395138/using-multiple-arguments-for-string-formatting-in-python-e-g-s-s

# Madlib Template: https://www.pinterest.com/pin/248120260697620838/