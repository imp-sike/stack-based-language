import re

def replace_whitespace_with_nbsp(match):
    return match.group(0).replace(' ', '&nbsp;')

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Define a regular expression to match text inside double quotes
    pattern = re.compile(r'"(.*?)"')

    # Use a function to replace whitespace with "&nbsp;" inside the matched text
    modified_content = pattern.sub(replace_whitespace_with_nbsp, content)

    # Write the modified content back to the file
    with open(file_path + ".intermediate", 'w') as file:
        file.write(modified_content)
    return file_path + ".intermediate"
