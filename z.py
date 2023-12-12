import re

def resolve_references(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
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

    with open(output_filename, 'w') as outfile:
        outfile.writelines(resolved_lines)

# Example usage:
input_filename = 'include.expr'
output_filename = 'include.expr.out'
resolve_references(input_filename, output_filename)
