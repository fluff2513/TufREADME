import questionary
from rich import print
import subprocess

subprocess.run("clear")
print("[red]T[/red][orange3]u[/orange3][yellow]f[/yellow][bright_green]M[/bright_green][bright_blue]D[/bright_blue] - The [bold]TUFFIEST[/bold] README file creator!")
name = questionary.text("What is the name of your project? :").ask()
author = questionary.text(f"Who is the author of {name}? :").ask()
description = questionary.text(f"What is the description of {name}? :").ask()
installation = questionary.text(f"How the user can install {name}? :").ask()
usage = questionary.text(f"What is the usage of {name}? :").ask()
license_ = questionary.select(
    f"What is the license of {name}?",
    choices=["MIT", "Apache 2.0", "GPL v3", "None"]
).ask()

with open(f"README.md", "w") as f:
    f.write(f"""# {name}
{description}
## 🌴 Installation
{installation}
## 🎀 Usage
{usage}
## 🚀 License
{license_}'s license
            
Made with ❤️ by {author}""")

print(f"""[bright_green]{name} README.md file succesfully create! :)[/bright_green]
You are now free to edit your fresh [bold]README[/bold]
Made by @Fluff2513 on GitHub.""")