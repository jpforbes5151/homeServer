import re
import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

# not currently being used. Thinking of a way to dynamically update the markdown file then
# render the page again
def extract_variables(markdown_file):
    variables = {}
    
    # Define the regular expression pattern to match variables like {{ variable }}
    pattern = r'\{\{\s*(\w+)\s*\}\}'
    
    # Read the Markdown file
    with open(markdown_file, 'r') as file:
        markdown_content = file.read()
    
    # Find all matches of the pattern in the Markdown content
    matches = re.findall(pattern, markdown_content)
    
    # Extract variable names and add them to the variables dictionary
    for match in matches:
        variables[match] = None  # Initialize variables with None values
    
    return variables