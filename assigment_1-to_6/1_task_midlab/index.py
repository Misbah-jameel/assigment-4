

# Mad Libs Project - Attractive and Interactive Version

# Colorful Text (Optional)
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# Welcome Message
print(colors.HEADER + "🌟 Welcome to the Ultimate Mad Libs Generator! 🌟" + colors.END)
print(colors.BLUE + "Let's create a fun and crazy story together!" + colors.END)

# Inputs with Prompts
noun = input(colors.GREEN + "Enter a noun (e.g., cat, city, dream): " + colors.END)
verb = input(colors.YELLOW + "Enter a verb (e.g., run, dance, explore): " + colors.END)
noun2 = input(colors.GREEN + "Enter another noun (e.g., mountain, pizza, adventure): " + colors.END)
noun3 = input(colors.GREEN + "Enter one more noun (e.g., friend, treasure, mystery): " + colors.END)
verb2 = input(colors.YELLOW + "Enter another verb (e.g., jump, sing, discover): " + colors.END)
noun4 = input(colors.GREEN + "Enter a final noun (e.g., journey, party, secret): " + colors.END)

# Mad Libs Story
madlibs = (
    f"\n{colors.RED}🌟 Here's Your Mad Libs Story! 🌟{colors.END}\n"
    f"Hey! Welcome to my {colors.BLUE}{noun}{colors.END}. "
    f"Here, we {colors.YELLOW}{verb}{colors.END} about {colors.BLUE}{noun2}{colors.END} "
    f"and we have fun with {colors.BLUE}{noun3}{colors.END}. "
    f"Make sure you {colors.YELLOW}{verb2}{colors.END} to my {colors.BLUE}{noun4}{colors.END}!"
)

# Print the Story
print(madlibs)
print(colors.HEADER + "\nThanks for playing! 😄" + colors.END)