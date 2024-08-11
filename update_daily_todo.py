import re
import os
from datetime import datetime

def get_latest_todo_file(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.md') and f[0].isdigit()]
    return max(files, key=lambda x: datetime.strptime(x[:10], '%m-%d-%Y')) if files else None

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='iso-8859-1') as file:
            return file.read()

def write_file_content(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_todo_section(section):
    lines = section.split('\n')
    return '\n'.join([line.replace('[x]', '[ ]') if line.strip().startswith('- [') else line for line in lines])

def process_projects_section(section):
    lines = section.split('\n')
    processed_lines = []
    current_h2 = None
    h2_has_unchecked = False
    current_indent = ''
    parent_unchecked = False

    for line in lines:
        if line.strip().startswith('## '):
            if current_h2 and h2_has_unchecked:
                processed_lines.extend(current_h2)
            current_h2 = [line]
            h2_has_unchecked = False
            current_indent = ''
            parent_unchecked = False
        elif current_h2 is not None:
            checkbox_match = re.match(r'^(\s*)-\s*\[([ x])\]\s*(.*)$', line)
            if checkbox_match:
                indent, status, text = checkbox_match.groups()
                if len(indent) > len(current_indent):
                    if parent_unchecked:
                        current_h2.append(line)
                        h2_has_unchecked = True
                elif len(indent) <= len(current_indent):
                    current_indent = indent
                    parent_unchecked = (status == ' ')
                    current_h2.append(line)
                    if status == ' ':
                        h2_has_unchecked = True
            else:
                current_h2.append(line)

    if current_h2 and h2_has_unchecked:
        processed_lines.extend(current_h2)

    return '\n'.join(processed_lines)

import re
import os
from datetime import datetime

def update_todo_list():
    base_dir = r"C:\Users\17272\Documents\Obsidian\CodeWars"
    todo_directory = os.path.join(base_dir, "6 - Main Notes", "DAILY TODO")
    template_directory = os.path.join(base_dir, "5 - Templates")
    
    latest_file = get_latest_todo_file(todo_directory)
    if not latest_file:
        print("No previous todo file found.")
        return
    
    file_path = os.path.join(todo_directory, latest_file)
    content = read_file_content(file_path)

    # Split content into main sections
    sections = re.split(r'(^# .*$)', content, flags=re.MULTILINE)
    processed_sections = []

    for i in range(1, len(sections), 2):
        header = sections[i]
        body = sections[i+1] if i+1 < len(sections) else ""
        
        if "TODO" in header:
            processed_body = process_todo_section(body)
        elif "Projects" in header:
            processed_body = process_projects_section(body)
            print("Projects section is being processed")
        else:
            processed_body = body
        
        processed_sections.extend([header, processed_body])

    processed_content = ''.join(processed_sections)

    # Update the template file
    template_path = os.path.join(template_directory, '{{date}}.md')
    write_file_content(template_path, processed_content)
    print(f"Template file {{{{date}}}}.md has been updated.")

    # Create new file for current date
    current_date = datetime.now().strftime('%m-%d-%Y')
    new_filename = f"{current_date}.md"
    new_file_path = os.path.join(todo_directory, new_filename)
    
    # Replace {{date}} with current date in the content
    new_content = processed_content.replace('{{date}}', current_date)
    
    write_file_content(new_file_path, new_content)
    print(f"Updated todo list created: {new_filename}")

if __name__ == "__main__":
    update_todo_list()