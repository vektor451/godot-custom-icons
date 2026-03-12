# Script to automate adding preview images of icons to the readme.txt. 
# Currently doesn't support subdirectories deeper than 1 level.

import os

README_PATH = "./README.md"
SCAN_PATH = "./"
UPDATE_FROM = "## Icon Previews:" # The previews will occur after this string in the readme.md
NO_ICON_DIR_STR = "There are currently no icons in this category. Feel free to commit your own!"

# Get existing file text.
readme_file = open(README_PATH, "r+t")
readme_text = readme_file.read()
readme_file.close()

# Process existing contents to remove text after UPDATE_FROM
readme_text = readme_text.partition(UPDATE_FROM)[0] + UPDATE_FROM + "\n"

# Generate previews
# Generate a section for each subdirectory
for dir in os.listdir(SCAN_PATH):
    if os.path.isdir(dir) and not dir.startswith('.'):        
        readme_text += f"<details>\n<summary>{dir}</summary>\n\n"

        subdir_path = SCAN_PATH + dir + "/"
        amount_of_valid_files = 0

        # Generate actual previews for individual icons.
        for icon in os.listdir(subdir_path):
            if icon.upper().endswith(".SVG"):
                readme_text += f"![{icon}]({subdir_path + icon}) "
                amount_of_valid_files += 1

        if amount_of_valid_files == 0:
            readme_text += NO_ICON_DIR_STR

        readme_text += "\n</details>\n\n"

# Write final contents to file.
readme_file = open(README_PATH, "w+t")
readme_file.write(readme_text)
