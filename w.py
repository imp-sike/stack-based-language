import re

def replace_whitespace_with_nbsp(match):
    return match.group(0).replace(' ', '&nbsp;')

def process_file(file_path):
    with open(file_path + ".i1", 'r') as file:
        content = file.read()

    # Define a regular expression to match text inside double quotes
    pattern = re.compile(r'"(.*?)"')

    # Use a function to replace whitespace with "&nbsp;" inside the matched text
    modified_content = pattern.sub(replace_whitespace_with_nbsp, content)

    # Write the modified content back to the file
    with open(file_path + ".intermediate", 'w') as file:
        file.writelines(modified_content)
    return file_path + ".intermediate"

def resolve_references(file_path):
    with open(file_path, 'r') as infile:
        lines = infile.readlines()

    resolved_lines = []
    for line in lines:
        match = re.match(r'{(.+\.expr)}', line)
        if match:
            reference_filename = match.group(1)
            with open(reference_filename, 'r') as reference_file:
                referenced_content = reference_file.read()
            resolved_lines.append(referenced_content)
        else:
            resolved_lines.append(line)

    with open(file_path + ".i1", 'w') as outfile:
        outfile.writelines(resolved_lines)

def parse_number(word):
    try:
        result = int(word)
    except ValueError:
        try:
            result = float(word)
        except ValueError:
            raise ValueError("Could not parse the word as a number")
    return result