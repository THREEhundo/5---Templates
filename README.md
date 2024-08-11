# Daily Todo Script

## Overview

The Daily Todo Script is a Python utility designed to manage and update daily
todo lists in an Obsidian vault. It processes the previous day's todo items,
carries over incomplete tasks, and creates a new file for the current day's
todos.

## Features

-   Automatically reads the most recent todo file
-   Processes and updates the TODO section:
    -   Resets all checkboxes to unchecked state
-   Processes and updates the Projects section:
    -   Maintains uncompleted tasks and their subtasks
    -   Removes completed tasks and their subtasks
    -   Preserves the hierarchy of tasks and subtasks
-   Creates a new todo file for the current date
-   Updates a template file for future use
-   Customizable for different Obsidian vault structures

## Requirements

-   Python 3.6 or higher
-   An Obsidian vault with:
    -   A directory for daily todo files
    -   A directory for template files

## Customization

Before using the script, you need to customize it for your Obsidian vault
structure:

1. Open the script in a text editor.
2. Locate the following lines at the beginning of the `update_todo_list()`
   function:

```python
base_dir = r"C:\Users\Your\File\Path\Here"
todo_directory = os.path.join(base_dir, "Main Notes", "DAILY TODO")
template_directory = os.path.join(base_dir, "Templates")
```

3. Modify these paths to match your Obsidian vault structure:
    - Update `base_dir` to point to your Obsidian vault's root directory
    - Adjust `todo_directory` to point to where you keep your daily todo files
    - Change `template_directory` to where you want to store the template file

For example, if your structure is different, you might change it to:

```python
base_dir = r"C:\Users\YourUsername\Obsidian\MyVault"
todo_directory = os.path.join(base_dir, "Daily Notes")
template_directory = os.path.join(base_dir, "Templates")
```

## Usage

1. After customizing the script for your vault structure, place it in a
   convenient location.
2. Run the script:

```bash
python daily_todo_script.py
```

The script will automatically find the most recent todo file in your specified
directory, process it, update the template, and create a new file for the
current date.

## File Structure

The script expects todo files to have the following structure:

```markdown
Status:

Tags:

# TODO

> [!warning] Daily Todo
>
> -   [ ] Task 1
> -   [ ] Task 2

> [!abstract] Miscellaneous Todo
>
> -   [ ] Task 3

# Projects

## Project 1

-   [ ] Main Task 1
    -   [ ] Subtask 1.1
    -   [x] Subtask 1.2

## Project 2

-   [x] Completed Task
-   [ ] Ongoing Task
```

## Notes

-   The script preserves the structure and formatting of the original todo file.
-   It only modifies checkbox states and removes completed tasks in the Projects
    section.
-   Make sure to backup your Obsidian vault before running the script for the
    first time.
-   The script creates a new file each day, so ensure you have enough storage
    space.

## Troubleshooting

If you encounter any issues:

1. Double-check that you've correctly set the file paths for your specific
   Obsidian vault structure.
2. Ensure that your todo files follow the expected format.
3. Review the console output for any error messages.
4. If the script can't find your todo files, verify that you're using the
   correct directory names and that the files exist.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit
issues or pull requests on the project repository.

## License

This script is released under the MIT License. See the LICENSE file for more
details.
