def format_directory_tree(directory_tree):
    # Split the directory tree into lines
    lines = directory_tree.strip().split("\n")
    # Initialize a list to hold the formatted lines
    formatted_lines = []

    for line in lines:
        # Replace | and - with spaces
        formatted_line = line.replace("|", "").replace("-", "").replace("├", "").replace("─", "").replace("│", "").replace("└", "")
        formatted_lines.append(formatted_line)

    # Join the formatted lines back into a single string
    formatted_tree = "\n".join(formatted_lines)
    return formatted_tree

def remove_common_offset(directory_tree):
    lines = directory_tree.split("\n")
    # Ignore empty lines for determining the minimum offset
    # non_empty_lines = [line for line in lines if line.strip()]

    min_leading_spaces = min(len(line) - len(line.lstrip(' ')) for line in lines)

    if all(line.startswith(' ' * min_leading_spaces) or line == '' for line in lines):
        trimmed_lines = [line[min_leading_spaces:] for line in lines]
        trimmed_tree = "\n".join(trimmed_lines)
    else:
        trimmed_tree = directory_tree  # Return the original if not all lines have the offset

    return trimmed_tree

def parse_tree_to_files_array(tree_string):
    lines = tree_string.strip().split("\n")
    files_array = []
    current_path = []

    for line in lines:
        if not line.strip():
            continue  # Skip empty lines

        # Calculate the indentation level: assuming each level of indentation is 3 spaces
        indentation_level = (len(line) - len(line.lstrip())) // 3

        # Update the current_path to reflect the current indentation level
        current_path = current_path[:indentation_level]
        item = line.strip()

        # If the item is a file (has a '.'), add its full path to the files_array
        if "." in item:
            full_path = "/".join(current_path + [item])
            files_array.append(full_path)
        else:
            # Update the current path for directories
            current_path.append(item)

    return files_array

# formatted_tree = parse_tree_to_files_array(remove_common_offset(format_directory_tree(directory_tree)))
# formatted_tree = [item.replace("//", "/") for item in formatted_tree]

# print(formatted_tree)